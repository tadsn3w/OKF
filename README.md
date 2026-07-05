# AI-Assisted Project Template

A folder-as-workspace scaffold for any project you build with AI assistance — a CLI tool, a sync daemon, an ERP automation. The *workflow* is AI-assisted; the project can be anything. Based on the Interpretable Context Methodology (ICM), three-layer routing, and the Agentic OS framework.

## How it works

The folder is the workspace.  Each top-level folder is a work mode.  The AI reads only what is relevant to the current task.

The five layers of context:

| Layer | File | Purpose |
|-------|------|---------|
| 0 | `AGENTS.md` | Map and identity — loaded every session |
| 1 | `CONTEXT.md` | Workspace overview — what each folder is for |
| 2 | `*/CONTEXT.md` | Stage contracts — inputs, process, outputs |
| 3 | `_config/`, `instructions/` | Stable reference — rules and conventions that don't change per run |
| 4 | workspace files | Working artifacts — what the AI reads and writes |

## Getting started

1. Fill in `_config/user.md` with your identity and preferences.
2. Fill in `_config/project-rules.md` with project-specific rules.
3. Start in `planning/` to spec your work, then move to `build/`.
4. Review gates sit between planning→build, build→docs, docs→ops — pass each before proceeding.
5. Skills in `skills/` wire into workspaces via the routing table in AGENTS.md.
6. Edit context files as you learn what the AI needs to know.

## Structure

```
├── AGENTS.md           ← Layer 0: identity, rules, routing table
├── CONTEXT.md          ← Layer 1: workspace overview
├── REQUEST.md          ← write your current task here (full Neovim editing)
├── _config/            ← Layer 3: stable reference material
├── planning/           ← specs, architecture, decisions
├── build/              ← code, implementation
├── docs/               ← documentation
├── ops/                ← deployment, monitoring
├── skills/             ← reusable instruction packages (code review, etc.)
├── outputs/            ← predictable output locations
├── notes/              ← learnings and session logs
└── instructions/       ← coding, writing, and memory system conventions
```

## Workflow

### Request-first

Instead of writing prompts in a chat input box (no mouse, no Cmd+Arrow),
write your task in `REQUEST.md` using Neovim with full editing power.
The AI reads it automatically at the start of every session.

### End-session ritual

Before quitting, run the **end-session** skill to persist context:

- **Claude:** type `/end-session` (global slash command)
- **pi:** say "end session" or "wrap up"

The skill appends a summary to `notes/session-log.md` and any
learnings to `notes/learnings.md`. Run it before you quit — once
you're gone, the AI can't write the log.
