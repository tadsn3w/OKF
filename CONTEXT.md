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

## Language

**Run Trace**:
The ordered sequence of files an AI agent reads or writes during a single
execution against an OKF bundle. The graph view shows the run trace as a
path through the file nodes.
_Avoid_: execution path, file list, traversal

**Reproducible Wrongness**:
The property that when an AI takes an unexpected run trace, that same
unexpected trace appears on every re-run with the same input. This is the
substrate Tad builds mental models on — he needs to see the wrong state,
repeatably, to understand and correct it.
_Avoid_: determinism (too vague), consistency (too generic)

## Open design notes

- **Edge typing**: Lattice v1 ships with untyped directed edges (matches OKF
  spec §5.3 — links are untyped; prose conveys the relationship kind). The
  data model must reserve a slot for edge types so a later version can add
  labels (e.g. `loads-every-session`, `depends-on`, `references`) without
  breaking the schema. Two future paths: (a) AI inference from surrounding
  prose, (b) manual labeling in the ERD-style editor. Defer the decision.

- **Graph scope**: Lattice v1 shows only knowledge files (OKF bundle —
  markdown). The final product shows knowledge files + code files (v2+).
  When the AI touches a code file in v1, it is not shown on the graph; only
  the knowledge files it consulted are traced. The OKF spec is markdown-only
  today; indexing code is a real scope expansion deferred to a later version.
