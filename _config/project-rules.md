# Project Rules

## What this project is

Define and prove the Open Knowledge Format (OKF) — a minimal markdown +
frontmatter format for representing project knowledge. Phase 1 delivers:

1. SPEC.md: the OKF format specification
2. `knowledge/`: a dogfood OKF bundle converting this project's own files
3. `build/okf-convert`: a script that converts any folder of markdown files
   into an OKF-conformant bundle

Phase 2 (in a separate `lattice` project) will consume OKF bundles to build
a visual project knowledge graph.

## Rules

1. Every OKF concept file MUST have a non-empty `type` field in frontmatter
   (SPEC.md §4.1).
2. Reserved filenames `index.md` and `log.md` MUST NOT be used for concepts
   (SPEC.md §3.1).
3. The dogfood bundle at `knowledge/` MUST be conformant — running the
   conversion tool on this project should produce equivalent output.
4. No speculative frontmatter fields beyond what SPEC.md defines. The
   `relations` extension (from the lattice vision) is not part of this phase.
5. Tests are required for any tool/script in `build/`.

## Technology Stack

- Python 3 for the conversion tool
- pytest for tests
- Markdown + YAML for all knowledge content
- jj (Jujutsu) for version control, backed by git

## Constraints

- macOS (Apple Silicon) — no cross-platform requirements yet
- No cloud services — everything runs locally
- No external dependencies beyond Python stdlib for the conversion tool

## Conventions

- Concept files follow the pattern `knowledge/<domain>/<concept-name>.md`
- `index.md` at every directory level for progressive disclosure
- `log.md` as creation/update history
- snake_case for Python, matching existing style
- Use `jj` for all version control: `jj describe`, `jj new`, `jj commit`, `jj undo`
