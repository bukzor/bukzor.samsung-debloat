---
status: in-progress
consumes: [package-inventory, usagestats, mediastore-db, dropbox]
answers: [patient-zero, removed-apps]
confidence: medium
reaches-window: "yes"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# removed-apps-recovery — name apps that are gone

Method: union every package *name* that appears anywhere off the package db —
`pm -u` data-retained, usagestats buckets, MediaStore `owner_package_name`,
dropbox crash entries, leftover `/sdcard/Android/*` dirs — then subtract the
installed set. Each surviving name is a removed app; cross-check the window.

The on-device complement to the account-side Play Library
(`../../open-questions.kb/removed-apps-list.md`).
