# What is the dropper APK?

Identify package name, signer certificate, and requested permissions of the
33 MB `forensics/<capture>/pulled/dropper.apk` — see
`../findings.kb/dropper-apk-in-downloads.md`.

Resolve: no `aapt`/`keytool`/`java` on the host; use `uv run --with androguard`
(package + perms + cert) or `unzip` the APK and inspect `META-INF` signing
blocks. The signer cert often reveals the adware family; the package name lets
us check whether it (or a sibling) is still installed.
