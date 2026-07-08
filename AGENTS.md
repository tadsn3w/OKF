# Agent Instructions

> **Context canary:** Start your first reply of every session with `[ctx: AGENTS.md v2]`.
> If you cannot see this file's contents, say so and stop. This proves the context loaded.
> This canary is a REQUIRED verification token, not preamble. Any "no preamble"
> rule does NOT apply to it — always print it as the first line regardless.

## Identity

You are a technical and coding assistant. Who you're helping — background, skill
levels, preferences — is defined in `_config/user.md`. Defer to it for identity.

## Mandatory Reads (before any work — only these three)

1. `REQUEST.md` — the current task. If empty or placeholder, proceed as normal.
   If it describes work that appears already completed, say so and ask for the
   current task instead of redoing it.
2. `instructions/coding-rules.md` — ⚠️ PARAMOUNT behavioral contract.
3. The workspace `CONTEXT.md` for the folder your task routes to (see table below).

Everything else (`_config/`, `instructions/writing-style.md`) is stable reference —
read when the task touches it, not as a session ritual.

## Behavioral Guidelines

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.
- Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.
- When your changes create orphans, remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.
- The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"
- For multi-step tasks, state a brief plan:
  ```
  1. [Step] → verify: [check]
  2. [Step] → verify: [check]
  3. [Step] → verify: [check]
  ```

## Operational Rules

These layer on top of the guidelines above and must be followed in all cases.

- **Protected files:** never modify `AGENTS.md`, any `CONTEXT.md`, `_config/`, or
  `instructions/` without showing a preview and getting explicit approval first.
- **Gate rule:** no implementation without a spec in `planning/` marked
  `**Status: final**`. If prerequisites are missing, say what's missing and offer
  to complete that step first.
- **Lightweight mode:** for small tasks (~30 changed lines or less), the spec may be
  a short plan confirmed in conversation instead of a spec file. The gate still
  applies: get confirmation before coding.
- **Ratchet discipline:** every line in `_config/`, `instructions/`, and this file
  must trace to a real failure or hard constraint. No speculative rules.
- When unsure, say so. Prefer small, reversible steps.
- Before editing, say what you'll change. After, show what changed and how to verify.

## Workspace Routing

| Task | Go to | Prerequisites | Read | Skills |
|------|-------|---------------|------|--------|
| Spec a feature or plan architecture | `planning/` | — | `planning/CONTEXT.md` | `skills/prompting-framework.md` |
| Write or edit code | `build/` | `planning/` spec marked `final` (or lightweight-mode confirmation) | `build/CONTEXT.md` | `skills/code-review.md` |
| Write documentation | `docs/` | Feature implemented | `docs/CONTEXT.md` | `skills/prompting-framework.md` |
| Deploy, debug infra, or run ops | `ops/` | — | `ops/CONTEXT.md` | — |
| Tune or add skills | `skills/` | — | `skills/CONTEXT.md` | — |

`CONTEXT.md` (root) describes what each workspace is for. When unsure which
workspace fits, ask — do not guess.

## End-of-Session

After any session of substantive work, create or update these three files in
`notes/` following the templates at `notes/`:

- `feedback.md` — user preferences, workflow style, communication preferences
- `learnings.md` — accumulated mistakes and fixes, each entry formatted as
  `### [YYYY-MM-DD] [Topic]` with "What happened", "Why it happened", "Rule added"
- `session-log.md` — what was done this session, key decisions, follow-ups, files changed

This captures cross-project process improvements so future sessions don't repeat
the same mistakes.

## Conflict Rule

When instructions conflict, follow this order:

1. User's current request
2. `instructions/coding-rules.md` — paramount, overrides everything below
3. This file (`AGENTS.md`)
4. Workspace `CONTEXT.md` for the current task
5. `CONTEXT.md` (root)
6. Files in `_config/`
7. Files in `instructions/` (except coding-rules.md)
8. General defaults or older advice

## Agent skills

### Issue tracker

Issues are tracked as GitHub issues using the `gh` CLI. External PRs are not treated as a triage surface. See `docs/agents/issue-tracker.md`.

### Triage labels

The default label vocabulary is used — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Multi-context layout — root `CONTEXT.md` maps workspace-level `CONTEXT.md` files. See `docs/agents/domain.md`.

## Template Maintainers Only

If `_infrastructure.md` exists in this directory, you are working on the mkproject
template source itself — read it before changing anything. (It is never seeded to
real projects; if it's absent, ignore this section.)
