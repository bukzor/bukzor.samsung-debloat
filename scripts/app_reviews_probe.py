#!/usr/bin/env python3
"""Probe Play user reviews for behavioural reports, one JSONL record per review.

User reports are valid evidence to separate adware from malware *when the signal
is high enough* — and Play gives a built-in weight: ``thumbs_up`` (how many users
found a review helpful). A heavily-upvoted 1-star review that says "it sent text
messages by itself" or "charged my card" is corroborated testimony of covert
capability abuse (the **malware** tell); one that says "unusable, full-screen ads
every tap" with the same weight is the **adware** tell. Same source, different
verdict — so we keep the raw reviews structured and let jq do the discrimination.

The script is deliberately dumb: it fetches the most-relevant reviews (Play's own
helpfulness-aware ranking) and emits one record per review. Thresholding by
``thumbs_up`` and matching behaviour keywords is the ad-hoc part — a jq one-liner:

    scripts/app_reviews_probe.py com.foo.bar \
      | jq -c 'select(.score<=2 and .thumbs_up>=20)
               | select(.content|test("sent text|charged|subscri|stole|password|spy|can.t uninstall";"i"))
               | {package, thumbs_up, score, content}'

``at`` (a datetime) is rendered ISO-8601. Packages with no live listing yield no
lines (app_reputation_probe.py already records their absence).

Network I/O lives in fetch_reviews()/main(); review_record() is pure.
"""

import json
import sys
from collections.abc import Mapping
from datetime import datetime


def review_record(package: str, raw: Mapping[str, object]):
    """Shape one google-play-scraper review dict into a JSONL record."""
    at = raw.get("at")
    return {
        "package": package,
        "review_id": raw.get("reviewId"),
        "score": raw.get("score"),
        "thumbs_up": raw.get("thumbsUpCount"),
        "date": at.isoformat() if isinstance(at, datetime) else at,
        "app_version": raw.get("reviewCreatedVersion"),
        "content": raw.get("content"),
    }


def fetch_reviews(package: str, count: int = 120):
    """Most-relevant reviews for a package; [] when Play has no live listing."""
    from google_play_scraper import Sort, reviews
    from google_play_scraper.exceptions import NotFoundError

    try:
        result, _token = reviews(
            package, lang="en", country="us", sort=Sort.MOST_RELEVANT, count=count
        )
    except NotFoundError:
        return []
    return result


def main() -> None:
    packages = sys.argv[1:] or [line.strip() for line in sys.stdin if line.strip()]
    for package in packages:
        for raw in fetch_reviews(package):
            print(json.dumps(review_record(package, raw)), flush=True)


if __name__ == "__main__":
    main()
