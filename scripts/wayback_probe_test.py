"""Tests for wayback_probe. Fixtures synthetic — no network."""

from wayback_probe import cdx_url, wayback_record

ROWS = [
    ["timestamp", "statuscode"],
    ["20251129182908", "200"],
    ["20260217012543", "200"],
]


class DescribeCdxUrl:
    def it_percent_encodes_the_play_query_so_cdx_treats_it_as_one_url(self):
        url = cdx_url("com.foo.bar")
        assert "play.google.com/store/apps/details%3Fid%3Dcom.foo.bar" in url

    def it_requests_json_with_collapsed_daily_captures(self):
        url = cdx_url("com.foo.bar")
        assert "output=json" in url
        assert "collapse=timestamp:8" in url


class DescribeWaybackRecord:
    def it_summarizes_first_last_and_count_of_captures(self):
        assert wayback_record("com.foo.bar", ROWS) == {
            "package": "com.foo.bar",
            "archived": True,
            "snapshots": 2,
            "first_snapshot": "20251129182908",
            "last_snapshot": "20260217012543",
            "last_status": "200",
        }

    def it_reports_an_empty_response_as_not_archived(self):
        assert wayback_record("com.gone.app", []) == {
            "package": "com.gone.app",
            "archived": False,
            "snapshots": 0,
            "first_snapshot": None,
            "last_snapshot": None,
            "last_status": None,
        }

    def it_treats_a_header_only_response_as_not_archived(self):
        assert wayback_record("x", [["timestamp", "statuscode"]])["archived"] is False
