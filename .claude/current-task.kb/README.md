---
last-updated: "2026-05-27"
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
- `open-questions.kb/` — what's still unknown and how to resolve each.
- `environment.kb/` — operational gotchas (wireless-ADB-only, Auto Blocker,
  pairing volatility, data handling, scoped-storage attribution).
- `forensic-sources.kb/` — inventory of on-device data sources + capture state,
  in domain sub-collections (untried→captured); "what data exists / what's missing".
- `forensic-analyses.kb/` — the analysis backlog over that data; each names the
  source(s) it consumes and a status (todo/blocked/done).

## State as of last-updated

Read-only capture taken (`forensics/20260526-182045-SM-S926U/`) and analyzed with
the new `scripts/forensic_report.py`. Active malware is **already removed** by the
user's uninstall spree; the Downloads dropper is the sideloaded **Tencent 应用宝
app store** (a *secondary* payload; the `_.admaster/` residue predates it).
**Install-source analysis** of all 48 surviving third-party apps shows them
**100% store-installed (zero sideloads)**, and this phone is a **2025-12-26
restore** — so the dropper and **patient zero were uninstalled and are purged
from `dumpsys package`**. The first passive capture is therefore **exhausted**
for naming patient zero; the *device itself is not* (see `forensic-sources.kb/`).
TeamViewer is the user's own tool (ruled out); its Host app was removed —
reinstall during post-wipe readiness. Nothing wiped yet.

Next steps, in order:
1. **Reconnect ADB** (`environment.kb/adb-reconnect-and-durable-endpoint.md`).
2. **Sweep the device sources** in `forensic-sources.kb/` — the DownloadManager db
   (who fetched the dropper) and `/sdcard/Android/*` leftovers can name a package
   directly; dropbox/batterystats reach before the logcat crash buffer. Run the
   no-device analyses meanwhile (`forensic-analyses.kb/`: usagestats-earliest-seen,
   install-timeline-clustering, residual-appops/overlay mining).
3. **Account-side Play Library** for the definitive removed-app list
   (`open-questions.kb/removed-apps-list.md`).
4. Only once patient zero is named or proven unrecoverable: **wipe + de-Samsung**
   (reinstall TeamViewer Host as readiness).
