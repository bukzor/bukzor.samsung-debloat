---
capture-status: partial
captured-as: [default-input-method.txt]
needs-device: false
last-updated: "2026-05-27"
---

# input-method — enabled IMEs (keylogger vector)

A malicious keyboard sees everything typed, including card numbers and OTPs.
Capture the default plus the full IME list:

    adb shell settings get secure default_input_method > default-input-method.txt
    adb shell dumpsys input_method                     > input-method-dump.txt

Default captured; the enabled-IME list (`dumpsys input_method`) not yet captured.
