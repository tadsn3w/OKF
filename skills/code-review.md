# Code Review Skill

Reviews code changes against this project's behavioural rules and conventions.

## Before executing

- Read `notes/learnings.md` for accumulated corrections and recurring patterns.

## Process

1. Read the diff or relevant source files.
2. Check against these rules:
   - **Simplicity first** — minimum code that solves the problem, nothing speculative.
   - **Surgical changes** — every changed line traces to the user's request.
   - **Goal-driven execution** — tests passing?  Success criteria met?
   - **Project conventions** — naming, file structure, output placement.
3. Write a review with this structure:
   - What changed (summary)
   - What's good
   - What to fix or reconsider
   - What to check before merging

## After executing

- Ask for feedback on the review.
- Append any new corrections or patterns to `notes/learnings.md`.
