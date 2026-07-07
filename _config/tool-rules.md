# Tool Rules

Conventions and constraints for the tools available to the AI agent in this project.

## Version Control

- **jj (Jujutsu) over git** — this project uses jj on top of git. Use `jj status`, `jj log`, `jj describe`, `jj new`, `jj squash`, `jj git push`. The repo is git underneath so `git` commands still work, but prefer `jj`.
- **Commit messages follow Conventional Commits** — `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`, `build:`, `ci:`. Full spec at `standards/conventional-commits.md`.

## Python

- **uv for Python** — use `uv run pytest` to run tests, `uv run python3` to execute scripts. Python scripts use shebang `#!/usr/bin/env -S uv run python3`. Avoid bare `pip` or `python3` commands.

## File System

- **Read before write** — always read the workspace `CONTEXT.md` and relevant reference files before making changes in that folder.
- **`_config/` and `instructions/` are read-only** — never modify them without explicit user confirmation.
- **Generated content goes to `outputs/`** — build artifacts, generated files, diagrams, and export outputs. Never place generated content in workspace folders.
- **Session context goes to `notes/`** — learnings, session logs, and feedback go in `notes/`. Not in workspace folders or `_config/`.
- **Match existing style** — when editing any file, match the existing tone, format, and conventions. Don't reformat.

## Safety

- **Never run destructive commands without explicit confirmation.** This includes any bash command that modifies the system.
- **Never expose secrets or credentials** — don't echo connection strings, passwords, tokens, or API keys.
