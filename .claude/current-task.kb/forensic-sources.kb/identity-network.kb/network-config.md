---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# network-config — proxy, DNS, VPN, saved Wi-Fi (MITM vectors)

Hijacked network config (HTTP proxy, custom private DNS, a silent VPN, a rogue
saved AP) can redirect or sniff traffic — relevant to the card-fraud thread.

Capture:

    adb shell settings get global http_proxy        > net-proxy.txt
    adb shell settings get global private_dns_mode   > net-dns.txt
    adb shell dumpsys connectivity                    > net-connectivity.txt
    adb shell dumpsys wifi                            > net-wifi.txt

Flag any non-default proxy/DNS or an unexpected always-on VPN.
