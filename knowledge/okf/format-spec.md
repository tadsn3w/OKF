---
type: Specification
title: Open Knowledge Format v0.1
description: The OKF spec for representing knowledge as markdown files with YAML frontmatter — bundle structure, concept documents, cross-linking, index/log files, and conformance rules.
tags: [okf, spec, format]
timestamp: 2026-07-05T00:00:00Z
---

Defines how self-describing knowledge bundles are structured. Every concept
is a `.md` file with a required `type` field in frontmatter. Bundles use
`index.md` for progressive disclosure and `log.md` for history.
