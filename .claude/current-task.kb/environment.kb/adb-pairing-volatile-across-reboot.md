# Wireless ADB pairing/ports change after reboot

Samsung wireless debugging assigns **new ports on every reboot** and the
pairing typically must be re-done. The repo devlog notes this repeatedly.

Consequences for this task:

- Don't hard-code an `ip:port`; read the current one off the phone each
  session. The repo's `master-debloat.adb.sh` takes the target as `$1`.
- **Avoid unnecessary reboots** during forensics — beyond losing logcat, each
  reboot forces a re-pair and can interrupt a capture.
- If the connection drops mid-task: re-pair (`adb pair ...`) then
  `adb connect ...` with the freshly displayed ports.
