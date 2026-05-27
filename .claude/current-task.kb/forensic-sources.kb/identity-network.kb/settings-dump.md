---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# settings-dump — full secure/global/system settings

A complete settings dump catches hijacked or weakened defaults — disabled
package verifier, changed assistant, captive-portal redirect, default app
overrides — that point analyses at tampering.

Capture:

    adb shell settings list secure  > settings-secure.txt
    adb shell settings list global  > settings-global.txt
    adb shell settings list system  > settings-system.txt

Feeds `settings-tamper-review`. Some values are device-specific; diff vs a clean
baseline.
