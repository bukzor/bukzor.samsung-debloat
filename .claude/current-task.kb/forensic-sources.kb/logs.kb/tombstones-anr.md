---
capture-status: unavailable
needs-device: true
last-updated: "2026-05-27"
---

# tombstones-anr — native crash dumps

`/data/anr/` (ANR traces) and `/data/tombstones/` (native crash dumps) name the
crashing package with timestamps, but are **root-only** for the `shell` user.

Capture (root, or extract from a bugreport):

    adb shell ls -l /data/anr /data/tombstones   # root

On this non-rooted device, reach this content via `bugreport.md` instead.
