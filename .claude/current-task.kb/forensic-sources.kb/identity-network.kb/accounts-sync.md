---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# accounts-sync — accounts, authenticators, sync adapters

`dumpsys account`: the device's accounts, registered authenticators, and sync
adapters — each authenticator/sync adapter names its owning package, which can
betray a leftover or unexpected app.

Capture: `adb shell dumpsys account > accounts.txt`

Avoid printing account identifiers into the kb; summarize package names only.
