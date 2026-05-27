---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# batterystats — timestamped background activity by package

`dumpsys batterystats` history: process starts, wakelocks, alarms, and
foreground-service events, attributed by uid/package with timestamps.

Capture:

    adb shell dumpsys batterystats --history  > batterystats-history.txt
    adb shell dumpsys batterystats --checkin  > batterystats-checkin.txt

An overlay/ad app must run to draw, so its activity shows here — but history
depth is bounded by charge cycles (hours to a few days), so it may not reach
05-18.
