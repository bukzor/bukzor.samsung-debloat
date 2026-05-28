---
when: "2026-05-26T08:52:03-05:00"
relates-to: [adware]
sources:
  - forensics/20260526-182045-SM-S926U/usagestats.txt
  - "forensics/takeout-20260527/Takeout/My Activity/Google Play Store/MyActivity.html"
  - scripts/myactivity_takeout.py
---

# 2026-05-26 08:52 CDT — cleanup tail; bounding the problem-period END

The only **directly observed** uninstall: `usagestats.txt` recent-task Token 251
shows the flow `Device Care → SuspiciousAppsActivity → com.open.web.ai.browser →
UninstallerActivity (uninstalling)`, and the precise event log has
`packageinstaller/UninstallerActivity` firing at **08:52:03 and 08:52:12**. This
is the *tail* of the user's ~12–30-app uninstall spree (the bulk is unrecoverable
— see below).

## Problem-period END — what can be bounded

| signal | bound |
|---|---|
| junk family last **ran** (My Activity "Used") | 2026-05-18 |
| junk family last popup-deeplink (Play "Visited") | 2026-05-18 21:11 |
| junk family **definitively not running** (absent from precise event log) | by 2026-05-25 18:20 |
| last **observed** suspicious-app uninstall | 2026-05-26 08:52 (`com.open.web.ai.browser`) |
| device clean-ish (capture) | 2026-05-26 18:24 |

So the cleanup spree falls in **2026-05-19 → 2026-05-26 08:52**, bulk before
05-25 evening. (0 of 81 junk-family apps appear in the 05-25 18:20→05-26 18:20
event log, out of 64 apps that did run there.)

## Why the exact "popups stopped" moment is not recoverable here

- **Uninstalls aren't logged in My Activity** at all (only Used/Visited/Searched).
- **logcat** main buffer spans only ~05-26 19:20→19:32 (~12 min); the
  "reaches back to 05-21" claim was the *crash* buffer, not the main log — so
  logcat cannot see a spree days earlier.
- **usagestats** keeps precise events only ~24–48h, so only the 05-26 tail
  survives; older uninstall-dialog invocations are purged.
- The one popup-proxy we have (Play "Visited") reflects the **install burst**
  (05-18), not the ongoing overlay-ad nuisance — which is logged nowhere.

Pinning the spree/cessation needs device-side **PackageInstaller/Play Protect
history** (reconnect) or the user's own recollection.
