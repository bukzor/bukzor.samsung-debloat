---
status: done
consumes: [notification-access]
answers: [adware]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# notification-listener-review — who reads all notifications

Method: review `enabled_notification_listeners` for unknown holders (a listener
sees every notification, incl. OTP previews).

Done → only legitimate holders (Android Auto, Samsung smart-mirroring)
(`../../findings.kb/active-malware-already-removed.md`). The posted-notification
log (who posted the popups) is a separate, not-yet-captured angle
(`../../forensic-sources.kb/capabilities.kb/notification-access.md`).
