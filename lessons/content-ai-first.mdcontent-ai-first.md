# Make content AI-first: start with text, not markup

**id:** content-ai-first
**date:** 2026-08-30
**tags:** content-strategy, ai-first, architecture, markdown, html
**source:** conversation

## Lesson

When building for a world where LLMs are primary consumers, write content as plain text or structured markdown first. HTML and CSS are rendering layers — they describe how content looks, not what it means. An LLM reading your HTML pays the token cost of the markup and extracts the text anyway.

The right order: content → structure → presentation. Markdown sits at the intersection of human-readable and machine-consumable. It is semantic without being verbose. A well-formed markdown file is already an API response.

## The tradeoff

Flash of unstyled content (FOUC) is real: if you serve markdown directly to a browser without a stylesheet, there is a visible jump when styles load. This is a rendering concern, not a content concern. Solve it at the delivery layer (preloaded CSS, SSR, build-time HTML generation) — not by putting presentation logic inside your source content.

Tokens are also a rendering concern. When an LLM consumes your content, every div.wrapper is noise. Plain text or minimal markdown costs far fewer tokens and loses no meaning. AI-first means your canonical source is the format an LLM would choose if it were writing the content for itself.

## Implications

- Source in markdown, render to HTML. The build step adds presentation; the source stays clean.
- Structure semantically. Headings, lists, and code blocks carry meaning that bold spans do not.
- Expose a text endpoint. If your site serves HTML, also serve /content.txt or /lessons.json. Let LLMs skip the parser.
- Test with curl, not just a browser. If the raw response is legible without rendering, you are AI-first.

## One line

Write for the reader who never opens a browser; render for the one who does.
