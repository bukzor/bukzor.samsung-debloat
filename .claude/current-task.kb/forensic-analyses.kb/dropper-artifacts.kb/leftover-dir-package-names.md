---
status: blocked
consumes: [storage-listing]
answers: [patient-zero, removed-apps]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "unknown"
last-updated: "2026-05-27"
---

# leftover-dir-package-names — package-named dirs on /sdcard

Method: enumerate subdirectories of `/sdcard/Android/{data,obb,media}` (each is
named by its package); any name not in the installed list is a removed-app
candidate, with mtimes to check against the window.

Blocked on a deep `storage-listing` (only `/Download` captured). Survival of
leftover dirs after uninstall is not guaranteed.
