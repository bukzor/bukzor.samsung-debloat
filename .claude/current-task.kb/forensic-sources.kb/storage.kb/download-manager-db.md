---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# download-manager-db — who fetched a file, and from where

The system DownloadManager db is queryable without root via its content
provider as the `shell` user.

Capture: `adb shell content query --uri content://downloads/all_downloads > downloads-db.txt`

Per-row columns of interest: `uri` (source URL), `notificationpackage` (the app
that requested the download), `_data` (saved path), `total_bytes`, `lastmod`. Can
name **what downloaded the Tencent dropper APK** and survives that app's
uninstall.
