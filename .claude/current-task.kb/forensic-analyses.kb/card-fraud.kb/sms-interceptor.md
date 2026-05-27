---
status: done
consumes: [appops]
answers: [card-fraud]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# sms-interceptor — apps reading/receiving SMS (OTP theft)

Method: list `READ_SMS` / `RECEIVE_SMS` holders and flag any non-system/
non-carrier app — the classic OTP/2FA-theft channel.

Done → all holders are system/carrier/Google/Samsung; no rogue interceptor
present (`../../findings.kb/no-rogue-sms-interceptor.md`). Confidence medium: an
interceptor could have been among the removed apps.
