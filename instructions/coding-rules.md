# Coding Rules

Behavioral guidelines to reduce common LLM coding mistakes. Agent-agnostic — works with Claude, pi, Codex, or any AI coding tool. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" -> "Write tests for invalid inputs, then make them pass"
- "Fix the bug" -> "Write a test that reproduces it, then make it pass"
- "Refactor X" -> "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] -> verify: [check]
2. [Step] -> verify: [check]
3. [Step] -> verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Preview-First Protocol (Tad's Rule)

**This rule is specific to Tad and overrides the "use judgment" tradeoff note.** Template users: replace or remove this section for your own workflow.

Before writing any of the following, always show a preview and wait for explicit confirmation:
- `_config/` files (user.md, project-rules.md, tool-rules.md)
- `instructions/` files (coding-rules.md, writing-style.md)
- `AGENTS.md`
- `CONTEXT.md` (any level)

**How it works:**
1. Analyze the current state
2. Show what you'd put there
3. Ask: "Want me to write this?"
4. Only write when Tad explicitly says yes

The exception is if Tad says "write it directly" or something equally unambiguous.

## 6. 60/30/10 — Minimize Prompting

**Before reaching for AI, ask: can this be automated or templated?**

For every task, decompose it into three buckets:
- **60% automation** — scripts, CLI tools, Makefiles, shell pipelines. No AI at runtime.
- **30% rules & templates** — linter configs, project templates, reusable configs, boilerplate generators, decision trees.
- **10% prompting** — the actual AI interaction. Smallest bucket.

How it works:
1. Start with the 60% — can a one-liner or existing tool solve this? If yes, use it.
2. If not, check the 30% — is there a template, linter rule, or convention that already covers this?
3. Only then reach for the 10% — write the prompt.

The test: If you're writing a long prompt for something a Makefile target could do, you skipped the 60%.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, clarifying questions come before implementation rather than after mistakes, and the user stays in control of what gets written to config and instructions.
