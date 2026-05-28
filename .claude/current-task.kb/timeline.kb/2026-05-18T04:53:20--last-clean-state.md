---
when: 2026-05-18T04:53:20-05:00
relates-to: [adware]
sources:
  - "forensics/takeout-20260527/Takeout/My Activity/Google Play Store/MyActivity.html"
  - scripts/myactivity_takeout.py
---

# 2026-05-18 04:53:20 CDT — last clean state

The final Google Play "app usage" snapshot before the infection shows **only
legitimate apps**:

| app | package |
|---|---|
| Spotify | com.spotify.music |
| Samsung One UI Home (launcher) | com.sec.android.app.launcher |
| Netflix | com.netflix.mediaclient |
| YouTube | com.google.android.youtube |
| Google Photos | com.google.android.apps.photos |
| Samsung OMC agent (system) | com.samsung.android.app.omcagent |

Meaning: as of 04:53 the phone is awake and in normal, clean use — no
junk-family package has appeared yet. This is the **lower anchor** of the
trigger window. Note `Used` snapshots are batched (many apps share the 04:53:20
timestamp), so this bounds "clean through ~04:53", not a single action.
