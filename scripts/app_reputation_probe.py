#!/usr/bin/env python3
"""Probe Google Play for structured reputation signals on a package, as JSONL.

Aimed at triaging the ``unknown/`` bucket in android-apps.kb *without scraping
HTML*: the ``google-play-scraper`` library hits Play's internal data endpoints
and returns typed dicts. For each package id this emits one JSON object with the
identity + scope signals that actually move an ``unknown`` verdict —

- developer identity (name, id, email, website) — a real, traceable developer
  leans ``legitimate``; a throwaway one leans the other way;
- install scale + rating posture (``min_installs``, ``score``, ``ratings``);
- ad posture (``ad_supported``, ``contains_ads``) — the ``adware`` tell;
- the full permission list — a "weather"/"cleaner" app demanding SMS, contacts,
  or accessibility is the ``malware`` tell (still needs device-side proof per
  android-apps.kb, but it flags the candidate);

plus ``found: false`` when Play has no live listing — a delisted / never-existed
signal that the HTTP-200 soft-404 page Play serves would otherwise hide.

    scripts/app_reputation_probe.py com.foo.bar com.baz.qux \
      | jq -s 'sort_by(.min_installs)'

    android_apps_kb.py list KB | jq -r 'select(.verdict=="unknown").package' \
      | scripts/app_reputation_probe.py | jq .

Network I/O lives in main()/fetch_play(); play_record() and
flatten_permissions() are pure (shape a raw dict -> JSONL record).
"""

import json
import sys
from collections.abc import Mapping, Sequence

# google-play-scraper camelCase key -> our snake_case JSONL key. Selecting an
# explicit subset keeps the record small and stable; the lib returns ~40 keys.
_FIELDS = {
    "title": "title",
    "developer": "developer",
    "developerId": "developer_id",
    "developerEmail": "developer_email",
    "developerWebsite": "developer_website",
    "genre": "genre",
    "installs": "installs",
    "minInstalls": "min_installs",
    "score": "score",
    "ratings": "ratings",
    "contentRating": "content_rating",
    "released": "released",
    "lastUpdatedOn": "last_updated_on",
    "adSupported": "ad_supported",
    "containsAds": "contains_ads",
}


def flatten_permissions(perms: Mapping[str, Sequence[str]] | None):
    """``{group: [perm, ...]}`` -> sorted unique flat list (None passes through)."""
    if perms is None:
        return None
    return sorted({perm for group in perms.values() for perm in group})


def play_record(package: str, app_data: Mapping[str, object] | None, perms):
    """Shape google-play-scraper output into a JSONL reputation record.

    ``app_data`` is the dict from ``app()``, or None when Play has no live
    listing (the library raised NotFoundError).
    """
    if app_data is None:
        return {"package": package, "found": False}
    record: dict[str, object] = {"package": package, "found": True}
    for src, dst in _FIELDS.items():
        record[dst] = app_data.get(src)
    record["permissions"] = flatten_permissions(perms)
    return record


def fetch_play(package: str):
    """Return ``(app_data, perms)``; app_data is None when Play has no listing."""
    from google_play_scraper import app, permissions
    from google_play_scraper.exceptions import NotFoundError

    try:
        app_data = app(package, lang="en", country="us")
    except NotFoundError:
        return None, None
    return app_data, permissions(package, lang="en", country="us")


def main() -> None:
    packages = sys.argv[1:] or [
        line.strip() for line in sys.stdin if line.strip()
    ]
    for package in packages:
        app_data, perms = fetch_play(package)
        print(json.dumps(play_record(package, app_data, perms)), flush=True)


if __name__ == "__main__":
    main()
