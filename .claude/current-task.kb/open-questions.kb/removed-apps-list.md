# What were the ~30 apps the user uninstalled?

Most were fully uninstalled (not data-retained), so on-device `pm list packages
-u -3` recovers only one (`com.imdb.mobile`). The culprit is very likely among
the rest.

**Largely answered** by the account-side My Activity captures: 305 packages
resolved, including the **~81-app junk family** (names + per-day activity) — see
`../findings.kb/ppi-adware-bundle-detonated-0518.md` and the gitignored
`forensics/myactivity-playstore-summary.tsv`.

Residual, still un-pulled (need account/device): Play **Protect** scan history
(named + *dated* removals — may name/date the seed) and Play **Library** (install
source). Note the leading seed candidate `com.open.web.ai.browser` is **off-Play**
so it will **not** appear in Library — Protect or the DownloadManager db are the
paths for it.
