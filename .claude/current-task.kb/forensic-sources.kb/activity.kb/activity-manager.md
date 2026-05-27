---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# activity-manager — live and recently-run components

`dumpsys activity` sections expose running/recent processes and services,
registered broadcast receivers (e.g. `BOOT_COMPLETED` auto-start), and content
providers — by package.

Capture:

    adb shell dumpsys activity processes  > am-processes.txt
    adb shell dumpsys activity services   > am-services.txt
    adb shell dumpsys activity broadcasts > am-broadcasts.txt

Boot/broadcast receivers feed the `persistence-mechanisms` analysis.
