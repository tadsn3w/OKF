# Writing Style

Voice, structure, and formatting conventions for all documentation in this project.

## Voice & Tone

- **Plain and direct.** Say what you mean. No padding, no throat-clearing ("It is worth noting that…", "It should be mentioned that…").
- **Concise.** Prefer short sentences. One idea per paragraph. If you can say it in 10 words instead of 20, do it.
- **Surface tradeoffs.** When presenting options, lead with the tradeoff, not the recommendation. Let the reader decide.
- **State uncertainty.** If you're not sure, say so. Don't hedge with vague language — say "I'm not sure about X" and explain why.
- **No flattery.** Don't praise the reader's question or idea. Answer it.

## Structure

- **One concept per file.** If a topic splits naturally (e.g., API auth vs. API rate limits), split the file.
- **Descriptive filenames.** `api-auth.md`, `getting-started.md`, `architecture-decisions.md`. Not `notes.md`, `doc1.md`.
- **Short files over long ones.** If a file exceeds ~300 lines, consider splitting.
- **Headings with purpose.** Use `##` for major sections, `###` for subsections. Don't skip levels.
- **Start with a one-paragraph summary.** Every document should begin with what it covers and who it's for.

## Formatting

- **Markdown only.** No HTML, no embedded CSS, no rich text.
- **Code blocks with language tags.** Always specify the language:
  ````markdown
  ```python
  def greet(name: str) -> str:
      return f"Hello, {name}"
  ```
  ````
- **Lists for parallel items.** Bullet lists for unordered items, numbered lists for sequential steps.
- **Tables for structured data.** Column alignment, clear headers.
- **Relative links for cross-references.** `../planning/feature-auth-spec.md`, not absolute paths or URLs.

## Diagrams

- **Mermaid first.** When a diagram is needed, embed Mermaid in a fenced code block. It stays close to the text and renders in most Markdown viewers.
  ```mermaid
  graph LR
      A[Input] --> B[Process] --> C[Output]
  ```
- **Excalidraw only when necessary.** Use it for complex layouts, multi-box flows, or when Mermaid can't express the relationship clearly. Export to `outputs/` and reference by path.

## What Not To Do

- **No obvious comments.** Don't write "This is the main section" above a main section. If the code needs that comment, the code is the problem.
- **No fluff.** Don't summarize what you just said. Don't add "In conclusion" unless there's an actual conclusion.
- **No over-explaining.** If a concept is standard (git, HTTP, Markdown), assume the reader knows it. Only explain what's specific to this project.
- **No marketing language.** No "robust", "scalable", "enterprise-grade", "next-generation", "seamless". Say what it does.
- **No passive voice when active works.** "The API returns 401" not "A 401 status code will be returned by the API."

## Audience

All documents in this project are read by **two audiences**: a human developer and an AI coding agent. Write for both:
- Be precise enough that an AI can act on the instructions without guessing.
- Be readable enough that a human can scan and understand in seconds.
- Avoid ambiguity. "Update the timeout" is unclear. "Set `TIMEOUT_SECONDS` to `30` in `config.py`" is clear.
