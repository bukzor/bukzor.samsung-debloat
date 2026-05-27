---
status: done
consumes: [package-dump]
answers: [patient-zero]
confidence: high
reaches-window: "yes"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# install-source-attribution — sideload vs store, per package

Method: per installed package read `packageSource` + `installerPackageName` /
`initiatingPackageName`; classify store (vending / samsungapps / chrome-PWA) vs
sideload (`packageSource` 2/3, `installer=null`, or a non-store installer).

Done → all 48 survivors store-installed, zero sideloads:
`../../findings.kb/install-source-of-survivors.md`. Kept (not removed) per the
exhaustive brain dump.
