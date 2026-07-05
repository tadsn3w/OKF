# OKF Conversion Tool

**Status: draft**

## Goal

Build a Python script (`build/okf-convert`) that converts any directory of
markdown files into an OKF-conformant knowledge bundle (SPEC.md).

## Scope

### In
- Recursive scan of a source directory for `.md` files
- Frontmatter extraction (existing) or generation (missing)
- Target directory with mirror of source directory structure
- `index.md` at every directory level
- `log.md` at bundle root
- Types list at bundle root (`types.md`)
- Dry-run mode (preview without writing)
- stdin/stdout piping for agent workflow

### Out
- No validation of file content beyond frontmatter
- No graph or relationship inference
- No file watching or incremental updates
- No git integration

## Interface

```
usage: okf-convert <source> [--output OUTPUT] [--dry-run] [--stdout]

positional arguments:
  source            Source directory to scan

options:
  --output, -o      Target directory for the bundle (default: ./knowledge)
  --dry-run, -n     Preview what would be created without writing
  --stdout, -c      Print bundle tree to stdout (JSON) instead of writing
```

## Frontmatter Rules

| Source state | Action |
|---|---|
| Valid YAML frontmatter with `type` | Preserve as-is |
| Valid YAML frontmatter without `type` | Add `type: Document` |
| No frontmatter | Generate minimal: `type: Document`, `title` from filename |
| Malformed YAML | Wrap body in frontmatter, move original to `description` |

## Directory Mapping

- Source root → target root
- Each subdirectory → subdirectory in target
- Non-`.md` files are skipped
- Reserved names (`index.md`, `log.md`, `types.md`) in source get prefixed:
  `_index.md`, `_log.md`, `_types.md` → to avoid collision

## Index Generation

Each directory gets an `index.md` with:
- A heading from the directory name
- Bullet links to each concept with title and description

## Verification

- `pytest tests/` — unit tests for frontmatter parsing, generation, and tree building
- Running `okf-convert .` on this project must produce a bundle equivalent to `knowledge/`
  (all concepts present, all types match)

## Testing

Tests go in `build/tests/`. Each test:
- Creates a temp source directory with known `.md` files
- Runs the conversion
- Asserts the output bundle structure and frontmatter

---

**Status: draft**
