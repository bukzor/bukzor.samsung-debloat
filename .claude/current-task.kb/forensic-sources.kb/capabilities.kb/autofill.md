---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# autofill — the active autofill service

A rogue autofill service can harvest credentials and card details across apps.

Capture:

    adb shell settings get secure autofill_service > autofill-service.txt
    adb shell dumpsys autofill                     > autofill-dump.txt

Expected to be Google/Samsung; anything else is a credential-capture concern.
