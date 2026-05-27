---
capture-status: captured
captured-as: [packages-3rdparty.txt, packages-3rdparty-removed.txt, packages-installer-map.txt, packages-paths.txt, packages-versions.txt]
needs-device: false
last-updated: "2026-05-27"
---

# package-inventory — installed / removed package lists

`pm list packages` in its useful variants: third-party (`-3`), include
uninstalled-with-data (`-u`), installer map (`-i`), code paths (`-f`), version
codes, plus system (`-s`) / disabled (`-d`) / enabled (`-e`).

Capture:

    adb shell pm list packages -3            > packages-3rdparty.txt
    adb shell pm list packages -u -3         > packages-3rdparty-removed.txt
    adb shell pm list packages -i -u         > packages-installer-map.txt
    adb shell pm list packages -f            > packages-paths.txt
    adb shell pm list packages --show-versioncode -3 > packages-versions.txt

The baseline "what is installed now". Diffing `-u` vs `-3` yields
uninstalled-but-data-retained apps (only `com.imdb.mobile` this capture).
