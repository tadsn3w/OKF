# OKF — Open Knowledge Format

Minimal markdown + frontmatter format for representing project knowledge.
Includes a conversion tool and a dogfood bundle proving the format on its
own project structure.

## What's here

- `SPEC.md` — the format specification
- `knowledge/` — an OKF bundle of this project's own scaffold files
- `build/` — tools (okf-convert Python script)
- `planning/` — specs and architecture decisions
- AI workflow scaffold (`AGENTS.md`, `CONTEXT.md`, `_config/`, `instructions/`)

## Phase 1 of a larger system

Phase 2 (separate `lattice` project) will consume OKF bundles for a visual
project knowledge graph with code, control, and activity layers.
