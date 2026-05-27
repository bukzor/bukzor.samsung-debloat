# Use wireless ADB, not USB (Crostini)

This machine is a ChromeOS Crostini Linux container. **USB ADB does not work**
here, and chasing it wastes time — the original repo sessions used wireless
ADB for exactly this reason.

Observed this session: the phone was visible to the container via `lsusb`
(`04e8:6860 Samsung ... MTP mode`) and its `/dev/bus/usb` node was world-rw,
yet `adb devices` showed nothing and restarting the adb server didn't help.
Switching to **wireless debugging** connected immediately.

Procedure (per repo `README.md`):

1. Phone: Settings → Developer options → **Wireless debugging** → on.
2. "Pair device with pairing code" → gives `ip:pairing-port` + 6-digit code.
3. `adb pair <ip>:<pairing-port> <code>`
4. Main wireless-debugging screen shows a *different* `ip:connection-port` →
   `adb connect <ip>:<connection-port>`

Default: reach for wireless first; do not re-investigate USB passthrough.
