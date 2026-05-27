# Which app was patient zero (brought the adware)?

The dropper (Tencent 应用宝) was a *secondary* payload
(`../findings.kb/dropper-is-tencent-app-store.md`). On-device leads for the
initial vector — all **removed**, all matching the "fake utility" adware
disguise:

| candidate | evidence | strength |
|---|---|---|
| `com.forecasts.noaa.live.weather` | FATAL crash in logcat **2026-05-21** (active in window); fake "NOAA weather" | strong |
| `com.weather.forecast.news` | in `usagestats.txt`, **no foreground use** (rode along, never opened) | strong |
| `com.play2248.block.numbers.merge` | usagestats last-seen **2026-05-25** (cleanup window); ad-heavy game | possible |

Note: her *legit* `com.weather.Weather` is still installed — these fake-weather
packages are distinct. Multiple fake-weather apps suggests an adware family /
one installing others.

How to resolve:
1. **Mine `logcat-events.txt`** for package install/remove events + which
   process downloaded the APK / wrote `_.admaster` (use the planned script).
2. **Web-check** the package names against adware databases.
3. **Ask the user** if she recognizes any (the uhc/pbs lesson: humans dismiss
   false positives fast).
4. **Play Library** (account-side) for the definitive removed-app list + install
   source — see `removed-apps-list.md`.

Caveat: `usagestats` only logs foregrounded apps; a purely headless dropper may
not appear there at all — logcat + Play Library cover that gap.
