---
last-updated: "2026-05-26"
---

# Current task — at a glance

Forensics → wipe → de-Samsung of a family member's compromised Galaxy S24+.
Read `mission.md` first for the goal and the hard "forensics before wipe"
constraint.

## Where things are

- `mission.md` — goal, phased plan, ordering constraints, card-fraud stance.
- `device.md` — what the phone is, how we connect.
- `history.md` — user-reported symptoms, prior cleanup, timeline anchors.
- `findings.kb/` — what the read-only capture established (incl. ruled-out).
- `open-question.kb/` — what's still unknown and how to resolve each.
- `environment.kb/` — operational gotchas (wireless-ADB-only, Auto Blocker,
  pairing volatility, data handling, scoped-storage attribution).

## State as of last-updated

Read-only capture taken (`forensics/20260526-182045-SM-S926U/`). Active malware
appears **already removed** by the user's uninstall spree. Confirmed adware
residue in Downloads (a 33 MB dropper APK + a hidden `_.admaster/` dir).
TeamViewer is the user's own support tool (ruled out), though its main Host app
was removed in the spree — reinstall during post-wipe readiness. Nothing wiped
yet. Immediate next steps: identify the dropper APK; pull the account-side Play
Library; then proceed to wipe + de-Samsung.
