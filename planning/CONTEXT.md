# Planning Workspace

Layer 2 stage contract for planning work: specs, architecture, design decisions.

## Inputs

- Layer 3 (reference): `../_config/user.md` — user identity and preferences
- Layer 3 (reference): `../_config/project-rules.md` — project-specific constraints
- Layer 3 (reference): `../_config/tool-rules.md` — tool conventions
- Layer 3 (reference): `../instructions/coding-rules.md` — coding conventions
- Layer 3 (reference): `../instructions/writing-style.md` — writing conventions

## Process

### Workflow

1. **Clarify** (tool: conversation) — Start by understanding what the user wants. State assumptions. Ask about scope, constraints, and open questions before writing.
2. **Explore** (tool: web, search, planner) — Research options. Surface tradeoffs. If a simpler approach exists, say so before writing a spec.
3. **Write spec** (tool: edit, read, planner) — One feature per file. Keep specs short (~200 lines max). Include:
   - Goal and scope (what's in, what's out)
   - Proposed approach with rationale
   - Tradeoffs surfaced, not hidden
   - Verification criteria (how will we know it works?)
4. **Review** (tool: conversation) — User reviews the spec. Mark decisions as `tentative` or `final`.
5. **Finalize** (tool: edit) — Only after the spec is reviewed and approved does implementation begin.

### Rules

- **Spec before code.** No implementation starts without a reviewed spec.
- **One feature per file.** If a spec exceeds ~200 lines, split it.
- **Surface tradeoffs.** Don't pick silently. Name the alternatives and why you chose one.
- **Design for what was asked, not what might be needed.** No speculative architecture.
- **Diagrams in Mermaid.** For architecture decisions, embed a Mermaid diagram in the spec. Use Excalidraw only when Mermaid can't express the relationships.

## Outputs

- Spec documents → this folder (named descriptively: `feature-auth-spec.md`, `architecture-decisions.md`)
- Architecture decision records (ADRs) → this folder
- Diagrams → embedded in specs (Mermaid) or exported to `../outputs/by-system/` (Excalidraw)
- Reviewed + marked `final` specs become Layer 4 inputs for `build/`

## Review Gate: Planning → Build

A planning task passes to `build/` when:
- [ ] All exit criteria below satisfied
- [ ] Spec has a `**Status: final**` badge
- [ ] User confirmed: "approved" or "go ahead"

Until the gate passes, the build workspace must not read this spec.

## Exit Criteria

A planning task is complete when:
- [ ] Spec written and placed in this folder
- [ ] Tradeoffs documented and discussed
- [ ] Decisions marked `tentative` or `final`
- [ ] User has reviewed and approved
- [ ] Scope boundaries clear (what's in v1, what's deferred)

## Conventions

- Filenames: `feature-name-spec.md`, `architecture-decisions.md`. Not `notes.md`, `plan.md`.
- Mark decisions with status badges: `**Status: tentative**` or `**Status: final**`.
- Keep specs short. If a concept needs deep research, write a separate research note in `../notes/`.
- Specs are read-only after finalization. Changes go through a new revision.

## Common Pitfalls

- **Skipping to code.** Don't start building before the spec is reviewed. Specs catch wrong assumptions early.
- **Designing for the future.** Don't add "flexibility" or hooks for features that weren't requested.
- **Hiding tradeoffs.** If there's a downside, say it. The user should never discover a tradeoff you didn't mention.
- **Spec creep.** If a spec keeps growing, it's multiple features. Use one file per feature, not one file per project.
