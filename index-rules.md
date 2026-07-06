---
type: Document
title: instructions/index rules
---

# Index Rules

Rules for writing and maintaining `index.md` files across the bundle.

## Root index.md

The root `index.md` is the bundle homepage — not a concept document, not a flat directory listing.

### Structure

Use exactly two sections in this order:

1. **Knowledge Areas** — links to top-level knowledge subdirectories (e.g., `project/`, `okf/`). One bullet per area. Each bullet: `[Name](dir/) - one-line description`.
2. **Metadata** — links to cross-cutting meta files: `types.md` (frontmatter `type` inventory) and `log.md` (bundle history).

### Template

````markdown
# {Bundle Name} Knowledge Bundle

## Knowledge Areas

* [Project Structure](project/) - Project architecture, workflow, rules, config, and current task
* [Format Specification](okf/) - Open Knowledge Format specification and reference concepts

## Metadata

* [Types in this bundle](types.md) - Inventory of frontmatter `type` values
* [Update Log](log.md) - Bundle history
````

### Rules

- **No frontmatter, except `okf_version`.** The root `index.md` has no frontmatter, with one exception: the OKF spec (§11) allows an `okf_version` field to declare the bundle's target OKF version (e.g., `okf_version: "0.1"`). This is the only frontmatter permitted on an `index.md`.
- **No concept content.** The root is navigation only. Put knowledge in concept `.md` files inside subdirectories.
- **Two sections, fixed order.** Knowledge Areas first, Metadata second. Do not add other sections.
- **One bullet per area.** Keep descriptions to one line. Detail lives in the subdirectory's own `index.md`.
- **Keep it current.** When a top-level directory is added or removed, update the root `index.md` in the same change.

## Subdirectory index.md

Each subdirectory (including nested ones) has its own `index.md` listing the concepts and subdirectories inside it. It follows the same core principle as the root — navigation only — but has a simpler structure.

### Structure

Use exactly one section:

1. **Concepts** — links to every `.md` concept file and every nested subdirectory in this directory. One bullet per item.

### Template

````markdown
# {Subdirectory Name}

* [Concept Title](concept-file.md) - one-line description
* [Another Concept](another-file.md) - one-line description
* [Nested Subdirectory](subdir/) - one-line description of the subdirectory
````

### Rules

- **No frontmatter.** Subdirectory `index.md` files have no frontmatter.
- **No concept content.** Navigation only. Put knowledge in concept `.md` files, not in the `index.md`.
- **One section.** A single heading, then the bullet list. Do not add extra sections.
- **Heading matches the directory.** Use the directory name, human-readable (e.g., `project/` → `# Project`, `stage-contracts/` → `# Stage Contracts`).
- **One bullet per item.** Every concept file and nested subdirectory gets exactly one bullet. Keep descriptions to one line.
- **Descriptions come from frontmatter.** Use the linked concept's `description` field when present. Fall back to the `title` if absent.
- **Link subdirectories with a trailing slash.** `[Rules](rules/)`, not `[Rules](rules/index.md)`.
- **Keep it current.** When a concept or subdirectory is added or removed, update the `index.md` in the same change.

## Why

Structured indexes give a clear entry path at every level, separate actual knowledge from navigation, and make the bundle feel like a browsable homepage rather than a directory dump. New readers (human or agent) can answer "what's in this bundle?" — and "what's in this subdirectory?" — in one glance.