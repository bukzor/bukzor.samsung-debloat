---
status: blocked
consumes: [dropbox]
answers: [patient-zero]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# dropbox-crash-timeline — crashes/ANRs before the logcat window

Method: parse `dumpsys dropbox --print` entries, order by package + timestamp,
and look for crash/ANR activity before logcat's crash buffer (pre-05-21) — an
adware/junk app that errored during install or first run would appear by name.

Blocked on capturing `dropbox`. Complements `logcat-crash-attribution`.
