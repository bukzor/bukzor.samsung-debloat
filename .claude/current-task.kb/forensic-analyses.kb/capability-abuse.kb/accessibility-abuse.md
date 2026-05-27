---
status: done
consumes: [accessibility]
answers: [adware]
confidence: high
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# accessibility-abuse — screen-watching / self-defense

Method: compare `enabled_accessibility_services` against expected/known-good; an
enabled unknown service is the "Settings closes itself" abuser.

Done → services `null`, enabled `0` (none active)
(`../../findings.kb/active-malware-already-removed.md`). The abuser is gone.
