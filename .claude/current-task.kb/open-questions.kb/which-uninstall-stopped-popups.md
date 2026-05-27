# Which of the ~30 uninstalls stopped the popups?

The user reported the popups stopped between uninstall #20 and #30, but not
which app did it.

Resolve: usagestats has **no** package install/remove events (confirmed — only
foreground/usage events), so the original plan to read removal timestamps there
does not work. Instead, the culprit's *last activity* ≈ when its removal stopped
the popups; recover that timestamp from the device sources in
`../forensic-sources.kb/` (dropbox last crash, batterystats last run, last
usagestats activity) once the culprit is named via `patient-zero-candidates.md`.
Lower priority — corroborates rather than blocks.
