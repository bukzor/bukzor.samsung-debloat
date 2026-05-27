# Reconnecting wireless ADB; and making a durable endpoint

The wireless-debugging `ip:port` **rotates** whenever the phone sleeps or
reboots. Running the previously-working `adb connect <ip:port>` then fails with
`No route to host` (seen this session: `192.168.87.245:44577` went stale).

## Recovering a dropped connection

- mDNS discovery works here — `adb mdns check` → *Openscreen discovery*. The
  device connects under its mDNS name `adb-<serial>-<rand>._adb-tls-connect._tcp`
  (not a raw `ip:port`), which proves multicast traverses the Crostini bridge.
- It vanishes from `adb mdns services` only while the phone is **asleep / off
  Wi-Fi** — mDNS is live broadcast, not a stored list. **Wake + unlock** the
  phone on the same Wi-Fi and adb auto-reconnects. `adb reconnect offline` and
  `adb kill-server && adb start-server` nudge rediscovery.
- Fallback: read the current `ip:port` (+ pairing code if asked) from
  Settings → Developer options → Wireless debugging, then `adb connect …`.
- The `<rand>` suffix and port regenerate, so there is **nothing stable to
  hardcode** — rely on mDNS auto-connect, don't cache an address.

## Durable typeable endpoint — REJECTED

`adb tcpip 5555` (fixed port + a router DHCP reservation) was considered and
**rejected**: port 5555 has **no TLS/pairing auth** (any host on the LAN can
connect) and it **reverts every reboot** (re-arm needed; not persistent without
root). Not worth it. Use **mDNS auto-connect** (above) instead — wake the phone
and it reconnects on its own; nothing to type or cache.
