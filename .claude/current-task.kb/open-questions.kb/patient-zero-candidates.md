# Which app was patient zero (brought the adware)?

The dropper (Tencent 应用宝) was a *secondary* payload
(`../findings.kb/dropper-is-tencent-app-store.md`). On-device leads for the
initial vector — all **removed**, all with generic/suspicious utility-style
names. None of these APKs has been examined, so "malicious" is unverified;
these are leads to investigate, not confirmed bad actors:

| candidate | evidence | strength |
|---|---|---|
| `com.forecasts.noaa.live.weather` | FATAL crash in logcat **2026-05-21** (active in window); weather-named, borrows NOAA branding | strong |
| `com.weather.forecast.news` | in `usagestats.txt`, **no foreground use** (rode along, never opened) | strong |
| `com.play2248.block.numbers.merge` | usagestats last-seen **2026-05-25** (cleanup window); ad-heavy game | possible |

Note: her *legit* `com.weather.Weather` is still installed — these
weather-named packages are distinct from it. Several weather-named packages
*could* indicate an adware family installing siblings, but could equally be
unrelated low-quality apps; unverified until the APKs or Play Library are
checked.

How to resolve: the first passive capture is exhausted for this — all 48
surviving apps are store-installed and patient zero is purged from the package db
(`../findings.kb/install-source-of-survivors.md`). Remaining avenues:

1. **Sweep the not-yet-captured device sources** — `../forensic-sources.kb/`.
   The DownloadManager db (who fetched the dropper APK) and leftover
   `/sdcard/Android/*` dirs can name a package directly; dropbox/batterystats
   reach before the logcat crash buffer.
2. **Account-side Play Library** — the definitive removed-app list + install
   source (`removed-apps-list.md`).
3. **Web-check / ask the user** any name that surfaces — but first gate it on the
   infection window and "malware already gone" (the false-lead lesson in
   `../findings.kb/install-source-of-survivors.md`).

Caveat: `usagestats` only logs apps that ran a component/foreground; a purely
headless installer may not appear there — the DownloadManager db, leftover dirs,
and dropbox cover that gap.
