# Personal/forensic data stays out of git

This repo is a publishable "works for me" project. The forensic capture
contains another person's private data — full app inventory, account hints,
SMS-capable package lists, a pulled (potentially malicious) APK.

Convention:

- All capture output goes under `forensics/<timestamp>-<model>/`, which is
  **gitignored** (added to `.gitignore` this session, alongside `trash/`).
- This `current-task.kb/` may reference capture *filenames* and quote *small,
  non-identifying* excerpts, but must not embed the mother's identity, account
  names, phone number, or card details.
- The reusable collector `forensics/collect.sh` is harmless (commands only) and
  could be promoted into `scripts/` later; its **output** never gets committed.
