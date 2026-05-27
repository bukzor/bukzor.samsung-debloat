---
status: todo
consumes: [package-dump]
answers: [patient-zero]
confidence: low
reaches-window: "yes"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# sideload-chain — reconstruct who-installed-whom

Method: build the graph where `initiatingPackageName` ≠ a store ⇒ app A installed
app B. Surfaces silent-install chains (a dropper installing siblings).

This capture: no surviving app was installed by a non-store app (the only
non-self case is carrier `LogiaDeck` → `facebook.appmanager`), so among survivors
the chain is empty — it lived among the removed apps.
