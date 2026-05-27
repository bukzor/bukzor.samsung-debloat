---
status: done
consumes: [pulled-artifacts]
answers: [adware]
confidence: high
reaches-window: "yes"
survives-uninstall: "yes"
last-updated: "2026-05-27"
---

# apk-static-analysis — androguard on pulled APKs

Method: run androguard over each pulled APK — package id, label, signing cert,
declared permissions and services — to classify it.

Done for the dropper → it is the genuine, Tencent-signed 应用宝 app store with the
full abuse kit: `../../findings.kb/dropper-is-tencent-app-store.md`. Re-run on any
further APKs pulled by the storage/download analyses.
