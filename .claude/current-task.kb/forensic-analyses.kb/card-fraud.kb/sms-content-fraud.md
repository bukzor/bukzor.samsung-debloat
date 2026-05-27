---
status: blocked
consumes: [telephony-messages]
answers: [card-fraud]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# sms-content-fraud — messages for OTPs / phishing / premium-SMS

Method: review SMS/MMS history for phishing links, premium-SMS subscriptions,
fraud confirmations, and OTP patterns around the fraud dates.

Blocked on capturing `telephony-messages`. SENSITIVE: read from `forensics/`
only; record abstract conclusions in `findings.kb/`, never quote message content.
