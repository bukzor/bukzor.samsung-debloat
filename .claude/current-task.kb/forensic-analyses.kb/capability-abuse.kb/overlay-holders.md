---
status: done
consumes: [appops]
answers: [adware]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# overlay-holders — who can draw over other apps

Method: list `SYSTEM_ALERT_WINDOW` holders (the "phone is dirty" popup surface)
and flag non-system/unknown ones.

Done → third-party holders are UHC, PBS, Messenger — all legit
(`../../findings.kb/uhc-and-pbs-are-legitimate.md`); the malicious overlay app is
already gone. Residual per-package access times in `appops-full.txt` not yet
mined.
