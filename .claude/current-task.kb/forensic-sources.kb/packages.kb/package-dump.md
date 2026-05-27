---
capture-status: captured
captured-as: [package-dump-full.txt]
needs-device: false
last-updated: "2026-05-27"
---

# package-dump — per-package install metadata, perms, signers

`dumpsys package`: for every installed package — `firstInstallTime`,
`installerPackageName` / `initiatingPackageName` / `originatingPackageName`,
`packageSource`, granted permissions, signing certs, declared receivers/services.

Capture: `adb shell dumpsys package > package-dump-full.txt`

Backbone for the install-provenance analyses. Holds **only installed** packages —
uninstalled apps are purged, so it cannot recover a removed app.
