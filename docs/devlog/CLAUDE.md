--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-collab)
---

# Development log

Chronological record of sessions. The directory listing is the index.

## What belongs

What diffs can't capture: decisions and rationale (especially rejected
alternatives), conventions established, tradeoffs that shaped the approach.

## What does NOT belong

- Lists of completed items (that's `git log`)
- Active task tracking (that's `.claude/current-task.kb/` / the subtask system)
- Code documentation (inline comments)

## Convention: identify the device

Every entry MUST name its **subject device** near the top, right under the H1
title, as a line linking to the registry — e.g.:

> **Subject device:** mother's phone #2 — Galaxy S24+ (`../devices.kb/mother-phone-02-galaxy-s24-plus.md`)

This project debloats family phones; the same owner cycles through hardware, so
the owner alone is ambiguous. The device line ties the session's chronology to
a specific unit in `docs/devices.kb/`.

## Creating entries

Filename `YYYY-MM-DD-NNN-slug.md`. Use `llm-collab-devlog "Entry title"`.
