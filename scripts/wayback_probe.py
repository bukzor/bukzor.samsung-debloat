#!/usr/bin/env python3
"""Probe the Wayback Machine for a package's Play-listing capture history, JSONL.

Complements scripts/app_reputation_probe.py. That probe's ``found: false`` means
"no *live* Play listing now"; it cannot say whether the app was *ever* on Play.
The Internet Archive CDX API — a real JSON API, no token, no HTML — answers that
from the capture record of ``play.google.com/store/apps/details?id=<pkg>``:

- archived + Play probe ``found: false``  => was on Play, since **delisted**
  (high signal — Play removed it);
- not archived + ``found: false``         => never publicly on Play (sideloaded /
  off-store — also high signal, different concern).

Join to the Play probe by ``package`` in jq. Timestamps are raw CDX 14-digit
``YYYYMMDDhhmmss`` (UTC); format in jq if you want them pretty.

    scripts/wayback_probe.py com.foo.bar | jq .
    jq -r 'select(.found==false).package' trash/unknown-probe.jsonl \
      | scripts/wayback_probe.py | jq -c '{package, archived, first_snapshot}'

Network I/O lives in fetch_cdx()/main(); cdx_url() and wayback_record() are pure.
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Sequence

_CDX = "http://web.archive.org/cdx/search/cdx"


def cdx_url(package: str) -> str:
    """Build the CDX query URL for a package's Play listing.

    The Play details URL is encoded into the ``url`` param (``?``/``=`` must be
    percent-encoded or CDX would parse them as its own query params). Captures
    are collapsed to one-per-day to bound volume on popular apps.
    """
    target = urllib.parse.quote(
        f"play.google.com/store/apps/details?id={package}", safe="/."
    )
    return (
        f"{_CDX}?url={target}"
        "&output=json&fl=timestamp,statuscode&collapse=timestamp:8"
    )


def wayback_record(package: str, rows: Sequence[Sequence[str]]):
    """Shape a CDX response (header row + capture rows, or empty) into a record."""
    captures = list(rows[1:]) if rows else []
    if not captures:
        return {
            "package": package,
            "archived": False,
            "snapshots": 0,
            "first_snapshot": None,
            "last_snapshot": None,
            "last_status": None,
        }
    return {
        "package": package,
        "archived": True,
        "snapshots": len(captures),
        "first_snapshot": captures[0][0],
        "last_snapshot": captures[-1][0],
        "last_status": captures[-1][1],
    }


def fetch_cdx(package: str, timeout: float = 30.0):
    """GET the CDX index for a package; [] when there are no captures."""
    with urllib.request.urlopen(cdx_url(package), timeout=timeout) as resp:
        body = resp.read().decode("utf-8").strip()
    return json.loads(body) if body else []


def main() -> None:
    packages = sys.argv[1:] or [line.strip() for line in sys.stdin if line.strip()]
    for package in packages:
        try:
            rows = fetch_cdx(package)
        except (urllib.error.URLError, TimeoutError) as err:
            print(
                json.dumps({"package": package, "archived": None, "error": str(err)}),
                flush=True,
            )
            continue
        print(json.dumps(wayback_record(package, rows)), flush=True)


if __name__ == "__main__":
    main()
