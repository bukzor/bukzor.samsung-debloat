"""Tests for app_reviews_probe. Fixtures synthetic — no network, no real PII."""

from datetime import datetime

from app_reviews_probe import review_record

REVIEW = {
    "reviewId": "abc123",
    "userName": "A User",
    "content": "it sent text messages by itself",
    "score": 1,
    "thumbsUpCount": 341,
    "reviewCreatedVersion": "2.4.1",
    "at": datetime(2026, 2, 1, 12, 0, 0),
    "replyContent": None,
}


class DescribeReviewRecord:
    def it_selects_the_report_bearing_fields_and_renders_date_iso(self):
        assert review_record("com.foo.bar", REVIEW) == {
            "package": "com.foo.bar",
            "review_id": "abc123",
            "score": 1,
            "thumbs_up": 341,
            "date": "2026-02-01T12:00:00",
            "app_version": "2.4.1",
            "content": "it sent text messages by itself",
        }

    def it_passes_a_nondatetime_date_through_unchanged(self):
        rec = review_record("x", {**REVIEW, "at": None})
        assert rec["date"] is None

    def it_tolerates_missing_keys(self):
        rec = review_record("x", {})
        assert rec == {
            "package": "x",
            "review_id": None,
            "score": None,
            "thumbs_up": None,
            "date": None,
            "app_version": None,
            "content": None,
        }
