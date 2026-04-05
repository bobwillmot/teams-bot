# Teams Bot Workspace Instructions

- When asked to track agent request transcripts, implementation history, or chat transcripts for this repository, default to Markdown files under `docs/agent-transcripts/`.
- Use dated transcript files such as `yyyy-mm-dd.md` unless the repository later adopts a different convention.
- When asked to track design decisions, architecture decisions, or long-term technical tradeoffs, default to Markdown ADR files under `docs/adr/`.
- Prefer ADRs with `Status`, `Context`, `Decision`, and `Consequences` sections.
- If either tracking folder is missing, create `docs/agent-transcripts/` and `docs/adr/` before adding new entries.
- If a future documentation convention is clearly established in this repository, follow that convention instead of forcing a duplicate structure.