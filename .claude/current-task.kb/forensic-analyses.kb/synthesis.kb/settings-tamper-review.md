---
status: blocked
consumes: [settings-dump]
answers: [adware, card-fraud]
confidence: low
reaches-window: "no"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# settings-tamper-review — hijacked / weakened defaults

Method: diff `settings list secure|global|system` against an expected baseline —
disabled package verifier, changed assistant, captive-portal redirect, default
app overrides, proxy/DNS set — to surface tampering an analysis should follow up.

Blocked on capturing `settings-dump`. `reaches-window: no` — reflects current
state, not history.
