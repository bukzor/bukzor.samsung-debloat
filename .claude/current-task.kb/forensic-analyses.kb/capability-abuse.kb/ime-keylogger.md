---
status: todo
consumes: [input-method]
answers: [card-fraud]
confidence: low
reaches-window: "unknown"
survives-uninstall: "no"
last-updated: "2026-05-27"
---

# ime-keylogger — malicious keyboard check

Method: review enabled IMEs (`dumpsys input_method`) for any non-Google/Samsung
keyboard; a malicious IME captures everything typed (card numbers, OTPs).

Only the default IME is captured so far — needs the enabled-IME list to close.
