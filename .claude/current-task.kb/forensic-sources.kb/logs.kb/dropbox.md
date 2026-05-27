---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# dropbox — crash / ANR / wtf history

DropBoxManager persists tagged system events (`data_app_crash`, `data_app_anr`,
`system_app_crash`, …) to `/data/system/dropbox`, often retaining days-to-weeks —
potentially deeper than logcat's crash buffer (which here only reaches 05-21).

Capture: `adb shell dumpsys dropbox --print > dropbox.txt`

Each entry carries a timestamp and the offending package, and survives that
app's uninstall.
