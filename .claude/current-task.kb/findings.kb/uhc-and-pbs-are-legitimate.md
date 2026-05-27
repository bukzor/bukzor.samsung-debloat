---
status: ruled-out
confidence: high
relates-to: [adware]
last-updated: "2026-05-26"
---

# `com.mobile.uhc` and `com.pbs.video` are legitimate (not adware)

Both appeared in `appop-overlay.txt` holding SYSTEM_ALERT_WINDOW (draw over
other apps) and have generic, vendorless package names — so they were flagged
as overlay-popup suspects.

The user identified them directly:

- `com.mobile.uhc` = **UnitedHealthcare** — her health-insurance app.
- `com.pbs.video` = **PBS** — she watches it.

Overlay permission is unremarkable for a video app (picture-in-picture) and a
health app (alerts). **Dismissed.** Kept as a record so they are not re-flagged
on a later pass.

Lesson: vendorless package names plus overlay permission are weak signals on
their own; confirm against the human's knowledge of their own apps before
suspecting.
