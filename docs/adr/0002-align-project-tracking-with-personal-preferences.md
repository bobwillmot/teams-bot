# ADR-0002: Align Project Tracking With Personal Preferences

## Status

Accepted

## Context

The repository already tracks agent work in `docs/agent-transcripts/` and technical decisions in `docs/adr/`.

To keep the documentation easy to scan and consistent across the project, the tracking files should follow a single naming convention. The preferred convention is lowercase hyphenated Markdown file names, while preserving conventional uppercase meta-files such as `README.md`.

## Decision

Keep project tracking in the existing folders:

- `docs/agent-transcripts/` for dated work logs
- `docs/adr/` for architecture and design decisions

Apply these naming rules within that structure:

- keep folder overview files as `README.md`
- name ADR files with a zero-padded number and lowercase hyphenated slug, such as `0002-align-project-tracking-with-personal-preferences.md`
- keep transcript files date-based as `yyyy-mm-dd.md`

## Consequences

- Project tracking stays consistent with the preferred Markdown naming style.
- New ADRs are easier to scan in file listings and predictable to create.
- The repository keeps standard uppercase meta-file names where that convention is stronger than the general hyphenated rule.