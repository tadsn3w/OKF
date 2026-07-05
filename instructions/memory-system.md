# Memory System

This project uses a subset of the six-level memory taxonomy described in the
Agentic OS framework.  Levels 1-2 are built in.  Levels 3-6 are documented
here so you know what to add when you need them.

## Levels 1-2: Built in

| Level | Name | Mechanism | In this project |
|-------|------|-----------|-----------------|
| 1 | Static rules | AGENTS.md, _config/, instructions/ | Always loaded. Baseline identity, conventions, and constraints. |
| 2 | Session start hooks | Mandatory first-reads at session start | AGENTS.md defines the mandatory read set. The AI must read these before any work. |

## Levels 3-6: Gaps — add when needed

| Level | Name | What to add | When to add it |
|-------|------|-------------|----------------|
| 3 | Semantic search | A retrieval tool (mem search, Claude Mem, enquire-mcp, or a custom MCP server that indexes `notes/` and `outputs/`) | When the AI repeats mistakes across sessions or you need to recall a specific decision from weeks ago. This is the 80/20 — add this first. |
| 4 | Verbatim recall | A tool that captures exact phrasing (Mem Palace or similar) | Client work where exact wording matters (contracts, legal, published copy). |
| 5 | Knowledge bases | A structured document repository (wiki, vector store) | Domain-specific reference that changes slowly — API docs, design systems, compliance manuals. |
| 6 | Cross-tool memory | Shared memory across devices and LLM providers | Multi-tool workflows spanning different AI platforms (Claude + pi + Codex). Rarely needed. |

## Recommendation

Start with levels 1-2 (already here).  Add Level 3 when the project has
enough history that the AI starts forgetting past decisions.  Levels 4-6
are optional bolt-ons — add them only when a specific use case demands it.
