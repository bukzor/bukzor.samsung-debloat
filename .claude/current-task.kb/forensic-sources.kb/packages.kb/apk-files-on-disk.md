---
capture-status: partial
captured-as: [packages-paths.txt, downloads-listing.txt, apk-search.txt]
needs-device: true
last-updated: "2026-05-27"
---

# apk-files-on-disk — APKs in /data/app and /sdcard

Installed app code paths come from `pm list packages -f` (`/data/app/...`); loose
APKs (sideload leftovers) live under `/sdcard`, especially `/sdcard/Download`.

Capture:

    adb shell pm list packages -f          > packages-paths.txt
    adb shell ls -laR /sdcard/Download     > downloads-listing.txt

The Tencent dropper APK is the key loose APK here (already pulled — see
`../../forensic-analyses.kb/dropper-artifacts.kb/apk-static-analysis.md`).
`find /sdcard -iname '*.apk'` is unreliable under the FUSE mount; prefer `ls -laR`.
