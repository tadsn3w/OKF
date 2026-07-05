# Tool Rules

Conventions and constraints for the tools available to the AI agent.  Add rules as you discover tool-specific failure modes.

## Rules

1. **Read before write** — always read the workspace `CONTEXT.md` and relevant reference files before making changes in that folder.
2. **`_config/` and `instructions/` are read-only** — never modify them without explicit user confirmation.  These are stable reference.
3. **Generated content goes to `outputs/`** — build artifacts, generated files, diagrams, and export outputs.  Never place generated content in workspace folders.
4. **Session context goes to `notes/`** — learnings, session logs, and feedback go in `notes/`.  Not in workspace folders or `_config/`.
5. **Diagrams in Mermaid first** — when a diagram is needed, prefer Mermaid (embed in markdown) over Excalidraw.  Use Excalidraw only when the diagram is complex or needs manual layout.
6. **Match existing style** — when editing any file, match the existing tone, format, and conventions.  Don't reformat.

## Available Tools

### File System
- `read` — read file contents (text and images)
- `write` — create or overwrite files
- `edit` — precise text replacement edits (preferred over write for incremental changes)
- `bash` — execute shell commands (ls, grep, find, python, etc.)

### Computer-Use (macOS UI Automation)
- `list_apps` / `list_windows` — discover running apps and their windows
- `screenshot` — capture and select a window for interaction
- `click`, `double_click`, `move_mouse`, `drag`, `scroll` — mouse actions
- `keypress`, `type_text`, `set_text` — keyboard input
- `wait` — pause and refresh UI state
- `arrange_window` — resize/move windows before interaction
- `navigate_browser` — direct browser navigation to a URL
- `computer_actions` — batch multiple UI actions when no intermediate state matters

## Safety

- **Never run destructive commands without explicit confirmation.**  This includes any bash command that modifies the system.
- **Never expose secrets or credentials** — don't echo connection strings, passwords, tokens, or API keys.
- **`read` over `bash cat`** — prefer the `read` tool for file contents.  Use `bash` only for discovery (ls, grep, find) or when you need to process output.
- **Prefer `computer_actions` for UI sequences** — when the intermediate state doesn't matter, batch actions.  Use individual tools only when you need to inspect the UI between steps.
- **jj (Jujutsu) over git** — this project uses jj on top of git. Use `jj status` instead of `git status`, `jj log` instead of `git log`, and `jj describe` to edit commit messages. The repo is git underneath so `git` commands still work, but prefer `jj`.
