from datetime import datetime

from myactivity_takeout import (
    Event,
    load_installed,
    parse_events,
    parse_timestamp,
    summarize,
)


def _cell(body: str) -> str:
    return (
        '<div class="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp">'
        '<div class="mdl-grid">'
        '<div class="header-cell mdl-cell mdl-cell--12-col">'
        '<p class="mdl-typography--title">x<br></p></div>'
        '<div class="content-cell mdl-cell mdl-cell--6-col '
        f'mdl-typography--body-1">{body}</div>'
        '<div class="content-cell mdl-cell mdl-cell--6-col '
        'mdl-typography--body-1 mdl-typography--text-right"></div>'
        '<div class="content-cell mdl-cell mdl-cell--12-col '
        'mdl-typography--caption"><b>Products:</b><br>Google Play Store</div>'
        "</div></div>"
    )


USED = _cell(
    "Used\xa0<a href=\"https://play.google.com/store/apps/details"
    '?id=com.forecasts.noaa.live.weather">Live Weather: Daily Forecast</a>'
    "<br>May 19, 2026, 10:36:40 AM CDT<br>"
)
VISITED = _cell(
    'Visited\xa0<a href="https://play.google.com/store/apps/details'
    '?id=com.forecasts.noaa.live.weather">Live Weather: Daily Forecast</a>'
    "<br>May 18, 2026, 9:00:00 AM CDT<br>"
)
SEARCHED = _cell(
    'Searched for\xa0<a href="https://www.google.com/search?q=cleaner">'
    "phone cleaner</a><br>May 17, 2026, 8:00:00 AM CDT<br>"
)
HTML = "<html><body>" + USED + VISITED + SEARCHED + "</body></html>"


class DescribeParseEvents:
    def it_extracts_one_event_per_cell(self):
        assert len(parse_events(HTML)) == 3

    def it_reads_action_and_package_and_title(self):
        used = parse_events(HTML)[0]
        assert used.action == "Used"
        assert used.package == "com.forecasts.noaa.live.weather"
        assert used.title == "Live Weather: Daily Forecast"

    def it_normalizes_narrow_and_nbsp_spaces_in_timestamp(self):
        used = parse_events(HTML)[0]
        assert used.when == datetime(2026, 5, 19, 10, 36, 40)
        assert used.tz == "CDT"

    def it_leaves_package_none_for_searches(self):
        searched = parse_events(HTML)[2]
        assert searched.action == "Searched for"
        assert searched.package is None
        assert searched.title == "phone cleaner"


class DescribeParseTimestamp:
    def it_parses_12h_clock_and_tz(self):
        assert parse_timestamp("May 19, 2026, 10:36:40 PM CDT") == (
            datetime(2026, 5, 19, 22, 36, 40),
            "CDT",
        )

    class WhenMonthIsAbbreviatedSept:
        def it_normalizes_to_strptime_form(self):
            when, _ = parse_timestamp("Sept 3, 2025, 1:02:03 AM CST")
            assert when == datetime(2025, 9, 3, 1, 2, 3)


class DescribeSummarize:
    def it_groups_by_package_and_counts_actions(self):
        (summary,) = summarize(parse_events(HTML))
        assert summary.package == "com.forecasts.noaa.live.weather"
        assert (summary.used, summary.visited) == (1, 1)
        assert summary.first == datetime(2026, 5, 18, 9, 0, 0)
        assert summary.last == datetime(2026, 5, 19, 10, 36, 40)

    def it_orders_by_last_seen_descending(self):
        events = (
            Event("Used", "com.old", "Old", datetime(2026, 1, 1), "CST"),
            Event("Used", "com.new", "New", datetime(2026, 5, 1), "CDT"),
        )
        assert [s.package for s in summarize(events)] == ["com.new", "com.old"]


class DescribeLoadInstalled:
    def it_strips_the_package_prefix(self):
        assert load_installed("package:com.a\npackage:com.b\n") == frozenset(
            {"com.a", "com.b"}
        )
