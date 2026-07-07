---
type: Reference
title: Conventional Commits 1.0.0
description: Commit message format spec used by this project for structured commit history.
tags: [standards, commits, versioning]
timestamp: 2026-07-06T00:00:00Z
---

This project follows Conventional Commits 1.0.0 for all commit messages.
The full spec is at `standards/conventional-commits.md` in the project root.

## Summary

Commit messages are structured as:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types used in this project

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `chore:` — maintenance, config, tooling
- `test:` — adding or fixing tests
- `refactor:` — code change that neither fixes a bug nor adds a feature
- `build:` — build system or dependencies
- `ci:` — CI configuration

See `standards/conventional-commits.md` for the full specification.