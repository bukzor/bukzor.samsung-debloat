---
last-updated: "2026-05-28"
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

The **trigger was most likely web, not an app**: the window **05-18
04:53→07:09:27** is silent in *every* retained source, and a dense-capture check
(04-29→05-26, 37–67 events/day) finds **no controller-profile app** in the
>2-week run-up — so the favored reading is a **malvertising page tapped in
Samsung Internet** (history not in Takeout), firing the deep-link storm with **no
installed seed**. `com.sunteame.superhomescreen` (accessibility+overlay, visible
mid-cascade) **escalates** the problem but does not initiate it.
`com.open.web.ai.browser`
("AI Browser") was the leading candidate but is **ruled out** (2026-05-28) — it's
a live adware Play browser lacking overlay/accessibility/install, so neither
off-Play nor capable of being the controller; it doesn't explain the Yahoo
hijack either (`findings.kb/open-web-ai-browser-seed-candidate.md`). The Tencent
应用宝 APK is **downstream** (filename 05-19 / mtime 05-25), not the enabler.
Active malware already gone by capture; TeamViewer ruled out. Nothing wiped —
and a **data-preservation gate** now blocks the wipe until all wanted content is
backed up (`mission.md`).

Next steps, in order:
1. **Get the device in hand / reconnect ADB** (`environment.kb/adb-reconnect-and-durable-endpoint.md`).
2. **HIGHEST forensic priority — test the favored "web-initiated" reading:**
   - **Samsung Internet history** (manual on-device review of 05-18 04:53→07:30)
     — *the* source that could show the malvertising page that initiated it; not
     in Takeout (`forensic-sources.kb/storage.kb/samsung-internet-history.md`).
   - **DownloadManager db** — names what fetched any sideload incl. the Tencent
     APK, with timestamp + source URL
     (`forensic-sources.kb/storage.kb/download-manager-db.md`).
   Rationale: `timeline.kb/2026-05-18T04:53:20-2026-05-18T07:09:27--silent-trigger-window.md`.
3. **Account-side Play Protect history** — may name/date a removed app; plus
   residual overlay/install-unknown appop holders.
4. **Backup-everything, verified** (photos, messages, contacts, app data, …) —
   the hard gate — **then** wipe + de-Samsung (reinstall TeamViewer Host).
