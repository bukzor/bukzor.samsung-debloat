---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# scheduled-work — jobs and alarms (keep-alive)

`dumpsys jobscheduler` and `dumpsys alarm` list scheduled jobs and repeating
alarms by package — the mechanisms adware uses to stay resident and re-launch.

Capture:

    adb shell dumpsys jobscheduler > jobscheduler.txt
    adb shell dumpsys alarm        > alarms.txt

Feeds the `persistence-mechanisms` analysis.
