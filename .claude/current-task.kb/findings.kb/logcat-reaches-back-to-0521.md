---
status: confirmed
confidence: high
relates-to: [adware]
last-updated: "2026-05-26"
---

# logcat is usable — it reaches back into the infection window

The earlier assumption that a reboot wiped logcat is **wrong** (the user
flagged this). Captured after-the-fact:

- `logcat-default.txt` (242k lines) earliest entry = **2026-05-21 12:46:03**
  (crash buffer). `logcat-events.txt` (15k lines) also captured.
- So logcat retains data back to at least **05-21** — squarely inside the
  period the adware was active (artifacts dated 05-18→05-25). Either there was
  no recent reboot, or it predates the 21st.

Immediate payload: the very first crash-buffer line is a **FATAL EXCEPTION in
`com.forecasts.noaa.live.weather`** (2026-05-21) — a *fake "NOAA weather"* app,
**not installed now** and **not** her legit `com.weather.Weather`. A strong
patient-zero candidate (see `../open-question.kb/patient-zero-candidates.md`).

Not yet mined: the **events buffer** (`logcat-events.txt`) for package
install/remove events and which process wrote the dropper APK / `_.admaster`.
Do this with the planned script (`../environment.kb/use-a-real-script-not-inline-bash.md`),
not inline bash. logcat is volatile — re-capture if the phone reboots before
analysis (`adb logcat -d -v year [-b events]`).
