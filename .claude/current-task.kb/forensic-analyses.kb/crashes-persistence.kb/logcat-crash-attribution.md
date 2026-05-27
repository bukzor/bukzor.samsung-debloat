---
status: done
consumes: [logcat-buffers]
answers: [patient-zero]
confidence: low
reaches-window: "yes"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# logcat-crash-attribution — crashes by package + buffer coverage

Method: scan logcat for `FATAL EXCEPTION` → attribute to the following
`Process:` line; report crashes-by-package and per-buffer time coverage (via
`scripts/forensic_report.py`).

Done → `../../findings.kb/logcat-reaches-back-to-0521.md`. Notably the
`com.forecasts.noaa.live.weather` crash is a **benign Firebase boot-race**, not
proof of malice; BofA crashed more often. Low confidence as a naming signal.
