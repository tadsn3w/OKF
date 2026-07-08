# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Layout

This repo uses a **multi-context** layout:

```
/
├── CONTEXT.md                         ← workspace map
├── planning/CONTEXT.md                ← specs context
├── build/CONTEXT.md                   ← implementation context
├── docs/CONTEXT.md                    ← documentation context
├── ops/CONTEXT.md                     ← ops context
├── skills/CONTEXT.md                  ← skills context
└── docs/adr/                          ← ADRs (created lazily)
```

## Before exploring, read these

- **`CONTEXT.md`** at the repo root — describes each workspace.
- The **workspace `CONTEXT.md`** for the area your task routes to (determined by the routing table in `CLAUDE.md`).
- **`docs/adr/`** — read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
