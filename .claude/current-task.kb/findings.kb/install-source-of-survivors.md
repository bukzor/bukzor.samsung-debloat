---
status: confirmed
confidence: high
relates-to: [adware]
last-updated: "2026-05-27"
---

# Every surviving third-party app is store-installed; patient zero is gone

Install attribution from `package-dump-full.txt` for all **48** currently
installed third-party packages (`packages-3rdparty.txt`):

- **100% store-installed.** Every one has `packageSource=0` and an
  `installerPackageName` of `com.android.vending` (Play),
  `com.sec.android.app.samsungapps` (Galaxy Store), or `com.android.chrome`
  (Chrome web-APK/PWA). **Zero sideloads survive** — no `packageSource=2/3`
  (local/downloaded file), no third-party `installerPackageName=null`, nothing
  installed by a non-store app.
- **Timeline anchor — 2025-12-26.** ~29 apps share a 10:09–11:40 `firstInstallTime`
  cluster: this phone's restore/setup day (a new device). The bulk
  `2026-05-22 14:47:09` cluster elsewhere in the dump is *system* packages.
- `com.facebook.appmanager` was installed by `com.LogiaGroup.LogiaDeck` — i.e.
  **LogiaDeck = Digital Turbine / Verizon carrier preinstaller**, not adware.

Implication: the sideloaded dropper (Tencent 应用宝) and patient zero were
**uninstalled in the spree and are purged from `dumpsys package`** — uninstall
deletes the package block (only `com.imdb.mobile` survives as data-retained, and
it is benign). So on-device naming of patient zero **cannot** come from the
package db, logcat (misses the install window), or usagestats recency. It must
come from the not-yet-swept device sources in `../forensic-sources.kb/` or
account-side (`../open-questions.kb/removed-apps-list.md`). The first passive
capture is **exhausted** for this purpose; the *device* is not.

## Lesson: gate every candidate on window + "malware already gone"

Three false leads this session each came from trusting a weak surface signal
without checking the established frame:

- **name similarity** — "fake NOAA weather" was read as malicious from its name;
- **recency** — apps "last-active 05-26" were just capture-day / in-hand noise;
- **scary name** — `com.LogiaGroup.LogiaDeck` looked like adware, is carrier bloat.

Before believing any candidate, ask: is it active in the **infection window
(05-18→05-25)**, and is it consistent with **"the active malware is already
removed"**? Then confirm against the human's knowledge of her own apps
(cf. `uhc-and-pbs-are-legitimate.md`).
