---
capture-status: captured
captured-as: [appops-full.txt, appop-overlay.txt, appop-install-unknown.txt, appop-read-sms.txt, appop-receive-sms.txt, appop-access-notifications.txt, appop-get-usage-stats.txt]
needs-device: false
last-updated: "2026-05-27"
---

# appops — op grants and last-access timestamps

`dumpsys appops` (full) plus per-op holder queries. Covers the abuse-relevant
ops: `SYSTEM_ALERT_WINDOW` (overlays), `REQUEST_INSTALL_PACKAGES` (sideload
door), `READ_SMS`/`RECEIVE_SMS`, `GET_USAGE_STATS`, `ACCESS_NOTIFICATIONS`.

Capture:

    adb shell dumpsys appops > appops-full.txt
    adb shell appops query-op SYSTEM_ALERT_WINDOW allow > appop-overlay.txt
    adb shell appops query-op REQUEST_INSTALL_PACKAGES allow > appop-install-unknown.txt

`appops-full.txt` also records per-package last-access times (never fully mined).
