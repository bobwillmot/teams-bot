# ADR-0001: Track Agent Work In Repo

## Status

Accepted

## Context

The project is being iterated through agent-driven changes in VS Code. Without a project-local record, implementation intent and design tradeoffs are easy to lose between sessions.

The repository already contains operational setup notes in `README.md`, but it does not have a durable place to record why meaningful changes were made or what the agent actually did.

## Decision

Track two kinds of project history in Markdown inside the repository:

- agent request transcripts in `docs/agent-transcripts/`
- architecture and design decisions in `docs/adr/`

Transcript entries should be brief summaries of important work sessions. ADRs should capture decisions that have lasting technical consequences.

## Consequences

- Future work has clearer historical context inside the repository.
- Important implementation intent is visible in pull requests and Git history.
- The process adds a small documentation burden when meaningful changes are made.