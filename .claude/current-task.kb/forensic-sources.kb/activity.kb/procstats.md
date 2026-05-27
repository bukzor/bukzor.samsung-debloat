---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# procstats — which processes ran, and for how long

`dumpsys procstats` aggregates process run-time over a multi-day window — useful
for spotting a persistent background junk process even if it's idle now.

Capture: `adb shell dumpsys procstats --hours 72 > procstats.txt`

Names processes by package; depth is typically ~3 days of rolling stats.
