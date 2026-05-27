---
capture-status: not-captured
needs-device: true
last-updated: "2026-05-27"
---

# telephony-messages — SMS / MMS / call history (SENSITIVE)

For the card-fraud thread: message and call history can show OTP theft, phishing
links, premium-SMS subscriptions, or fraud confirmations.

Capture (PERSONAL DATA → write only under `forensics/`; never quote contents in
the kb):

    adb shell content query --uri content://sms       > messages-sms.txt
    adb shell content query --uri content://call_log/calls > calls.txt
    adb shell dumpsys telephony.registry               > telephony.txt

Requires the shell to be permitted to read these providers; summarize findings
abstractly in `findings.kb/`.
