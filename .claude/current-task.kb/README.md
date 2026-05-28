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

**Account-side My Activity is now the spine of the case** (two captures: the live
scrape `forensics/myactivity.google.com.json` + the Takeout export under
`forensics/takeout-20260527/`, parsed by `scripts/myactivity_takeout.py`; see
`environment.kb/two-myactivity-captures-complementary.md`). Established this
session — the adware was an **~80-package PPI bundle, Play-Store-installed**,
that **detonated 2026-05-18** as a single-day store-deeplink burst (first event
**07:09:27**; 165 "Visited" + 49 "Used" that day; **zero junk activity after
05-18 21:11**, dual-source confirmed). The full chain is in `timeline.kb/`. The
older 3 "candidates" are minor leaf members — **do not anchor on them**
(`open-questions.kb/patient-zero-candidates.md`).

The **seed/controller is off-Play**: the trigger window **05-18 04:53→07:09:27**
is silent in *every* retained source (cloud + device), so it was a non-synced
browser action or a headless sideload. **Leading seed candidate:
`com.open.web.ai.browser`** ("AI Browser") — sideloaded, no Play telemetry,
**Samsung-Device-Care-flagged**, ties to the Chrome **Yahoo search-hijack**;
uninstalled 05-26 08:52. **Undated** and unconfirmed (`findings.kb/`). The Tencent
应用宝 APK is **downstream** (filename 05-19 / mtime 05-25), not the enabler.
Active malware already gone by capture; TeamViewer ruled out. Nothing wiped —
and a **data-preservation gate** now blocks the wipe until all wanted content is
backed up (`mission.md`).

Next steps, in order:
1. **Reconnect ADB** (`environment.kb/adb-reconnect-and-durable-endpoint.md`).
2. **DownloadManager db + Samsung Internet history** — the only sources that can
   *date* the seed / `com.open.web.ai.browser` and reveal the silent-window
   browser action; plus residual overlay/install-unknown appop holders.
3. **Account-side Play Protect history** — may name/date the removed seed.
4. **Backup-everything, verified** (photos, messages, contacts, app data, …) —
   the hard gate — **then** wipe + de-Samsung (reinstall TeamViewer Host).
