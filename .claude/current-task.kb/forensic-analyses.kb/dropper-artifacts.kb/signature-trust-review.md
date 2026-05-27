---
status: todo
consumes: [package-dump]
answers: [adware]
confidence: low
reaches-window: "yes"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# signature-trust-review — unexpected signers among installed apps

Method: extract each installed package's signing cert from `dumpsys package` and
flag self-signed or unexpected signers on apps that present as well-known brands
(a trojanized repackage would mis-sign).

Low priority: survivors are all store-installed, so a trojanized survivor is
unlikely — but cheap to confirm from data in hand.
