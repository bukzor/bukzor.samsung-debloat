import json
from datetime import datetime, timezone

from myactivity_scrape import (
    Event,
    find_action,
    parse_record,
    parse_scrape,
)

# 1700000000 s since epoch == 2023-11-14T22:13:20+00:00
TS = 1_700_000_000_000_000


def _record(
    action,
    *,
    device: str | None = "samsung SM-S926U",
    product: str | None = "Google Play Store",
    ts: int = TS,
) -> list:
    """Build a positional My-Activity record matching the observed layout."""
    record: list = [None] * 20
    record[3] = [15]
    record[4] = ts
    record[6] = [product, None, "//icon.png"]
    record[8] = action
    record[19] = [[device]] if device is not None else None
    return record


VISITED = _record(
    [
        "Difference: Spot & Find",
        None,
        "Visited",
        "https://play.google.com/store/apps/details?id=com.find.spot&authuser=6",
    ]
)
SEARCH = _record(
    ["602 club", None, "Searched for", "https://www.google.com/search?q=602+club"],
    device=None,
)
NO_ACTION = _record(None)


class DescribeParseRecord:
    def it_reads_action_title_and_package(self):
        ev = parse_record(VISITED)
        assert ev is not None
        assert ev.action == "Visited"
        assert ev.title == "Difference: Spot & Find"
        assert ev.package == "com.find.spot"

    def it_reads_the_device_tag(self):
        ev = parse_record(VISITED)
        assert ev is not None and ev.device == "samsung SM-S926U"

    def it_reads_the_product(self):
        ev = parse_record(VISITED)
        assert ev is not None and ev.product == "Google Play Store"

    def it_parses_the_microsecond_timestamp_as_utc(self):
        ev = parse_record(VISITED)
        assert ev is not None
        assert ev.when == datetime(2023, 11, 14, 22, 13, 20, tzinfo=timezone.utc)
        assert ev.when.isoformat() == "2023-11-14T22:13:20+00:00"

    def it_returns_none_without_an_action_block(self):
        assert parse_record(NO_ACTION) is None

    class WhenTheEventIsASearch:
        def it_has_no_package(self):
            ev = parse_record(SEARCH)
            assert ev is not None
            assert ev.action == "Searched for"
            assert ev.package is None

        def it_has_no_device_when_the_tag_is_absent(self):
            ev = parse_record(SEARCH)
            assert ev is not None and ev.device is None


class DescribeFindAction:
    def it_ignores_the_product_block_which_lacks_an_action_verb(self):
        # the product block [name, None, icon] must not be read as an action
        assert find_action(NO_ACTION) is None


class DescribeParseScrape:
    def it_yields_one_event_per_nonblank_actionable_line(self):
        text = "\n".join(
            [json.dumps(VISITED), "", json.dumps(SEARCH), json.dumps(NO_ACTION)]
        )
        events = parse_scrape(text)
        assert [e.action for e in events] == ["Visited", "Searched for"]

    def it_returns_events(self):
        (text,) = (json.dumps(VISITED),)
        assert all(isinstance(e, Event) for e in parse_scrape(text))
