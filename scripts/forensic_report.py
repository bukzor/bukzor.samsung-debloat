#!/usr/bin/env python3
"""Analyze an Android forensic capture directory and print a report.

A capture is a directory of `adb shell dumpsys`/`pm`/`logcat`/`appops` outputs
(see `forensics/collect.sh`). This tool ingests one such directory and reports:

- logcat buffer coverage (how far back each buffer reaches);
- crashes attributed to a package;
- package install/remove events found in logcat (usually none — buffers are
  shallow; the account-side Play Library is the authoritative source);
- usagestats "removed-app candidates" (apps with recorded activity that are no
  longer installed) with last-active time;
- name-heuristic flags (a weak signal for review — never a verdict);
- third-party holders of sensitive appops (overlay / SMS / install-unknown);
- /sdcard/Download anomalies (hidden names, APKs, filename/mtime date drift).

All parsing is pure (text in, data out); only `main` touches the filesystem.
"""

import sys
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re

# Package-name prefixes treated as OS/vendor/carrier (not user-installed apps).
SYSTEM_PREFIXES = (
    "android",
    "com.android.",
    "com.google.",
    "com.samsung",
    "com.sec.",
    "com.samsung",
    "com.qualcomm.",
    "com.qti.",
    "qcom.",
    "vendor.",
    "org.codeaurora.",
    "com.skms.",
    "com.knox",
    "com.monotype.",
    "com.dsi.ant",
    "com.osp.app",
    "com.wssyncmldm",
    "com.wssnps",
    "com.sktelecom.",
    # carrier (Verizon family — this device's carrier image)
    "com.verizon.",
    "com.vzw.",
    "com.vcast.",
    "com.securityandprivacy.android.verizon",
    "com.synchronoss.",
)

# Substrings that recur in adware/PUP package names. A MATCH IS A FLAG, NOT A
# VERDICT: many legitimate apps match (a weather app is named for weather).
# Always confirm against the human's knowledge of their own apps.
SUSPICIOUS_KEYWORDS = (
    "clean", "boost", "antivirus", "virus", "security", "applock", "junk",
    "purge", "trash", "vault", "optimizer", "cooler", "speedup", "flashlight",
    "weather", "forecast", "navigation", "gpsmap", "translator", "caller",
    "wallpaper", "scanner", "vpn",
)

# logcat / dumpsys line patterns.
_TS = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
_BUFFER = re.compile(r"^-+ beginning of (\w+)")
_FATAL = re.compile(r"AndroidRuntime: FATAL EXCEPTION")
_CRASH_PROC = re.compile(r"AndroidRuntime: Process: ([^,]+), PID:")
_USAGE_SUMMARY = re.compile(
    r'package=(\S+).*?lastTimeUsed="([^"]*)".*?'
    r'lastTimeComponentUsed="([^"]*)".*?appLaunchCount=(\d+)'
)
_USAGE_EVENT = re.compile(r'time="([^"]+)" type=(\S+) package=(\S+)')
# install/remove logging across logcat buffers (PackageManager + events buffer).
_PKG_EVENT = re.compile(
    r"(Removing package|Finished install of|installPackage|deletePackageX?|"
    r"pkg_install|pkg_uninstall|sysui_view_visibility)\s.*?"
    r"\b([a-z][\w.]+\.[a-z][\w.]+)"
)
# a single `ls -l` row: perms links owner group size YYYY-MM-DD HH:MM name
_LS_ROW = re.compile(
    r"^([dlbcps-][rwxsStT-]{9})\s+\d+\s+\S+\s+\S+\s+(\d+)\s+"
    r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\s+(.+)$"
)
_LEADING_DATE = re.compile(r"^(\d{4})(\d{2})(\d{2})")


@dataclass(frozen=True, slots=True)
class UsageStat:
    package: str
    last_active: datetime | None
    foregrounded: bool
    launch_count: int


@dataclass(frozen=True, slots=True)
class Crash:
    package: str
    when: datetime | None


@dataclass(frozen=True, slots=True)
class BufferCoverage:
    buffer: str
    first: datetime
    last: datetime


@dataclass(frozen=True, slots=True)
class PkgEvent:
    when: datetime | None
    kind: str
    package: str


@dataclass(frozen=True, slots=True)
class DownloadEntry:
    directory: str
    name: str
    size: int
    mtime: datetime
    is_dir: bool


