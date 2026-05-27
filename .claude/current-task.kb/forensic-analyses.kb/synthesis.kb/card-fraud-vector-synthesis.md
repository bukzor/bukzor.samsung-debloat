---
status: todo
consumes: [appops, telephony-messages, autofill, network-config]
answers: [card-fraud]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "unknown"
last-updated: "2026-05-27"
---

# card-fraud-vector-synthesis — technical channel vs social engineering

Method: combine the card-fraud analyses — SMS interceptor, message content,
autofill, IME, network hijack/exfil, remote-access (TeamViewer ruled out) — into
a verdict on whether the fraud has a technical channel on this phone or is
social-engineering/phishing.

Current lean: social-engineering (technical channels mostly ruled out so far) —
see `../../open-questions.kb/card-fraud-link.md`. Finalize once the blocked
analyses run.
