# What seeded the 2026-05-18 PPI cascade?

**Superseded the old 3-candidate list** (`com.forecasts.noaa.live.weather` etc.).
Those were artifacts of the impoverished first capture; the Takeout My Activity
record (`../findings.kb/ppi-adware-bundle-detonated-0518.md`) shows they are two
minor *leaf* members of an ~80-package bundle, not the source. Do **not** anchor
on them.

The real patient zero is the **seed/controller**: the app that, the morning of
2026-05-18 (between ~05:00 and the first cascade event at 07:09:27), began
throwing Play-deeplink popups and/or auto-installing the family. It is **not in
the Play usage telemetry** — no junk-family event predates 07:09 — so it is
headless or sideloaded: an off-Play controller holding **overlay and/or
accessibility** (on Android 16 the over-everything popups + "Settings closes
itself" require it). The Tencent 应用宝 APK is **downstream** (05-19→05-25), a
later distributor, not the morning trigger.

**Ruled out as the seed:** `com.open.web.ai.browser` — once the leading
candidate, now a confirmed live **adware** Play browser lacking
overlay/accessibility/install
(`../findings.kb/open-web-ai-browser-seed-candidate.md`). The best *surviving*
overlay/accessibility holder is `com.sunteame.superhomescreen`, but it appeared
mid-cascade (07:16:40), so it is not the initial seed either.

How to resolve (device-side, needs ADB reconnect):

1. **DownloadManager db** — when the dropper/seed APK was fetched and its source
   URL/referrer; a fetch in the 05:00–07:09 window names the vector.
2. **Sideload chain** — `packageSource`/`installerPackageName` of any leftover,
   and `/sdcard/Android/*` + leftover-dir package names.
3. **Residual capability holders** — re-read the 05-26 capture's
   `appop-overlay.txt` and `appop-install-unknown.txt`; a holder that is not in
   the surviving 48 is a seed lead.
4. **Account-side Play Library / Play Protect** — Protect may have flagged and
   removed the seed by name (`removed-apps-list.md`).

Gate any name on the infection window and "active malware already removed"
(`../findings.kb/install-source-of-survivors.md`).
