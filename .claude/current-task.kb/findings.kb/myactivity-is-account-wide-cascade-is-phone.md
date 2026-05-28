---
status: confirmed
confidence: high
relates-to: [adware, general]
last-updated: "2026-05-27"
---

# My Activity is account-wide across 5 devices — but the 05-18 cascade is the phone's

A methodological caveat and its resolution, together.

## The account spans five devices, so Play / My-Activity data is not phone-only

Takeout `Google Play Store/Devices.json` lists **five** devices on this Google
account, not just the subject phone:

| device | kind | registered | last active |
|---|---|---|---|
| samsung **SM-S926U** (`e2q`) | the subject phone | **2025-12-26** | 2026-05-26 |
| Google `hatch_cheets` | Chromebook (ARC runs Android apps) | 2023-05-28 | 2026-05-26 |
| Hisense `lushan` "SmartTV 4K" | Android TV | 2025-08-09 | 2026-05-21 |
| Google `kiwi_x86_64` "HPE device" | cloud/emulator VM | 2025-12-18 | 2025-12-19 |
| "PC" | a PC | 2025-12-16 | 2026-05-01 |

So **any timeline built on My Activity / Play data is account-wide** and could
mix in events from the Chromebook or TV. This was an unverified assumption in
the cascade timeline (`ppi-adware-bundle-detonated-0518.md` and `timeline.kb/`),
which read the events as on-the-phone.

(Aside: the phone's `deviceRegistrationTime` of **2025-12-26** independently
corroborates the "2025-12-26 restore/setup" anchor in
`install-source-of-survivors.md`.)

## Verified: the 05-18 detonation is on the phone, not the TV/Chromebook

The live scrape carries a per-event device tag the Takeout HTML lacks. Parsed
with the committed extractor `scripts/myactivity_scrape.py` (→
`forensics/myactivity-scrape.jsonl`, 1387 actionable events):

- **Whole scrape:** 1378 tagged `samsung SM-S926U`, **5** `Hisense SmartTV 4K`,
  4 untagged. The Chromebook contributes **zero** Play My-Activity events.
- **2026-05-18 (CDT day):** 291 `samsung SM-S926U`, **0** TV, **0** Chromebook,
  3 untagged (her own searches). The 07:09–07:32 GPS/launcher/calendar/weather
  cascade is **entirely** SM-S926U.

So the multi-device contamination risk is real in general (the TV does appear)
but **nil for the infection window** — the cascade and the Yahoo search-hijack
happened on the phone. This converts the timeline's "on-phone" claim from
assumed to **verified**.

## Corroboration: the cascade apps were never even Play-acquired

Spot-checking cascade package ids (`easy.launcher`, `com.eet.scan.launcher`,
`com.passwordmanager.apps.mypassword`, `com.weather.accurate.pro`) against
Takeout `Library.json` (account-wide entitlements, incl. removed apps) returns
**0 hits** each — they were never installed *or acquired*, only deep-link
"Visited". Reinforces the popup-deep-link reading over an install spree.
