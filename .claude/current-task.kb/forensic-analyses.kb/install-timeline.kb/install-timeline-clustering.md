---
status: todo
consumes: [package-dump]
answers: [patient-zero]
confidence: medium
reaches-window: "yes"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# install-timeline-clustering — cluster install times, find cohorts

Method: extract `firstInstallTime` / `timeStamp` for all packages and cluster by
time to surface the restore/setup batch, OTA batches, and any sideload bursts in
the infection window. Fold into `scripts/forensic_report.py`.

Known anchor: the 2025-12-26 restore cluster
(`../../findings.kb/install-source-of-survivors.md`). Limited to surviving
packages, so it bounds *when* but cannot name a removed app.
