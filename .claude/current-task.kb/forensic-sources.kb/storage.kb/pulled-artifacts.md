---
capture-status: partial
captured-as: [pulled/dropper.apk, pulled/admaster_uidfk.txt, pulled/dropper-analysis.txt]
needs-device: true
last-updated: "2026-05-27"
---

# pulled-artifacts — local copies for static analysis

Suspect files copied off the device for offline analysis (APKs, hidden blobs).

Capture: `adb pull <device-path> pulled/`

Pulled so far: the Tencent dropper APK, the `_.admaster` blob (encrypted,
anonymous), and the androguard analysis. Pull any further suspicious APKs/files
surfaced by the storage/download analyses.
