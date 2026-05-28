# Two My-Activity captures — use both; they are complementary

We hold **two** captures of her Google "My Activity", with different strengths.
Use both; neither alone is sufficient.

## 1. Live scrape — `forensics/myactivity.google.com.json`

JSONL of array-indexed records (one per event). Known indices:

- `[4]` event time, **microseconds** since epoch
- `[7]` product `[name, _, icon]`
- `[9]` item `[title, _, action, url]` (url has `details?id=<pkg>`)
- `[17]` / `[18]` secondary app(s) `[title, url, img]`
- `[19]` **device**, e.g. `[['samsung SM-S926U']]`  ← unique to this capture

URLs carry `authuser=6` (her account is browser index 6 — "one among several").
Coverage: 2026-04-29 → 05-26, ~1605 events, **1587 on SM-S926U**, 13 on the
Hisense TV. **Unique value: per-event device attribution** (proves an event is
on the phone, not the TV) and it is the most-recent/live snapshot. Tools over
this positional-array JSONL: `scripts/myactivity_scrape.py` (Python decoder →
structured events, **incl. the device tag**); or the jq trio —
`scripts/myactivity.google.com.jq` (human-readable TSV), `.records.jq` (tidy
JSONL incl. device), `.gap-analysis.jq` (coverage span + silent-window gaps).

## 2. Takeout export — `forensics/takeout-20260527/Takeout/My Activity/*/`

Per-product HTML. Deeper history (Play Store back to 2026-02-26 vs the scrape's
04-29) and package id in each entry's `details?id=` href, but **no per-event
device**. Parsed by `scripts/myactivity_takeout.py`.

## Why both

Takeout for **depth/coverage and package resolution**; the scrape for **device
attribution and corroboration**. They agree exactly on the 2026-05-18 window
(both: only the 6-event clean batch before 07:09:27), which is why the
silent-window and on-phone findings are **dual-source confirmed**. Lesson: when
a second capture of the same source exists, reconcile it — don't pivot to the
richer one and abandon the other.
