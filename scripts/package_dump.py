#!/usr/bin/env python3
"""Extract per-package install metadata from a `dumpsys package` dump as JSONL.

Input is a capture's ``package-dump-full.txt`` (the full ``adb shell dumpsys
package`` output). For each ``Package [...]`` block this emits one JSON object
with the install provenance a forensic timeline needs: who installed it, when it
first landed for the primary user, when the APK was last updated, and whether
it's enabled.

JSONL out, one package per line — join/filter/sort with jq:

    scripts/package_dump.py forensics/<capture>/package-dump-full.txt \
      | jq -s 'sort_by(.first_install_time)'

Fields are ``null`` when the dump omits them (common for preinstalled system
packages, which carry no installer and a stub install time).
"""

import json
import re
import sys
from collections.abc import Iterator

# A package block starts at column 2: "  Package [<id>] (<hash>):".
_BLOCK = re.compile(r"^  Package \[([\w.]+)\] \([0-9a-f]+\):$", re.MULTILINE)
_VERSION_NAME = re.compile(r"^    versionName=(.+)$", re.MULTILINE)
_TIMESTAMP = re.compile(r"^    timeStamp=(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)", re.MULTILINE)
_LAST_UPDATE = re.compile(r"^    lastUpdateTime=(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)", re.MULTILINE)
_INSTALLER = re.compile(r"^    installerPackageName=(.+)$", re.MULTILINE)
_CODE_PATH = re.compile(r"^    codePath=(\S+)$", re.MULTILINE)
# The primary-user sub-block and the install fields nested under it.
_USER0 = re.compile(r"^    User 0:.*?(?=^    User \d|\Z)", re.MULTILINE | re.DOTALL)
_INSTALLED = re.compile(r"\binstalled=(\w+)")
_ENABLED = re.compile(r"\benabled=(\d+)")
_FIRST_INSTALL = re.compile(r"firstInstallTime=(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)")

# dumpsys COMPONENT_ENABLED_STATE integer -> meaning.
_ENABLED_STATE = {
    "0": "default",
    "1": "enabled",
    "2": "disabled",
    "3": "disabled-user",
    "4": "disabled-until-used",
}


def _maybe(match: re.Match[str] | None) -> str | None:
    if match is None:
        return None
    value = match.group(1).strip()
    return None if value == "null" else value


def split_blocks(text: str) -> Iterator[tuple[str, str]]:
    """Yield (package, block-text) for each Package block, first occurrence only.

    A package can recur (e.g. a "Hidden system packages:" section repeats it);
    the first occurrence is the live primary entry.
    """
    starts = list(_BLOCK.finditer(text))
    seen: set[str] = set()
    for i, match in enumerate(starts):
        package = match.group(1)
        if package in seen:
            continue
        seen.add(package)
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        yield package, text[match.start() : end]


def parse_user0(block: str) -> dict[str, object]:
    user0 = _USER0.search(block)
    if user0 is None:
        return {"installed": None, "enabled": None, "first_install_time": None}
    span = user0.group(0)
    installed = _INSTALLED.search(span)
    enabled = _ENABLED.search(span)
    first_install = _FIRST_INSTALL.search(span)
    return {
        "installed": installed.group(1) == "true" if installed else None,
        "enabled": _ENABLED_STATE.get(enabled.group(1)) if enabled else None,
        "first_install_time": first_install.group(1) if first_install else None,
    }


def package_record(package: str, block: str) -> dict[str, object]:
    return {
        "package": package,
        "version_name": _maybe(_VERSION_NAME.search(block)),
        "installer": _maybe(_INSTALLER.search(block)),
        "timestamp": _maybe(_TIMESTAMP.search(block)),
        "last_update_time": _maybe(_LAST_UPDATE.search(block)),
        "code_path": _maybe(_CODE_PATH.search(block)),
        **parse_user0(block),
    }


def records(text: str) -> Iterator[dict[str, object]]:
    for package, block in split_blocks(text):
        yield package_record(package, block)


def main() -> None:
    (path,) = sys.argv[1:]
    text = open(path, encoding="utf-8").read()
    for record in records(text):
        print(json.dumps(record))


if __name__ == "__main__":
    main()
