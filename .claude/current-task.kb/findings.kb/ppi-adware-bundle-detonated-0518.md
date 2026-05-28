---
status: confirmed
confidence: high
relates-to: [adware]
last-updated: "2026-05-27"
---

# A PPI adware bundle detonated the morning of 2026-05-18

Source: Takeout `My Activity/Google Play Store/MyActivity.html`, parsed by
`scripts/myactivity_takeout.py` (package-resolved usage/visit events; summary in
the gitignored `forensics/myactivity-playstore-summary.tsv`). This records
**305 packages including removed ones** — the history `Installs.json` (current
library only) and `dumpsys package` (purged) both lack.

## What the timeline shows (minute resolution, 2026-05-18)

- **04:53** — last clean usage batch (Spotify, Netflix, YouTube, Photos). No junk.
- **07:09:27** — cascade begins: Play Store pages auto-opening in tight
  **category clusters** (6 GPS-nav clones in a row, then launchers, calendars,
  weather…), many 15–20 s apart, in waves until **21:11**.
- By the **10:43** usage batch the first wave is **installed and running**
  (Network Master/Scan/Status, AntiVirus Toolkit, Norton/McAfee lookalikes,
  AppLock clones, GPS/calendar/weather clones).
- Her own fingerprints are interleaved, fighting it: Play searches `602 club`,
  `running games`, and — matching her reported symptom — **`settings for android
  samsung` at 16:08** (Settings kept closing on her).

## Nature of the bundle

~80 distinct junk packages, all **first-seen 2026-05-18**, spanning the full
adware taxonomy: cleaners, fake antivirus/VPN, app-lockers, PDF/QR "tools",
WiFi/network scanners, weather clones, GPS clones, launcher/homescreen
replacements. The three earlier "candidates" are just two minor leaf members.

Two-tier behaviour:
- **Majority = "Visited" only, 0 "Used"** — popup deep-links that opened a Play
  listing without installing. This *is* the "zero-interaction popup" symptom.
- **A subset got installed and ran** ("Used" in the 10:43/14:53/19:20 batches).

All carry real `details?id=` + "Play app usage" provenance, so the family was
**installed from the official Play Store**, not sideloaded.

## Mechanism (most likely)

A seed app holding **overlay (SYSTEM_ALERT_WINDOW)** and/or **Accessibility**
threw full-screen "your phone is dirty" interstitials that deep-link to Play
listings; the "0 Used" majority are popups she never completed. The "Settings
closes itself" symptom points to Accessibility (or an aggressive overlay
redrawing over Settings) defending the seed.

## Why this does not name patient zero by itself

The seed arrived **between ~05:00 and 07:09 on 05-18** (nothing junk-like before
07:09; 04:53 batch is clean) and is **invisible to Play telemetry** — no
junk-family "Used"/"Visited" event predates the cascade, consistent with a
headless or sideloaded controller (ties to the Tencent-dropper thread). Naming
it needs device-side sources not yet swept: DownloadManager db + sideload chain,
and residual overlay/appop holders (`appop-overlay.txt`,
`appop-install-unknown.txt` in the 05-26 capture).

## Caveat on the data

`Used` events are **batched** to coarse snapshot times (04:53, 10:43, 14:53,
19:20 — identical timestamps across many apps), so they bound *that an app ran in
a window*, not when. `Visited` events are **precise** (per store-page open) and
drive the timeline above.

## Device-attribution verified (2026-05-27)

My Activity is account-wide across 5 devices (see
`myactivity-is-account-wide-cascade-is-phone.md`), so "on the phone" needed
proof. The live scrape's per-event device tag (parsed by
`scripts/myactivity_scrape.py`) shows the entire **2026-05-18 cascade is tagged
`samsung SM-S926U` — 0 events on the Chromebook or TV**. The cascade packages
also have **0 hits in `Library.json`**, confirming the "Visited"-majority were
deep-link popups never acquired, not installs.
