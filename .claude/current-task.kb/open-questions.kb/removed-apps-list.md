# What were the ~30 apps the user uninstalled?

Most were fully uninstalled (not data-retained), so on-device `pm list packages
-u -3` recovers only one (`com.imdb.mobile`). The culprit is very likely among
the rest.

Resolve **account-side** (survives the wipe): Google Play → **"Manage apps &
device" → Manage → Library** lists every app ever installed on her account,
including removed ones. Also check Play **Protect** scan history for
flagged/removed threats. Done in a browser/Play Store signed into her account.
