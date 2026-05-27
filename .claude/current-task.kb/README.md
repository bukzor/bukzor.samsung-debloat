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
appears **already removed** by the user's uninstall spree. The Downloads dropper
is identified: **Tencent 应用宝 app store** (sideloaded ~05-18/19) — an
accessibility + silent-install + overlay gateway that explains the symptoms, but
likely a *secondary* payload (the `_.admaster/` residue predates it). **logcat
is usable back to 05-21** (the reboot assumption was wrong) and already shows a
crashing fake-weather app — patient-zero candidates are now narrowing
(`open-question.kb/patient-zero-candidates.md`). TeamViewer is the user's own
support tool (ruled out); its Host app was removed in the spree — reinstall
during post-wipe readiness. Nothing wiped yet.

Next steps, in order:
1. **Write `scripts/forensic-report.py`** (reusable; ingests a
   `forensics/<capture>/` dir) — inline bash kept failing under `set -e`; see
   `environment.kb/use-a-real-script-not-inline-bash.md`.
2. Use it to mine `logcat-events.txt` + usagestats and **confirm patient zero**.
3. Account-side Play **Library** for the definitive removed-app list / install
   source.
4. Then **wipe + de-Samsung** (reinstall TeamViewer Host as readiness).
