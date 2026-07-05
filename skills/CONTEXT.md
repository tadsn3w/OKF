# Skills System

Reusable, modular instruction packages that plug into specific workspaces.
Each skill is a self-contained markdown file under 200 lines.

## Design principles

- **Progressive disclosure.**  The skill file loads its name and description
  first.  The AI decides whether the skill is needed.  Only then does the
  full body load.
- **Under 200 lines.**  The AI can reliably recall this amount.  Longer
  skills degrade in reliability.
- **Self-learning.**  Each skill reads `notes/learnings.md` before executing
  and asks for feedback after running.  Every run improves the next one.
- **Scrappy MVP first.**  Build a rough version, use it for a week, notice
  what breaks, fix it.  Do not try to make a perfect skill on day one.

## Wiring

Skills are wired to workspaces through the routing table in AGENTS.md.
A skill is not a workspace — it is a reusable instruction that plugs into
one or more workspaces.

## Available skills

| Skill | Wired to | Purpose |
|---|---|---|---|
| `code-review.md` | `build/` | Reviews code changes against project rules |
| `prompting-framework.md` | all workspaces | Methodology for writing effective CONTEXT.md files and prompts |

## Creating a new skill

1. Create a markdown file in `skills/`.
2. Add it to the routing table in AGENTS.md under the target workspace.
3. Follow the design principles above.
