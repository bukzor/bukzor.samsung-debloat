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

Notable: the very first crash-buffer line is a **FATAL EXCEPTION in
`com.forecasts.noaa.live.weather`** (2026-05-21) — a weather-*named*
third-party package, **not installed now** and distinct from her legit
`com.weather.Weather`. We have **not** examined this APK, so calling it "fake"
or malicious is unverified; the suspicious name plus a crash in-window make it a
**patient-zero candidate**, not a confirmed payload
(see `../open-questions.kb/patient-zero-candidates.md`).

Mined since, via `scripts/forensic_report.py`: the events buffer contains **no**
package install/remove events, and the main/system buffers only cover the last
~1 hour — so logcat **cannot** date the dropper install or attribute who wrote
it. The crash buffer (back to 05-21) yields crashes-by-package only (and the
`com.forecasts.noaa.live.weather` entry is a benign Firebase boot-race, not
proof of malice). logcat is volatile — re-capture if the phone reboots
(`adb logcat -d -v year [-b events]`).