# ---------------------------------------------------------------------------
# pure parsers
# ---------------------------------------------------------------------------


def parse_ts(value: str) -> datetime | None:
    """Parse a dumpsys/logcat timestamp; epoch sentinel and blanks -> None."""
    value = value.strip()
    if not value:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.strptime(value, fmt)
        except ValueError:
            continue
        return None if dt.year < 2000 else dt
    return None


def is_system_package(package: str) -> bool:
    return package.startswith(SYSTEM_PREFIXES)


def parse_package_list(text: str) -> frozenset[str]:
    """`pm list packages` output: lines like `package:com.foo`."""
    out: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("package:"):
            out.add(line.removeprefix("package:").split()[0])
    return frozenset(out)


def parse_installer_map(text: str) -> Mapping[str, str]:
    """`pm list packages -i` output: `package:com.foo  installer=com.bar`."""
    out: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("package:"):
            continue
        body = line.removeprefix("package:")
        pkg = body.split()[0]
        installer = "unknown"
        for token in body.split():
            if token.startswith("installer="):
                installer = token.removeprefix("installer=")
        out[pkg] = installer
    return out


def parse_appop_holders(text: str) -> frozenset[str]:
    """`appops query-op ... allow` output: one bare package per line."""
    out: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line == "No operations." or " " in line or "." not in line:
            continue
        out.add(line)
    return frozenset(out)


def parse_usagestats(text: str) -> Mapping[str, UsageStat]:
    """Merge per-window summaries and the 24h event log into one stat/package."""
    last: dict[str, datetime | None] = {}
    launches: dict[str, int] = {}
    foreground: dict[str, bool] = {}

    def observe(pkg: str, when: datetime | None, *, fg: bool) -> None:
        if when is not None and (last.get(pkg) is None or when > last[pkg]):  # type: ignore[operator]
            last[pkg] = when
        if fg:
            foreground[pkg] = True
        foreground.setdefault(pkg, False)

    for line in text.splitlines():
        summary = _USAGE_SUMMARY.search(line)
        if summary:
            pkg, used, comp, count = summary.groups()
            launches[pkg] = max(launches.get(pkg, 0), int(count))
            used_dt, comp_dt = parse_ts(used), parse_ts(comp)
            observe(pkg, used_dt, fg=int(count) > 0 or used_dt is not None)
            observe(pkg, comp_dt, fg=False)
            continue
        event = _USAGE_EVENT.search(line)
        if event:
            when_s, etype, pkg = event.groups()
            observe(pkg, parse_ts(when_s), fg=etype.startswith("ACTIVITY_"))

    return {
        pkg: UsageStat(pkg, last.get(pkg), foreground.get(pkg, False),
                       launches.get(pkg, 0))
        for pkg in set(last) | set(launches) | set(foreground)
    }


def parse_logcat_coverage(lines: Iterable[str]) -> list[BufferCoverage]:
    bounds: dict[str, list[datetime]] = {}
    current = "unknown"
    for line in lines:
        marker = _BUFFER.match(line)
        if marker:
            current = marker.group(1)
            continue
        stamp = _TS.match(line)
        if not stamp:
            continue
        dt = parse_ts(stamp.group(1))
        if dt is None:
            continue
        if current not in bounds:
            bounds[current] = [dt, dt]
        else:
            bounds[current][0] = min(bounds[current][0], dt)
            bounds[current][1] = max(bounds[current][1], dt)
    return [BufferCoverage(b, lo, hi) for b, (lo, hi) in bounds.items()]


def parse_crashes(lines: Sequence[str]) -> list[Crash]:
    out: list[Crash] = []
    for i, line in enumerate(lines):
        if not _FATAL.search(line):
            continue
        stamp = _TS.match(line)
        when = parse_ts(stamp.group(1)) if stamp else None
        package = "unknown"
        for nxt in lines[i + 1 : i + 6]:
            proc = _CRASH_PROC.search(nxt)
            if proc:
                package = proc.group(1)
                break
        out.append(Crash(package, when))
    return out


def parse_pkg_events(lines: Iterable[str]) -> list[PkgEvent]:
    out: list[PkgEvent] = []
    for line in lines:
        match = _PKG_EVENT.search(line)
        if not match:
            continue
        stamp = _TS.match(line)
        when = parse_ts(stamp.group(1)) if stamp else None
        out.append(PkgEvent(when, match.group(1), match.group(2)))
    return out


