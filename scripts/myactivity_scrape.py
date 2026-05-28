#!/usr/bin/env python3
"""Parse the live ``myactivity.google.com`` JSON scrape into structured events.

Unlike the Takeout HTML export (see ``myactivity_takeout.py``), the live scrape
is line-delimited JSON where each line is a *positional* array. Critically it
carries a per-event **device tag** (e.g. ``samsung SM-S926U``) that the Takeout
HTML lacks — letting us attribute each event to one of the account's devices,
which matters because My Activity is account-wide (phone + TV + Chromebook…).

Observed positional layout (indices stable across the captured scrape):

* ``[4]``  — microsecond epoch timestamp.
* ``[6]``  — product block ``[<product name>, null, <icon url>]``.
* ``[19]`` — device block ``[[<device display name>]]`` (absent for some
  searches).
* one top-level sub-array is the action ``[<title>, null, <action>, <url>]``
  where ``<action>`` is ``Visited`` / ``Used`` / ``Searched for``. Its index
  varies per record, so it is found structurally, not by position.

Usage:
    scripts/myactivity_scrape.py PATH.json     # JSONL events on stdout
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone

type Json = str | int | float | bool | None | list["Json"] | dict[str, "Json"]

ACTIONS = ("Visited", "Used", "Searched for")
_PACKAGE = re.compile(r"details\?id=([\w.]+)")
_TS_INDEX = 4
_PRODUCT_INDEX = 6
_DEVICE_INDEX = 19


@dataclass(frozen=True)
class Event:
    when: datetime
    device: str | None
    product: str | None
    action: str
    title: str
    url: str | None
    package: str | None


def _strings(value: Json) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def first_string(value: Json) -> str | None:
    return next(iter(_strings(value)), None)


def _at(record: list[Json], index: int) -> Json:
    return record[index] if index < len(record) else None


def read_timestamp(record: list[Json]) -> datetime:
    micros = record[_TS_INDEX]
    assert isinstance(micros, int) and micros > 10**15, micros
    return datetime.fromtimestamp(micros / 1e6, timezone.utc)


def find_action(record: list[Json]) -> list[Json] | None:
    for value in record:
        if (
            isinstance(value, list)
            and len(value) >= 4
            and value[2] in ACTIONS
            and isinstance(value[0], str)
        ):
            return value
    return None


def parse_record(record: Json) -> Event | None:
    assert isinstance(record, list), record
    action = find_action(record)
    if action is None:
        return None
    title, verb, url = action[0], action[2], action[3]
    assert isinstance(title, str), title
    assert isinstance(verb, str), verb
    package = _PACKAGE.search(url) if isinstance(url, str) else None
    return Event(
        when=read_timestamp(record),
        device=first_string(_at(record, _DEVICE_INDEX)),
        product=first_string(_at(record, _PRODUCT_INDEX)),
        action=verb,
        title=title,
        url=url if isinstance(url, str) else None,
        package=package.group(1) if package else None,
    )


def parse_scrape(text: str) -> tuple[Event, ...]:
    events: list[Event] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        event = parse_record(json.loads(stripped))
        if event is not None:
            events.append(event)
    return tuple(events)


def event_dict(event: Event) -> Mapping[str, object]:
    return {
        "when": event.when.isoformat(),
        "device": event.device,
        "product": event.product,
        "action": event.action,
        "title": event.title,
        "package": event.package,
        "url": event.url,
    }


def main() -> None:
    (path,) = sys.argv[1:]
    for event in parse_scrape(open(path, encoding="utf-8").read()):
        print(json.dumps(event_dict(event)))


if __name__ == "__main__":
    main()
