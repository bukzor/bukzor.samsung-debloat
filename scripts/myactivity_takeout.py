#!/usr/bin/env python3
"""Parse a Google Takeout "My Activity" HTML export into structured events.

Takeout records Play Store activity as ``Used`` / ``Visited`` / ``Searched for``
entries. Each app entry carries the package id in a ``play.google.com`` store
URL (``details?id=<package>``), so this recovers a *package-resolved* usage and
store-visit timeline — including apps that have since been uninstalled and are
no longer visible in ``dumpsys package`` or Takeout's ``Installs.json``.

Usage:
    scripts/myactivity_takeout.py PATH/MyActivity.html [--installed PKGLIST]
    scripts/myactivity_takeout.py PATH/MyActivity.html --json   # JSONL events

``--installed`` takes a file of ``package:<id>`` lines (``adb shell pm list
packages`` / ``packages-3rdparty.txt``); the summary then marks which packages
are still installed, so the rest are the removed-app suspect pool.
"""

from __future__ import annotations

import html as htmllib
import json
import re
import sys
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime

_BODY = re.compile(
    r'content-cell[^"]*mdl-typography--body-1">(.*?)</div>', re.S
)
_LINK = re.compile(r"<a [^>]*>(.*?)</a>", re.S)
_PACKAGE = re.compile(r"details\?id=([\w.]+)")
_TAGS = re.compile(r"<[^>]+>")
_TIMESTAMP = re.compile(
    r"[A-Z][a-z]{2,3} \d{1,2}, \d{4}, \d{1,2}:\d{2}:\d{2} [AP]M [A-Z]{2,4}"
)


@dataclass(frozen=True)
class Event:
    action: str
    package: str | None
    title: str
    when: datetime
    tz: str


@dataclass(frozen=True)
class PackageSummary:
    package: str
    title: str
    used: int
    visited: int
    other: int
    first: datetime
    last: datetime


def _text(fragment: str) -> str:
    return htmllib.unescape(_TAGS.sub("", fragment)).replace("\xa0", " ").strip()


def parse_timestamp(stamp: str) -> tuple[datetime, str]:
    body, tz = stamp.rsplit(" ", 1)
    body = re.sub(r"^Sept\b", "Sep", body)
    return datetime.strptime(body, "%b %d, %Y, %I:%M:%S %p"), tz


def parse_cell(chunk: str) -> Event | None:
    body_match = _BODY.search(chunk)
    if not body_match:
        return None
    body = body_match.group(1).replace("\xa0", " ").replace(" ", " ")
    time_match = _TIMESTAMP.search(body)
    if not time_match:
        return None
    when, tz = parse_timestamp(time_match.group(0))
    action = _text(body.split("<a", 1)[0])
    link = _LINK.search(body)
    title = _text(link.group(1)) if link else ""
    package = _PACKAGE.search(chunk)
    return Event(action, package.group(1) if package else None, title, when, tz)


def parse_events(html: str) -> tuple[Event, ...]:
    chunks = html.split('<div class="outer-cell')
    return tuple(ev for chunk in chunks[1:] if (ev := parse_cell(chunk)))


def summarize(events: Iterable[Event]) -> tuple[PackageSummary, ...]:
    by_package: dict[str, list[Event]] = defaultdict(list)
    for ev in events:
        if ev.package is not None:
            by_package[ev.package].append(ev)
    summaries = [
        _summarize_package(package, evs) for package, evs in by_package.items()
    ]
    return tuple(sorted(summaries, key=lambda s: s.last, reverse=True))


def _summarize_package(package: str, evs: Sequence[Event]) -> PackageSummary:
    title = next((e.title for e in evs if e.title), "")
    used = sum(1 for e in evs if e.action == "Used")
    visited = sum(1 for e in evs if e.action == "Visited")
    return PackageSummary(
        package=package,
        title=title,
        used=used,
        visited=visited,
        other=len(evs) - used - visited,
        first=min(e.when for e in evs),
        last=max(e.when for e in evs),
    )


def load_installed(text: str) -> frozenset[str]:
    return frozenset(
        line.removeprefix("package:").strip()
        for line in text.splitlines()
        if line.strip()
    )


def render_summary(
    summaries: Iterable[PackageSummary], installed: frozenset[str]
) -> str:
    header = "last\tfirst\tused\tvisited\tinst\tpackage\ttitle"
    rows = [
        "\t".join(
            (
                s.last.strftime("%Y-%m-%d"),
                s.first.strftime("%Y-%m-%d"),
                str(s.used),
                str(s.visited),
                "Y" if s.package in installed else "-",
                s.package,
                s.title,
            )
        )
        for s in summaries
    ]
    return "\n".join([header, *rows])


def render_searches(events: Iterable[Event]) -> str:
    rows = [
        f"{e.when:%Y-%m-%d %H:%M}\t{e.title}"
        for e in events
        if e.action.startswith("Searched")
    ]
    return "\n".join(["# searches", *rows]) if rows else "# searches: none"


def event_dict(ev: Event) -> Mapping[str, object]:
    return {
        "when": ev.when.isoformat(),
        "tz": ev.tz,
        "action": ev.action,
        "package": ev.package,
        "title": ev.title,
    }


def main() -> None:
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [a for a in args if a != "--json"]
    installed: frozenset[str] = frozenset()
    if "--installed" in args:
        i = args.index("--installed")
        installed = load_installed(open(args[i + 1], encoding="utf-8").read())
        del args[i : i + 2]
    (path,) = args
    events = parse_events(open(path, encoding="utf-8").read())
    if as_json:
        for ev in events:
            print(json.dumps(event_dict(ev)))
        return
    print(render_summary(summarize(events), installed))
    print()
    print(render_searches(events))


if __name__ == "__main__":
    main()
