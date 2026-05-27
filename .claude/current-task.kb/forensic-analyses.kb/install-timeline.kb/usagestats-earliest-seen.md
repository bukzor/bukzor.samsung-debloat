---
status: todo
consumes: [usagestats]
answers: [patient-zero]
confidence: medium
reaches-window: "yes"
survives-uninstall: "unknown"
last-updated: "2026-05-27"
---

# usagestats-earliest-seen — order suspects by FIRST activity

Method: from the daily/weekly/monthly/yearly buckets (NOT the 24h event log),
take each package's earliest recorded activity; the earliest-appearing removed
junk app ≈ patient zero. Add as a `first-seen` view in
`scripts/forensic_report.py`.

Caveat: usagestats only logs apps that ran a component/foreground; a headless
installer may never appear, and first-activity is a lower bound on install time.
(Mirror image of the 05-26 "last-active" noise that misled us — earliest is the
signal.)
