---
status: blocked
consumes: [scheduled-work, activity-manager, package-dump]
answers: [adware]
confidence: medium
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# persistence-mechanisms — what keeps junk resident

Method: cross-reference `BOOT_COMPLETED` (and similar) receivers from
`package-dump`/`activity-manager` with scheduled jobs and repeating alarms from
`scheduled-work`, by package — the keep-alive surface an adware family uses to
re-launch and survive.

Blocked on capturing `scheduled-work` / `activity-manager` (receivers are in the
captured package dump).
