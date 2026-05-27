---
capture-status: captured
captured-as: [logcat-default.txt, logcat-events.txt]
needs-device: true
last-updated: "2026-05-27"
---

# logcat-buffers — main / system / crash / events

`adb logcat -d -v year` across buffers. The crash buffer holds deep history;
main/system/events fill fast and only cover the recent past.

Capture:

    adb logcat -d -v year            > logcat-default.txt
    adb logcat -d -b events -v year  > logcat-events.txt

This capture: crash buffer reaches 2026-05-21; main/system/events only ~1h. No
package install/remove events present. Volatile — recapture after any reboot.
