---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# mediastore-db — owner_package_name of stored files

MediaStore records the app that added each file in `owner_package_name` — naming
the writer even after that app is uninstalled.

Capture:

    adb shell content query --uri content://media/external/file \
      --projection _data:owner_package_name:date_added > mediastore-files.txt

Targets: who wrote the dropper APK and the `_.admaster` blob in `/sdcard/Download`
(the FUSE owner UID was uninformative; this column is the real attribution).
