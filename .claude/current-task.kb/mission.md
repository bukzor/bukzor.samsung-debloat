# Mission

A family member's (the user's mother's) Galaxy S24+ was overrun with
zero-interaction "your phone is dirty, clean now!" popup ads and had become
nearly unusable. She also suffers recurring Visa card fraud (relation to the
phone unknown). The user wants to:

1. **Forensics first** — determine *what* the bad app was, *how* it was
   installed, and *when*, in order to **prevent recurrence**.
2. **Factory wipe** the phone.
3. **De-Samsung / debloat** it to a near-Pixel state, reusing this repo's
   scripts as a *guide* (they are months old; verify package names and ADB
   flow rather than trusting blindly).

## Hard ordering constraint

Forensics must complete **before** the wipe — the wipe destroys all on-device
evidence. Until the read-only capture is reviewed and the user is satisfied:

- **Do not** factory reset / wipe.
- **Do not** uninstall more apps, reboot unnecessarily, or run any "cleaner"
  app (those are the malware category).

## Card-fraud stance

Treat the adware and the card fraud as *possibly* linked but probably
distinct symptoms of the same risky-behavior pattern. Check for a technical
link (remote-access tools, SMS interceptors, accessibility scrapers) rather
than assuming one. Prevention likely spans both technical lockdown and
card-level controls (lock card, virtual numbers, alerts).
