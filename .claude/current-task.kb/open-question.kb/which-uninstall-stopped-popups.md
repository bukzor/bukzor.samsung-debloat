# Which of the ~30 uninstalls stopped the popups?

The user reported the popups stopped between uninstall #20 and #30, but not
which app did it.

Resolve: parse `forensics/<capture>/usagestats.txt` for package
removed/uninstall events with timestamps, order them, and correlate the
cluster around when the behavior stopped. Combined with the removed-apps list
(`removed-apps-list.md`), this can fingerprint the culprit even though it is
already gone. Lower priority — corroborates rather than blocks.
