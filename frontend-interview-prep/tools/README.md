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
