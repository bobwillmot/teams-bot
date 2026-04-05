# Architecture Decision Records

This folder stores Architecture Decision Records for changes that matter beyond a single edit.

Create a new ADR when a change affects:

- project structure
- runtime behavior
- deployment or operational workflow
- testing strategy
- tooling or maintenance tradeoffs

Naming convention:

- Keep the folder README as `README.md`.
- Name ADR files with a zero-padded number and a lowercase hyphenated slug.
- Examples: `0001-track-agent-work-in-repo.md`, `0002-align-project-tracking-with-personal-preferences.md`

Recommended sections:

- Status
- Context
- Decision
- Consequences

Keep ADRs concise and focused on decisions with lasting technical impact.

Use [adr-template.md](adr-template.md) as the starting point for new records.