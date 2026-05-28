---
status: confirmed
confidence: medium
relates-to: [card-fraud]
verify-via: [sms-interceptor, removed-apps-recovery]
last-updated: "2026-05-26"
---

# No third-party SMS interceptor is currently present

Relevant to the card-fraud thread: OTP/2FA theft commonly works by an app
reading incoming SMS. Current state shows none rogue.

Evidence (capture `20260526-182045-SM-S926U/`):

- `appop-read-sms.txt` / `appop-receive-sms.txt` holders are all
  system/carrier/Google/Samsung components (`android`, telephony providers,
  `com.android.phone`, `com.samsung.android.messaging`, Verizon `vvm`/`vcast`/
  `vzw.ecid`, `com.google.android.apps.messaging`, GMS). No unknown
  third-party app.
- Default SMS role = `com.google.android.apps.messaging` (`roles.txt`).

Confidence is **medium**, not high: this is *current* state after the user's
uninstall spree — an interceptor could have been among the removed apps. The
account-side Play Library review
(`../open-questions.kb/removed-apps-list.md`) may still reveal one.
