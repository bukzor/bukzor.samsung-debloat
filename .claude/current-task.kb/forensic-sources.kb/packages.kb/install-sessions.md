---
capture-status: captured
captured-as: [package-dump-full.txt]
needs-device: false
last-updated: "2026-05-27"
---

# install-sessions — recent PackageInstaller sessions

The "Install sessions" section of `dumpsys package` (already inside
`package-dump-full.txt`): staged/committed install sessions with the calling
installer and timestamps.

Usually **ephemeral** — cleared once an install completes — so it is typically
empty after the fact (and was here). Its value is a fresh `dumpsys package` taken
*right after* a suspicious install, where the session still names the installer.
