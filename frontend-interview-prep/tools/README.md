# Rebuilding the PDFs

The PDFs in `../pdf/` are generated from the markdown files one level up.
Regenerate after editing any of them:

```bash
pip install markdown pygments pypdf reportlab
python3 build_pdf.py          # -> pdf/WeMakeScholars-Frontend-Interview-Prep.pdf
python3 build_cheatsheet.py   # -> pdf/Cheat-Sheet-Morning-Revision.pdf
```

`build_pdf.py` renders markdown to styled HTML, prints it with headless Chromium,
then stamps footers and page numbers with reportlab + pypdf. It runs Chromium
twice: the first pass locates where each section lands so the contents page can
carry real page numbers.

Two environment notes, both deliberate:

- **Emoji are replaced with CSS-drawn markers.** No colour-emoji font is installed,
  so the priority markers would print as empty boxes. `deemoji()` swaps them for
  styled spans.
- **Ligatures are disabled.** Chromium's default ligatures render "differentiator"
  as a single glyph, which breaks both Ctrl+F and the section-to-page matching.

Paths at the top of `build_pdf.py` are absolute — adjust `SRC`, `OUT` and
`SCRATCH` if you run this somewhere else.

## Markdown gotchas this build is strict about

`build_pdf.py` raises an error if any file fails to convert cleanly, because
Python-Markdown fails **silently**: when block parsing breaks, it emits the rest of
the file as raw text and the PDF ships with visible `##` and `- **` markers. Two
things cause it, and both have bitten this guide:

1. **A ``` fence indented inside a list item.** Keep code blocks at column 0, with a
   blank line before and after, or use inline backticks instead.
2. **An inline code span containing HTML tags that wraps across two lines.** The tag
   at the start of the second line is parsed as a raw HTML block and swallows
   everything after it. Put each tag in its own backticks.

Also note: a list needs a blank line before it. Without one it renders as plain text
lines instead of bullets.
