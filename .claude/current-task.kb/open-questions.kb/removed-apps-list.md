# What were the ~30 apps the user uninstalled?

Most were fully uninstalled (not data-retained), so on-device `pm list packages
-u -3` recovers only one (`com.imdb.mobile`). The culprit is very likely among
the rest.

**Largely answered** by the account-side My Activity captures: 305 packages
resolved, including the **~81-app junk family** (names + per-day activity) — see
`../findings.kb/ppi-adware-bundle-detonated-0518.md` and the gitignored
`forensics/myactivity-playstore-summary.tsv`.

Play **Library** is now **captured** (Takeout `Google Play Store/Library.json`
under `forensics/takeout-20260527/`) but **un-mined as a whole**: diff it against
currently-installed to enumerate the Play apps she removed (feeds
`removed-apps-recovery` / `patient-zero-synthesis`). Still un-pulled (need
account/device): Play **Protect** scan history (named + *dated* removals — may
name/date the seed). (`com.open.web.ai.browser`, once floated as the seed, is
**ruled out** — a live adware Play app, see
`../findings.kb/open-web-ai-browser-seed-candidate.md`.)
