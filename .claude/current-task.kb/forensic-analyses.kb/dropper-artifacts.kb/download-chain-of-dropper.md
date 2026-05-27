---
status: blocked
consumes: [download-manager-db]
answers: [patient-zero]
confidence: high
reaches-window: "unknown"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# download-chain-of-dropper — who fetched the Tencent APK

Method: query the DownloadManager db for the dropper APK row
(`20260519_…_offset_…apk`) and read `notificationpackage` (requesting app) + `uri`
(source URL) + `lastmod`. Names the app that pulled the dropper, even if removed.

Blocked on capturing `download-manager-db`. Highest-value lead for the sideload
chain.
