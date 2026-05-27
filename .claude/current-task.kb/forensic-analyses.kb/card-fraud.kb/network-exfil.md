---
status: blocked
consumes: [netstats]
answers: [card-fraud, adware]
confidence: low
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# network-exfil — per-app data anomalies

Method: review per-uid data volumes (`netstats`) for an app with outsized
background traffic (ad fraud / data exfiltration).

Blocked on capturing `netstats`. Low confidence as a card-fraud signal —
recycled uids and normal app chatter make this noisy.
