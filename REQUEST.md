# Phase 1 — OKF: dogfood + conversion tool

<!-- Next session: read notes/ideas.md and run grill-with-docs -->

This is Phase 1 of a larger graph-system project. Two deliverables:

1. **Dogfood bundle** — convert this project's own scaffold files into an OKF
   knowledge bundle (`knowledge/`), proving the format works.
2. **Conversion tool** — a script that scans ANY folder of markdown files and
   produces an OKF bundle from them. This is the reusable bridge to Phase 2.

## Context / constraints

- The project was scaffolded from a generic template. All CONTEXT.md,
  instruction, and config files are placeholders that describe a generic
  workflow, not this project specifically.
- SPEC.md defines the OKF format we must conform to.
- The dogfood bundle lives in `knowledge/` at the project root.
- The conversion tool lives in `build/` and works on any folder.
- Phase 2 (future, separate project) will consume OKF bundles for
  visual/graphical maintenance — the conversion tool is its entry point.

## Plan

### Phase 1a — Customize project files
- Fill `_config/project-rules.md` with OKF-specific rules
- Clean `_config/tool-rules.md` (remove Oracle MCP, keep relevant tools)
- Update `REQUEST.md` to describe this phase (done)

### Phase 1b — Create dogfood OKF bundle
- Create `knowledge/` with OKF bundle structure per SPEC.md
- Convert project files into OKF concepts with frontmatter:
  - AGENTS.md → concept `project/agent-map`
  - CONTEXT.md → concept `project/workspace-overview`
  - Each `*/CONTEXT.md` → concepts in `project/stage-contracts/`
  - `instructions/coding-rules.md` → concept `project/rules/coding`
  - `instructions/writing-style.md` → concept `project/rules/writing`
  - `_config/user.md` → concept `project/config/user`
  - `_config/project-rules.md` → concept `project/config/project-rules`
  - etc.
- Include `index.md` files for progressive disclosure
- Include `log.md` for the creation history
- Populate frontmatter (`type`, `title`, `description`, `tags`, `timestamp`)

### Phase 1c — Build conversion tool
- Write a Python script (`build/okf-convert`) that:
  - Takes a source directory path as input
  - Scans all `.md` files recursively
  - For each file: extracts or generates YAML frontmatter
  - Outputs an OKF-conformant bundle directory
  - Generates `index.md` at each level
  - Generates a `log.md`
- The dogfood bundle (Phase 1b) should be buildable with this tool
- Tests for the conversion tool alongside it

### Phase 2 (future) — Graph system
- Separate project that consumes OKF bundles for visual/graphical maintenance
- Phase 1c's conversion tool is what feeds into it

## Success criteria

- [ ] `knowledge/` directory exists with OKF-conformant structure
- [ ] Every project meta-file has a corresponding OKF concept
- [ ] All concept files have valid frontmatter with `type` field (per SPEC.md §4.1)
- [ ] `index.md` files at each directory level for progressive disclosure
- [ ] `log.md` captures creation history
- [ ] Customized project files (`project-rules.md`, `tool-rules.md`) describe the actual OKF project
- [ ] `build/okf-convert` script exists and works on any folder of markdown files
- [ ] Running the tool on this project reproduces (or can generate) the `knowledge/` bundle
- [ ] Tests for the conversion tool pass
