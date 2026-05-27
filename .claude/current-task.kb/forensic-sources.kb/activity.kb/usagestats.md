---
capture-status: captured
captured-as: [usagestats.txt]
needs-device: false
last-updated: "2026-05-27"
---

# usagestats — app usage events and per-package buckets

`dumpsys usagestats`: a 24h foreground/usage event log plus daily/weekly/monthly/
yearly per-package buckets (`lastTimeUsed`, `lastTimeComponentUsed`,
`appLaunchCount`).

Capture: `adb shell dumpsys usagestats > usagestats.txt`

Note: it has **no** package install/remove events. The 24h event log is
capture-day noise (the 05-26 trap); the buckets' *earliest* activity is the
real signal.
