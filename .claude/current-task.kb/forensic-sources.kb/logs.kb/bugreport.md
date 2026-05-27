---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# bugreport — the superset bundle

`adb bugreport` produces a zip bundling most `dumpsys` output, all logcat
buffers, DropBox entries, batterystats history, and ANR/tombstone traces in one
shot.

Capture: `adb bugreport bugreport.zip`

Heavy (tens of MB) and slow, but a single comprehensive grab — useful as a
catch-all if picking individual sources risks missing something.
