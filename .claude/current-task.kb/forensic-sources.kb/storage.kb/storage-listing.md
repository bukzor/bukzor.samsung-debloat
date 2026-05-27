---
capture-status: partial
captured-as: [downloads-listing.txt]
needs-device: true
last-updated: "2026-05-27"
---

# storage-listing — recursive /sdcard listing

`ls -laR /sdcard`, especially `Android/data`, `Android/obb`, `Android/media` —
each subdirectory there is **named by its package**, so leftovers can name a
removed app, with mtimes that place it in the window.

Capture:

    adb shell ls -laR /sdcard/Download                       > downloads-listing.txt
    adb shell ls -laR /sdcard/Android/data /sdcard/Android/obb /sdcard/Android/media > sdcard-android-dirs.txt

Only `/Download` captured so far. Use `ls -laR`; `find` is unreliable under the
FUSE mount, and the owner UID is always MediaProvider (uninformative).