def parse_downloads(text: str) -> list[DownloadEntry]:
    """Parse `ls -laR` output into file entries (directories included)."""
    out: list[DownloadEntry] = []
    directory = ""
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped.endswith(":") and not stripped.startswith(("total", "d", "-")):
            directory = stripped[:-1]
            continue
        row = _LS_ROW.match(stripped)
        if not row:
            continue
        perms, size, date, time, name = row.groups()
        if name in (".", ".."):
            continue
        when = parse_ts(f"{date} {time}:00")
        assert when is not None, (date, time)
        out.append(DownloadEntry(directory, name, int(size), when,
                                 perms.startswith("d")))
    return out


def parse_manifest(text: str) -> list[tuple[str, int, str]]:
    """manifest.tsv rows -> (name, exit_code, cmd); header skipped."""
    out: list[tuple[str, int, str]] = []
    for line in text.splitlines()[1:]:
        fields = line.split("\t")
        if len(fields) >= 4:
            out.append((fields[0], int(fields[1]), fields[3]))
    return out


# ---------------------------------------------------------------------------
# pure analysis
# ---------------------------------------------------------------------------


def removed_app_candidates(
    usage: Mapping[str, UsageStat], installed: frozenset[str]
) -> list[UsageStat]:
    """Third-party apps with recorded activity that are no longer installed."""
    out = [
        stat
        for pkg, stat in usage.items()
        if stat.last_active is not None
        and pkg not in installed
        and not is_system_package(pkg)
    ]
    return sorted(out, key=lambda s: s.last_active, reverse=True)  # type: ignore[arg-type,return-value]


def suspicious_matches(package: str) -> list[str]:
    return [kw for kw in SUSPICIOUS_KEYWORDS if kw in package]


