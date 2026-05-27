---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# netstats — per-app data-volume history

`dumpsys netstats --uid`: historical mobile/Wi-Fi byte counts per uid/package —
an ad/exfiltration app often shows outsized background traffic.

Capture: `adb shell dumpsys netstats --uid > netstats.txt`

Names by uid; recycled uids of removed apps may need cross-referencing.
