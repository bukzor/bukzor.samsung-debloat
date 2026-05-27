---
capture-status: partial
captured-as: [accessibility-services.txt, accessibility-enabled.txt]
needs-device: false
last-updated: "2026-05-27"
---

# accessibility — enabled accessibility services

The accessibility-service grant is the "Settings closes itself" / screen-watching
abuse vector. Read the secure settings and the dump:

    adb shell settings get secure enabled_accessibility_services > accessibility-services.txt
    adb shell settings get secure accessibility_enabled          > accessibility-enabled.txt
    adb shell dumpsys accessibility                              > accessibility-dump.txt

This capture: services = `null`, enabled = `0` (none active — the abuser is gone).
