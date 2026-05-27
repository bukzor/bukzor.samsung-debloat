# findings.kb — maintenance guide

One file per **evidence-backed forensic finding** about the subject device.

Belongs here: a discrete conclusion (or dismissed hypothesis) supported by a
specific captured artifact — "X holds overlay permission", "no accessibility
service is active", "this APK is a dropper". Each carries frontmatter
(`status`, `confidence`, `relates-to`, `last-updated`) per
`../findings.jsonschema.yaml`.

Does NOT belong here: open questions with no evidence yet
(→ `../open-questions.kb`), operational gotchas about tooling
(→ `../environment.kb/`), or the task plan (→ `../mission.md`).

Always cite the artifact the finding rests on, by capture name under
`forensics/<timestamp>/` (e.g. `appop-overlay.txt`, `downloads-listing.txt`).
When new evidence shifts a finding, edit it in place and bump `last-updated`;
flip `status` to `ruled-out` rather than deleting a dismissed hypothesis.
