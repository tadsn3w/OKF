# Docs Workspace

Layer 2 stage contract for documentation: API docs, user guides, changelogs.

## Inputs

- Layer 4 (working): `../planning/` — specs and design decisions
- Layer 4 (working): `../build/` — the code being documented
- Layer 3 (reference): `../_config/user.md` — user identity and preferences
- Layer 3 (reference): `../_config/project-rules.md` — project-specific constraints
- Layer 3 (reference): `../instructions/coding-rules.md` — coding conventions
- Layer 3 (reference): `../instructions/writing-style.md` — writing conventions

## Process

### Workflow

1. **Audit code** (tool: read, grep) — Before writing, read the current code and existing docs. The code is the source of truth.
2. **Start with README** (tool: edit, read) — Every project needs an entry point. README.md is the first thing a developer or AI reads.
3. **Write docs** (tool: edit, read) — One topic per file. API docs, user guides, changelogs, architecture — separate files with descriptive names.
4. **Add diagrams** (tool: edit, bash) — Use Mermaid for architecture/flow diagrams. Excalidraw only when Mermaid can't express the relationships.
5. **Verify against code** (tool: read, grep) — Confirm docs match the current code. If the code changed, check if the docs need updating.

### Rules

- **Document the present, not the future.** No stubs, no "coming soon", no planning notes in docs.
- **No obvious documentation.** Don't restate the code. Document why, not what.
- **Keep docs close to the code they describe.** Cross-reference with relative links.
- **Mermaid for diagrams.** Prefer embedded Mermaid over external diagram files.

## Outputs

- Documentation files → this folder
- API docs, user guides, changelogs, README updates
- Diagrams → embedded in docs (Mermaid) or exported to `../outputs/by-system/` (Excalidraw)

## Review Gate: Docs → Ops

Before documentation moves to operations:
- [ ] All docs exit criteria below satisfied
- [ ] Docs match current code state (no drift)
- [ ] User reviewed the documentation

Skip if no ops changes in this cycle.

## Exit Criteria

A docs task is complete when:
- [ ] Content matches the current state of the code
- [ ] Follows writing-style.md conventions
- [ ] Has a one-paragraph summary at the top
- [ ] Uses relative links to cross-reference related docs
- [ ] No stubs, placeholders, or "coming soon" sections

## Conventions

- One topic per file.
- Use descriptive filenames: `api-auth.md`, `getting-started.md`.
- Cross-reference related docs with relative links.
- Keep files under ~300 lines. Split if they grow beyond.

## Common Pitfalls

- **Documenting what doesn't exist yet.** Plans belong in `planning/`. Docs describe what's already built.
- **Duplicating code comments.** If the code clearly shows what it does, don't repeat it in docs. Focus on usage, architecture, and rationale.
- **Stale docs.** If docs aren't updated with code changes, they become misleading. Treat docs updates as part of build completion.
- **Too much structure, too little content.** A file with headings and no substance is worse than no file.