def name_flags(packages: Iterable[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for pkg in packages:
        hits = suspicious_matches(pkg)
        if hits:
            out[pkg] = hits
    return out


def download_anomalies(entries: Sequence[DownloadEntry]) -> list[tuple[str, str]]:
    """Return (entry-path, reason) pairs for suspicious Download entries."""
    out: list[tuple[str, str]] = []
    for entry in entries:
        path = f"{entry.directory}/{entry.name}"
        if entry.name.startswith((".", "_")):
            out.append((path, "hidden/obscured name"))
        if entry.name.lower().endswith(".apk"):
            out.append((path, f"APK in Download ({entry.size} bytes)"))
        lead = _LEADING_DATE.match(entry.name)
        if lead:
            embedded = f"{lead.group(1)}-{lead.group(2)}-{lead.group(3)}"
            if embedded != entry.mtime.strftime("%Y-%m-%d"):
                out.append((path, f"filename date {embedded} != mtime "
                                  f"{entry.mtime:%Y-%m-%d}"))
    return out


# ---------------------------------------------------------------------------
# rendering + I/O
# ---------------------------------------------------------------------------


def _fmt(dt: datetime | None) -> str:
    return dt.strftime("%Y-%m-%d %H:%M") if dt else "never"


def render_report(capture: str, data: "CaptureData") -> str:
    lines: list[str] = [f"# Forensic report — {capture}", ""]

    failed = [(n, c) for n, c, _ in data.manifest if c != 0]
    lines.append("## Capture integrity")
    lines.append(f"manifest: {len(data.manifest)} commands, {len(failed)} nonzero exits")
    for name, code in failed:
        lines.append(f"  ! {name}: exit {code}")
    lines.append("")

    lines.append("## logcat coverage")
    if not data.coverage:
        lines.append("  (no timestamped logcat lines)")
    for cov in sorted(data.coverage, key=lambda c: c.first):
        lines.append(f"  {cov.buffer:8} {_fmt(cov.first)} -> {_fmt(cov.last)}")
    lines.append("")

    lines.append("## Crashes (FATAL EXCEPTION) by package")
    by_pkg: dict[str, list[datetime | None]] = {}
    for crash in data.crashes:
        by_pkg.setdefault(crash.package, []).append(crash.when)
    for pkg in sorted(by_pkg, key=lambda p: len(by_pkg[p]), reverse=True):
        whens = [w for w in by_pkg[pkg] if w]
        span = f"{_fmt(min(whens))}..{_fmt(max(whens))}" if whens else "?"
        tag = "" if (pkg in data.installed or is_system_package(pkg)) else "  [NOT installed]"
        lines.append(f"  {len(by_pkg[pkg]):3}x {pkg}  ({span}){tag}")
    lines.append("")

    lines.append("## Package install/remove events in logcat")
    if not data.pkg_events:
        lines.append("  none found — logcat buffers do not reach the install window.")
        lines.append("  Use the account-side Play Library for the authoritative list.")
    for ev in data.pkg_events:
        lines.append(f"  {_fmt(ev.when)} {ev.kind}: {ev.package}")
    lines.append("")

    lines.append("## Removed-app candidates (active in usagestats, not installed)")
    for stat in removed_app_candidates(data.usage, data.installed):
        retained = "  [data-retained]" if stat.package in data.removed_data else ""
        fg = "foregrounded" if stat.foregrounded else "background-only"
        lines.append(f"  {_fmt(stat.last_active)}  {stat.package}  "
                     f"({fg}, launches={stat.launch_count}){retained}")
    lines.append("")

    lines.append("## Name-heuristic flags (WEAK signal — confirm with the human)")
    candidates = set(data.installed) | {s.package for s in
                                        removed_app_candidates(data.usage, data.installed)}
    for pkg, hits in sorted(name_flags(candidates).items()):
        state = "installed" if pkg in data.installed else "removed"
        lines.append(f"  [{state:9}] {pkg}  <- {','.join(hits)}")
    lines.append("")

    lines.append("## Third-party holders of sensitive appops")
    for label, holders in data.appops.items():
        third = sorted(h for h in holders if not is_system_package(h))
        shown = ", ".join(third) if third else "(none third-party)"
        lines.append(f"  {label}: {shown}")
    lines.append("")

    lines.append("## /sdcard/Download anomalies")
    anomalies = download_anomalies(data.downloads)
    if not anomalies:
        lines.append("  (none)")
    for path, reason in anomalies:
        lines.append(f"  {path}  <- {reason}")
    lines.append("")

    return "\n".join(lines)


@dataclass(frozen=True, slots=True)
class CaptureData:
    manifest: list[tuple[str, int, str]]
    coverage: list[BufferCoverage]
    crashes: list[Crash]
    pkg_events: list[PkgEvent]
    usage: Mapping[str, UsageStat]
    installed: frozenset[str]
    removed_data: frozenset[str]
    appops: Mapping[str, frozenset[str]]
    downloads: list[DownloadEntry]


def _read(directory: Path, name: str) -> str:
    path = directory / name
    return path.read_text(errors="replace") if path.exists() else ""


def load_capture(directory: Path) -> CaptureData:
    installed = parse_package_list(_read(directory, "packages-3rdparty.txt"))
    removed_all = parse_package_list(_read(directory, "packages-3rdparty-removed.txt"))
    logcat = (_read(directory, "logcat-default.txt").splitlines()
              + _read(directory, "logcat-events.txt").splitlines())
    appops = {
        "SYSTEM_ALERT_WINDOW": parse_appop_holders(_read(directory, "appop-overlay.txt")),
        "READ_SMS": parse_appop_holders(_read(directory, "appop-read-sms.txt")),
        "RECEIVE_SMS": parse_appop_holders(_read(directory, "appop-receive-sms.txt")),
        "REQUEST_INSTALL_PACKAGES": parse_appop_holders(
            _read(directory, "appop-install-unknown.txt")),
    }
    return CaptureData(
        manifest=parse_manifest(_read(directory, "manifest.tsv")),
        coverage=parse_logcat_coverage(logcat),
        crashes=parse_crashes(logcat),
        pkg_events=parse_pkg_events(logcat),
        usage=parse_usagestats(_read(directory, "usagestats.txt")),
        installed=installed,
        removed_data=removed_all - installed,
        appops=appops,
        downloads=parse_downloads(_read(directory, "downloads-listing.txt")),
    )


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <forensics/CAPTURE_DIR>", file=sys.stderr)
        return 2
    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"not a directory: {directory}", file=sys.stderr)
        return 2
    print(render_report(directory.name, load_capture(directory)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
