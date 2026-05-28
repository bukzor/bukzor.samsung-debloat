---
status: suspected
confidence: medium
relates-to: [adware]
last-updated: "2026-05-27"
---

# `com.open.web.ai.browser` ("AI Browser") — leading seed candidate

Surfaced from `usagestats.txt` recent-task **Token 251**, which captures the
uninstall flow on **2026-05-26 08:52**:

```
Device Care → com.samsung.android.sm.cleaner.ui.SuspiciousAppsActivity
  → com.open.web.ai.browser → packageinstaller UninstallerActivity (uninstalling)
```

i.e. **Samsung Device Care's own SuspiciousApps scanner flagged it**, and she
uninstalled it through that flow.

## Why it fits the seed profile

- **Off-Play / sideloaded.** Absent from *both* My-Activity captures, from
  Takeout `Library.json`/`Installs.json`, and from the package db — present only
  as residual recent-task tokens (it had **no Play app-usage telemetry**). This
  matches the silent-window conclusion that the trigger was off-Play
  (`../timeline.kb/2026-05-18T04:53:20-2026-05-18T07:09:27--silent-trigger-window.md`).
- **A browser** → explains the **Yahoo default-search hijack** seen in Chrome
  history at 07:33–07:36 on 05-18.
- **Samsung-flagged suspicious** — an independent on-device verdict.
- **Archetype match.** Security reporting describes a current family of Android
  trojans using a hidden WebView / "AI browser" for click-fraud, sideloaded from
  third-party APK sites (bleepingcomputer.com "New Android malware uses AI to
  click on hidden browser ads"). A browser can also fire `market://` deeplinks,
  which would drive the Play-Store "Visited" cascade.

## Caveats — not yet a conviction

- **Undated.** No capture timestamps its arrival (purged on uninstall); cannot
  place it in the 05-18 silent window vs earlier.
- **Not confirmed as the cascade driver** — fits, but unproven; could be one of
  several bad sideloads. Gate per the false-lead lesson
  (`install-source-of-survivors.md`).

## How to resolve

DownloadManager db (its APK download time + source URL, if sideloaded via a
download), Play Protect history (may name/dated its removal), or ask the user
whether she recalls installing an "AI Browser". All need the ADB reconnect or
account-side access.
