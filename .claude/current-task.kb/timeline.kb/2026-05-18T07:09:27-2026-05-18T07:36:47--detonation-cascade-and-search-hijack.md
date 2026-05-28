---
start: 2026-05-18T07:09:27-05:00
end: 2026-05-18T07:36:47-05:00
relates-to: [adware]
sources:
  - "forensics/takeout-20260527/Takeout/My Activity/Google Play Store/MyActivity.html"
  - "forensics/takeout-20260527/Takeout/My Activity/Chrome/MyActivity.html"
  - forensics/myactivity.google.com.json
  - scripts/myactivity_takeout.py
---

# 2026-05-18 07:09:27 → 07:36:47 CDT — detonation: auto-cascade + search hijack

The first malicious activity. Two concurrent threads interleave: an **automated
Play-Store-page cascade** (category-clustered, not human) and **Chrome history**
showing a **Yahoo-hijacked default search** plus a scam page. `[P]` = Play
store-page visit; `[C]` = Chrome page visit; `[S]` = Play search (her own).

| time | src | event |
|---|---|---|
| 07:09:27 | P | Visited **GPS Offline Maps & Navigation** (cascade begins) |
| 07:10:33 | C | Visited "Free Trial … \| Google Cloud" |
| 07:10:44 | P | Visited Easy Homescreen (`easy.launcher`) |
| 07:11:07 | C | Visited **"Wrinkle-Lift Peptides & Vita A Retinol Cream – Jhati"** (dropship/scam page) |
| 07:12:24 | P | Visited Voice GPS - Maps & Navigation |
| 07:12:40 | P | Visited GPS Maps Navigation Directions |
| 07:12:59 | P | Visited GPS Voice Map & Route Finder |
| 07:13:16 | P | Visited GPS Voice Map: Live Navigation |
| 07:14:29 | P | Visited GPS Maps Navigation GPS Camera |
| 07:15:06 | P | Visited ScanNow Home (`com.eet.scan.launcher`) |
| 07:15:25 | P | Visited Password Autofill (`com.passwordmanager.apps.mypassword`) |
| 07:16:40 | P | Visited Super HomeScreen (`com.sunteame.superhomescreen`) |
| 07:17:12 | P | Visited Inbox Homescreen (`com.eet.email.launcher`) |
| 07:18:30 | P | Visited Calendar 2026 |
| 07:19:16 | P | Visited Calendar For Android |
| 07:20:36 | P | Visited Calendar - Easy Planner |
| 07:20:51 | C | Visited "Sign in - Google Accounts" |
| 07:24:35 | P | Visited Voice GPS Navigation Direction |
| 07:25:07 | P | Visited Weather Forecast - Live Alerts |
| 07:25:33 | P | Visited Weather Pro – Daily Forecast |
| 07:27:15 | P | Visited Daily Weather: Forecast&Alerts |
| 07:28:27 | P | Visited Google Play Store (home) |
| 07:28:40 | S | Searched "602 club" |
| 07:28:43 | S | Searched "602 club" |
| 07:28:43 | P | Visited Google Play Store (home) |
| 07:32:16 | P | Visited Local News: Breaking & Latest |
| 07:33:03 | C | Visited **"live music near me - Yahoo Search Results"** |
| 07:33:23 | C | Visited "local bars with live music near me tonight - Yahoo Search Results" |
| 07:36:47 | C | Visited **"spotify - Yahoo Search Results"** |

## Reading

- **The Play cascade is automated.** Seven near-identical GPS-nav clones open in
  ~5 min, then a launcher/homescreen cluster, three calendar clones, three
  weather clones — store pages opening 15–80 s apart in tight *category*
  batches. No human opens seven interchangeable GPS apps. This is the seed
  driving Play-deeplink popups (cf. `../findings.kb/ppi-adware-bundle-detonated-0518.md`).
- **Browser search was hijacked to Yahoo.** Her genuine queries ("602 club",
  "live music near me", "spotify") return as **"Yahoo Search Results"** — the
  classic adware default-search redirect — and a dropship/scam retinol page
  appears at 07:11. So *she* is using the phone (the `[S]`/`[C]` queries are
  hers) while the cascade runs *around* her, exactly matching the reported
  zero-interaction popups.
- The seed itself is **not in this listing** — it predates 07:09:27 and is
  off-Play (see the silent-window entry). The launchers, password-autofill, and
  calendar clones here are *payloads* it pushed, not the controller.
- **On-phone, confirmed.** The live scrape (`myactivity.google.com.json`) tags
  every event in this window device `samsung SM-S926U` — the cascade is on the
  phone, not her TV or another device.
