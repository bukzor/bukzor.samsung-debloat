---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-28"
---

# samsung-internet-history — the likely entry vector (web, off Takeout)

Samsung Internet (`com.sec.android.app.sbrowser`) browsing history. The **favored
seed hypothesis**
(`../../timeline.kb/2026-05-18T04:53:20-2026-05-18T07:09:27--silent-trigger-window.md`)
is that the infection was **initiated by a malvertising page tapped here** at
~07:09 on 2026-05-18. Samsung Internet history is **not** in Google Takeout, so
this is the one source that could show it — making it the **#1 forensic capture
for the next session**.

Capture (no root):

- **Manual on-device review is the realistic path** — open Samsung Internet →
  ☰ → History, scroll to **2026-05-18 ~04:53–07:30**, and screenshot/transcribe
  the pages + any redirect chain. Device is in-hand, so this needs no ADB.
- Content-provider query as `shell`
  (`content query --uri content://com.sec.android.app.sbrowser.browser/history`)
  is **likely permission-blocked** (app-private) — try, but expect failure
  without root.
- `adb backup` of the package is usually blocked (`allowBackup=false`).

Look for: an ad/redirect chain into a "your phone is infected / clean now"
interstitial, a `market://` deep-link source, or an APK-download referrer in that
window.
