#!/usr/bin/env python3
"""Standalone two-column cheat sheet PDF - the only thing to read tomorrow morning."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import markdown
from build_pdf import deemoji, render, SCRATCH, SRC, OUT

CSS = """
@page { size: A4; margin: 12mm 11mm 14mm 11mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans","Liberation Sans",sans-serif; font-size: 8.2pt;
       line-height: 1.42; color: #1a1a1a; margin: 0; font-variant-ligatures: none;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.masthead { border-bottom: 3px solid #14356b; padding-bottom: 2.5mm; margin-bottom: 4mm; }
.masthead h1 { font-size: 15pt; margin: 0; color: #0d1b33; }
.masthead .sub { font-size: 8pt; color: #5a6675; margin-top: 1mm; }
.cols { column-count: 2; column-gap: 7mm; column-rule: 1px solid #dde3ec; }
h2 { font-size: 9.5pt; color: #fff; background: #14356b; margin: 0 0 2mm;
     padding: 1.4mm 2.5mm; break-after: avoid; break-inside: avoid; }
h2:not(:first-child) { margin-top: 4mm; }
h3 { font-size: 8.6pt; color: #14356b; margin: 3mm 0 1mm; break-after: avoid; }
p { margin: 0 0 2mm; }
ul, ol { margin: 0 0 2.5mm; padding-left: 4.5mm; }
li { margin-bottom: 1.1mm; break-inside: avoid; }
strong { color: #0d1b33; }
hr { border: none; border-top: 1px solid #e3e8f0; margin: 3mm 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 7.2pt; background: #eef1f6;
       padding: 0.3mm 0.8mm; border-radius: 2px; color: #9c2340; }
pre { background: #f7f9fc; border-left: 3px solid #14356b; padding: 1.8mm 2mm;
      margin: 2mm 0; white-space: pre-wrap; word-wrap: break-word; break-inside: avoid; }
pre code { background: none; color: #12203a; font-size: 6.9pt; padding: 0; }
blockquote { margin: 2mm 0; padding: 2mm 2.5mm; background: #f2f6fc;
             border-left: 3px solid #4a7ec4; break-inside: avoid; }
blockquote p { margin: 0; }
.dot { display: inline-block; width: 6px; height: 6px; border-radius: 50%; vertical-align: 1px; }
.dot-hi { background: #d93025; } .dot-med { background: #e8710a; }
.tick { color: #128a3c; font-weight: bold; } .warn { color: #b45309; font-weight: bold; }
table { width: 100%; border-collapse: collapse; font-size: 7.2pt; margin: 2mm 0; break-inside: avoid; }
th { background: #14356b; color: #fff; padding: 1.2mm; text-align: left; }
td { padding: 1.2mm; border: 1px solid #ccd4e0; }
"""

def main():
    raw = (SRC / "14-final-cheatsheet.md").read_text(encoding="utf-8")
    body_md = re.sub(r"^#\s+.*$", "", deemoji(raw), count=1, flags=re.M)
    body_md = re.sub(r"^\*\*Budget.*$", "", body_md, flags=re.M)
    # reflow: outside fenced code, join lines that are clearly wrapped continuations
    # of the previous line, so quotes read as sentences in a narrow column
    parts, out = re.split(r"(```.*?```)", body_md, flags=re.S), []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
        else:
            part = re.sub(r"(?<=[^\n:*])\n[ \t]*(?=[a-z\"\u201c(])", " ", part)
            out.append(part)
    body_md = "".join(out)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "codehilite",
                                       "sane_lists", "nl2br"])
    html = f"""<!doctype html><html><head><meta charset='utf-8'>
<title>Morning Cheat Sheet</title><style>{CSS}</style></head><body>
<div class="masthead">
  <h1>Morning Cheat Sheet &mdash; read this and nothing else</h1>
  <div class="sub">Java Backend &middot; Infosys &middot; 5 September, 4:00 PM &middot;
  Learn nothing new today &mdash; revision only.</div>
</div>
<div class="cols">{md.convert(body_md)}</div></body></html>"""
    hp = SCRATCH / "cheat.html"
    hp.write_text(html, encoding="utf-8")
    out = OUT / "Infosys-Cheat-Sheet.pdf"
    render(hp, out)
    from pypdf import PdfReader
    print(f"built {out} ({len(PdfReader(str(out)).pages)} pages, {out.stat().st_size//1024} KB)")

main()
