---
status: blocked
consumes: [network-config]
answers: [card-fraud]
confidence: low
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# network-hijack — proxy / DNS / VPN tampering (MITM)

Method: check for a non-default HTTP proxy, custom private DNS, an always-on VPN,
or a rogue saved Wi-Fi — any of which can redirect/sniff traffic.

Blocked on capturing `network-config`. A clean result helps rule out a technical
card-fraud channel (pushing toward social-engineering).
