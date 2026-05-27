---
status: blocked
consumes: [mediastore-db]
answers: [patient-zero]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# mediastore-owner-attribution — who wrote the APK and the blob

Method: read `owner_package_name` from MediaStore for the dropper APK and the
`_.admaster` blob in `/sdcard/Download`. That column names the writing app even
after uninstall (the FUSE owner UID was just MediaProvider — uninformative).

Blocked on capturing `mediastore-db`. Corroborates `download-chain-of-dropper`.
