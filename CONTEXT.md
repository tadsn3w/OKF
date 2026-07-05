# Workspace Context

This file tells the AI how to navigate this project.  It is Layer 1 of the context hierarchy.  The AI reads this after `AGENTS.md` to know which workspace to enter for a given task.

## Workspaces

| Workspace | Purpose | Key Files |
|-----------|---------|-----------|
| `planning/` | Specs, architecture, design decisions | `planning/CONTEXT.md` |
| `build/` | Code, implementation, testing | `build/CONTEXT.md` |
| `docs/` | API docs, user guides, changelogs | `docs/CONTEXT.md` |
| `ops/` | Deploy, monitoring, CI/CD, scripts | `ops/CONTEXT.md` |
| `skills/` | Reusable instruction packages | `skills/CONTEXT.md` |

## Routing

The task-to-workspace routing table lives in `AGENTS.md` (the single source of truth, loaded every session). This file describes each workspace; `AGENTS.md` tells you which one to enter.

**Routing example:** If the user asks "add login with Google", the agent reads `AGENTS.md`, finds it maps to `planning/`, reads `planning/CONTEXT.md`, then works through the planning workflow. Only when the spec is `final` does it route to `build/`.

## Conventions

- All outputs go into `outputs/`, filed by one of two axes:
  - `by-skill/<skill>/` — grouped by what produced the file (e.g. `excalidraw/`, `code-review/`).
  - `by-system/<component>/` — grouped by what the file is about (e.g. `auth-service/`, `oracle-erp/`).
  - Tiebreaker: use `by-system/` when the file clearly belongs to one component; otherwise `by-skill/`.
- Session notes and learnings go into `notes/`.
- Stable reference material lives in `_config/`.
- Each workspace's `CONTEXT.md` defines its inputs, process, and outputs.
- When unsure which workspace to use, ask.  Do not guess.
