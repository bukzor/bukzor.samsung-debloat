---
status: confirmed
confidence: high
relates-to: [adware]
last-updated: "2026-05-27"
---

# The dropper is Tencent 应用宝 (Yingyongbao / "MyApp") app store

Static analysis (`pulled/dropper-analysis.txt`, via androguard) identifies the
33 MB `/sdcard/Download` APK as:

- **`com.tencent.android.qqdownloader`**, label **应用宝**, v9.2.1, targetSdk 29.
- **Validly signed by Tencent** (Android QZone Team, Tencent Company, Beijing;
  cert sha256 `9C:28:6B:8B…8D:36`). So it is the *genuine* Tencent third-party
  app store — not a forged/trojanized APK. In Western contexts it is widely
  classified **riskware/PUA** and is a known malware-distribution vector.

Why it explains every symptom — it declares and requests the full abuse kit:

- `YYBAccessibilityService` (accessibility) + a notification listener →
  screen-watching and the "Settings closes itself" self-defense.
- `SYSTEM_ALERT_WINDOW` → the zero-interaction "phone is dirty" overlays.
- `INSTALL_PACKAGES` + `REQUEST_INSTALL_PACKAGES` + `DELETE_PACKAGES` → silent
  install/removal of further junk.
- `QUERY_ALL_PACKAGES`, `PACKAGE_USAGE_STATS`, `READ_SECURE_SETTINGS`,
  `RECORD_AUDIO`, plus keep-alive/"alliance.alive"/daemon services and services
  named to mimic system components (`GMSService`, `ColorSafeService`).

**Likely a secondary payload, not patient zero.** The `_.admaster/` ad-tracking
residue (2026-05-18) predates this APK (filename 2026-05-19), so an ad component
was already active and probably fetched 应用宝. The initial vector is most
likely one of the ~30 removed apps — see `../open-questions.kb/removed-apps-list.md`.

How/when: **sideloaded** (in Downloads, not Play). Two date signals from
`downloads-listing.txt`: filename prefix **`20260519`** (app-claimed) and FS
**mtime 2026-05-25 10:05**; the `offset_32641024`-of-33166208 name is a
resumable/chunked-download marker, so it was fetched in pieces across 05-19→05-25.
**ctime not captured** (`ls -laR` only; would need `stat`, and `/sdcard`
sdcardfs ctime is often synthetic anyway). Both dates **postdate the 05-18
07:09 detonation** (`../timeline.kb/`), confirming this is downstream/secondary,
not the enabler. To land, "install unknown apps" had to be granted to some
downloader and Auto Blocker off. Both doors are now shut
(`appop-install-unknown.txt` = "No operations"; Auto Blocker re-enabled) — keep
them that way (prevention).

What fetched it is **not** recoverable from file ownership: the APK is owned by
`u0_a316` = appId 10316 = `com.google.android.providers.media.module`
(MediaProvider), the scoped-storage artifact — see
`../environment.kb/scoped-storage-ownership-not-attributable.md`. Only the
**DownloadManager db** (requesting package + source URL) can name the fetcher.

The app itself is no longer installed (no `com.tencent.*` in the package
captures); only this installer APK remained.
