---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# play-protect-state — was verify-apps enabled?

Whether Google Play Protect / verify-apps was on bears on how a sideload landed.

Capture:

    adb shell settings get global package_verifier_enable        > ppr-verifier.txt
    adb shell settings get global verifier_verify_adb_installs   > ppr-adb.txt

The GMS-side scan history isn't reachable without root — the account-side Play
Protect history (browser) is the fuller record (cross-ref
`../../open-questions.kb/removed-apps-list.md`).
