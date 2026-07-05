# Prompting Framework Skill

Methodology for writing effective CONTEXT.md files, stage contracts, and
AI prompts that minimize ambiguity and maximize first-pass accuracy.

## When to use

- Writing or revising a workspace CONTEXT.md
- Structuring a multi-step prompt for a complex task
- Debugging why an agent keeps misunderstanding a workspace contract

## Principles

### 1. Progressive disclosure

Don't dump everything into one file. Layer information so the agent reads
only what it needs at each moment:

- **What** (one line, top of file) — "This workspace handles X."
- **How** (the process section) — step-by-step, top to bottom.
- **Why** (rules / pitfalls) — anti-patterns and rationale.
- **Reference** (inputs) — what to read before starting.

The agent should be able to stop after "What" and decide whether to enter
this workspace. It reads "How" only when engaged.

### 2. Context window budgeting

Every CONTEXT.md competes for the agent's limited attention. Budget wisely:

| Content type | Token cost | When to include |
|---|---|---|
| File purpose (1 line) | ~5 tokens | Always |
| Workflow steps | ~50-100 tokens | Always |
| Rules / constraints | ~30-50 tokens | When non-obvious |
| Tool examples | ~20-40 tokens | When tool is unfamiliar |
| Anti-patterns | ~30-60 tokens | When failures are costly |
| Reference links | ~10-20 tokens | When detail lives elsewhere |

If a CONTEXT.md exceeds ~400 lines, split it: keep the contract in
CONTEXT.md, move reference material to a `references/` subfolder.

### 3. Show, don't just tell

Prefer examples over abstract rules:

```
Bad:  "Filenames should be descriptive."
Good: "Filenames: `feature-auth-spec.md`, not `notes.md`."
```

```
Bad:  "Use Mermaid for diagrams."
Good: "Diagrams in Mermaid (architecture), Excalidraw only when
       Mermaid can't express the relationships."
```

### 4. Tool-selection-first

Before writing any prompt, decide which tools handle which parts:
- **Shell** for file ops, git, builds
- **Planner** for architecture, spec writing
- **Editor** for implementation
- **Web** for research

If the prompt doesn't need a specific tool, simplify it.

## Process

1. Read the current CONTEXT.md or prompt draft.
2. Check each principle above — what's missing?
3. Rewrite with progressive disclosure, budgeted context, concrete
   examples, and tool assignments.
4. Read `notes/learnings.md` for recurring prompting mistakes.
5. Ask for feedback after first use.
