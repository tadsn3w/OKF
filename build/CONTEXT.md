# Build Workspace

Layer 2 stage contract for code and implementation work.

## Inputs

- Layer 4 (working): `../planning/` — specs and architecture decisions (must be marked `final`)
- Layer 3 (reference): `../_config/user.md` — user identity and preferences
- Layer 3 (reference): `../_config/project-rules.md` — project-specific constraints
- Layer 3 (reference): `../_config/tool-rules.md` — tool conventions
- Layer 3 (reference): `../instructions/coding-rules.md` — coding conventions
- Layer 3 (reference): `../instructions/writing-style.md` — writing conventions

## Process

### Workflow

1. **Read the spec** (tool: read, grep) — Find the relevant `final` spec in `../planning/`. If no spec exists, stop and go back to planning.
2. **Plan the change** (tool: conversation, read) — State what files you'll touch and what will change. Get confirmation before writing code.
3. **Write code** (tool: edit, read) — Follow coding-rules.md. Surgical changes only. Simplicity first.
4. **Write tests** (tool: edit, read) — Tests alongside the code they test. One command to run them all.
5. **Verify** (tool: bash) — Run tests. Show the output. Confirm the change works.
6. **Clean up** (tool: edit, grep) — Remove imports, variables, or functions your changes made unused. Do not touch pre-existing dead code.

### Rules

- **No code without a spec.** If the planning spec isn't marked `final`, don't start building.
- **Surgical changes only.** Every changed line must trace to the user's request.
- **Tests are not optional.** Every feature or fix includes tests. Test output must be shown.
- **One command to verify.** `pytest`, `cargo test`, `bun test` — whatever the project uses.
- **Match existing style.** Even if you'd do it differently.

## Outputs

- Source code → project source directories
- Tests → alongside the code they test
- Build artifacts and run logs → `../outputs/by-skill/` or `../outputs/by-system/`

## Review Gate: Build → Docs

Before code moves to documentation:
- [ ] All build exit criteria below satisfied
- [ ] Tests pass and output shown
- [ ] User confirmed implementation

If tests fail or user requests changes, stay in build.

## Exit Criteria

A build task is complete when:
- [ ] Code written and corresponds to a `final` spec in `../planning/`
- [ ] Tests written and passing
- [ ] No orphaned imports, variables, or functions from your changes
- [ ] Verification command shown and confirmed working
- [ ] Only the requested scope was touched

## Conventions

- Match existing code style, even if you'd do it differently.
- Do not refactor things that aren't broken.
- Every changed line should trace directly to the user's request.
- Commit messages reference the spec: `feature-auth: implement JWT validation`.

## Common Pitfalls

- **Building without a spec.** The most expensive mistake. If the spec isn't clear, clarify before coding.
- **Refactoring adjacent code.** Don't "improve" things you weren't asked to touch. It bloats diffs and risks bugs.
- **Skipping tests.** "It's a small change" is when tests catch regressions. Always test.
- **Silent scope creep.** If you realize more code is needed than planned, stop and discuss.
