# OKF Conversion Tool

**Status: final**

## Goal

Build a Python script (`build/okf-convert`) that converts a directory of
markdown files into an OKF-conformant knowledge bundle per `SPEC.md`.

The v1 tool is a deterministic converter, not an inference engine: it preserves
existing markdown links as relationships, but does not infer new graph edges.

## Scope

### In
- Recursive scan of a source directory for `.md` files
- Frontmatter extraction or generation
- Target directory with mirror of source directory structure
- `index.md` at every output directory level that contains concepts
- `log.md` at bundle root
- Bundle-level `types.md` inventory for humans to see which frontmatter `type` values exist
- Dry-run mode that previews writes without creating files
- `--stdout` mode that prints a clean JSON summary only
- Safe default excludes for generated/cache/vendor directories

### Out
- No graph or relationship inference beyond preserving existing markdown links
- No fixed taxonomy or type registry enforcement
- No file watching or incremental updates
- No git integration
- No semantic rewriting of source markdown bodies
- No claim that converting the whole project root exactly reproduces the curated
  `knowledge/` dogfood bundle

## Interface

```
usage: okf-convert <source> [--output OUTPUT] [--dry-run] [--stdout]

positional arguments:
  source            Source directory to scan

options:
  --output, -o      Target directory for the bundle (default: ./knowledge)
  --dry-run, -n     Preview what would be created without writing
  --stdout, -c      Print bundle summary as JSON instead of writing files
```

## Frontmatter Rules

| Source state | Action |
|---|---|
| Frontmatter with non-empty `type` | Preserve as-is |
| Frontmatter without non-empty `type` | Add `type: Document` |
| No frontmatter | Generate minimal: `type: Document`, `title` from filename |
| Unclosed frontmatter delimiter | Treat as no valid frontmatter and generate minimal frontmatter above the original content |

The tool does not need full YAML schema validation in v1. OKF requires parseable
YAML for conformance, but this tool only guarantees the `type` field exists or is
added when frontmatter can be recognized simply.

## Directory Mapping

- Source root → target root
- Each subdirectory → same relative subdirectory in target
- Non-`.md` files are skipped
- OKF reserved source filenames (`index.md`, `log.md`) get prefixed in output:
  `_index.md`, `_log.md` → to avoid collision with generated bundle files
- `types.md` is not reserved by `SPEC.md`; if present in source, preserve it as a
  normal concept file unless it would collide with the generated bundle-level
  `types.md`, in which case write the source file as `_types.md`

## Default Excludes

When scanning, skip these directory names anywhere in the source tree:

- `.git`
- `.venv`
- `.pytest_cache`
- `__pycache__`

Also skip the output directory if it is inside the source tree, preventing the
converter from recursively ingesting its own generated bundle.

## Index Generation

Each output directory that contains concept files gets an `index.md` with:
- A heading from the directory name (`Bundle Root` for the root)
- Bullet links to each concept with title and description when available

Generated `index.md` files contain no frontmatter.

## Type Inventory Generation

The output root gets a generated `types.md` with:
- Frontmatter using `type: Concept Directory`
- A table of distinct frontmatter `type` values discovered in generated concepts
- A count and concept links for each type

This file is informational for human navigation. It does not define or enforce a
closed taxonomy.

## Log Generation

The output root gets a `log.md` with:
- `# Bundle Update Log`
- Current UTC date as `YYYY-MM-DD`
- A creation entry naming the source path and concept count

## Verification

- `uv run pytest build/tests`
- Unit tests cover scanning, excludes, frontmatter handling, reserved filenames,
  dry-run behavior, stdout behavior, index generation, and bundle writing
- Running the converter against a fixture directory produces an OKF-conformant
  bundle: every non-reserved output markdown file has frontmatter with `type`

## Testing

Tests go in `build/tests/`. Each test:
- Creates a temp source directory with known `.md` files
- Runs the conversion
- Asserts the output bundle structure and frontmatter

---

**Status: final**
