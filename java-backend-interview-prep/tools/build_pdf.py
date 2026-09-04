#!/usr/bin/env python3
"""Build a printable PDF study guide from the frontend-interview-prep markdown files."""
import re, subprocess, sys, os, html
from pathlib import Path
import markdown

SRC = Path("/home/user/Java/java-backend-interview-prep")
OUT = Path("/home/user/Java/java-backend-interview-prep/pdf")
SCRATCH = Path("/tmp/claude-0/-home-user-Java/511b1e01-f010-504c-a181-1e9c535fa679/scratchpad")

ORDER = ["README.md", "01-core-java.md", "02-java8-functional.md",
         "03-spring-boot.md", "04-jpa-hibernate.md", "05-microservices.md",
         "06-kafka-rabbitmq.md", "07-spring-security-jwt.md",
         "08-sql-and-databases.md", "09-coding-round.md", "10-system-design.md",
         "11-your-experience.md", "12-hr-and-behavioural.md",
         "13-delivery-and-code-review.md", "14-final-cheatsheet.md"]

# Emoji -> print-safe markup (no colour-emoji font exists in this environment)
def deemoji(text: str) -> str:
    text = text.replace("\U0001F534\U0001F534", '<span class="dot dot-hi"></span><span class="dot dot-hi"></span>')
    text = text.replace("\U0001F534", '<span class="dot dot-hi"></span>')
    text = text.replace("\U0001F7E0", '<span class="dot dot-med"></span>')
    text = text.replace("✅", '<span class="tick">✓</span>')
    text = text.replace("⚠️", '<span class="warn">⚠</span>')
    text = text.replace("⚠", '<span class="warn">⚠</span>')
    for junk in ["\U0001F525", "☕", "\U0001F305", "\U0001F680", "\ufe0f"]:
        # take an adjacent space with it, so "**Go get it. X**" stays bold
        text = text.replace(" " + junk, "").replace(junk + " ", "").replace(junk, "")
    return text

def title_of(md_text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.*)$", md_text, re.M)
    if not m:
        return fallback
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", deemoji(m.group(1)))).strip()

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", "Liberation Sans", sans-serif; font-size: 10pt;
       line-height: 1.5; color: #1a1a1a; margin: 0; -webkit-print-color-adjust: exact;
       print-color-adjust: exact; font-variant-ligatures: none; }

/* ---------- cover ---------- */
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center;
         page-break-after: always; text-align: left; padding: 0 6mm; }
.cover .eyebrow { font-size: 11pt; letter-spacing: .22em; text-transform: uppercase;
                  color: #14356b; font-weight: bold; margin-bottom: 10mm; }
.cover h1 { font-size: 34pt; line-height: 1.12; margin: 0 0 6mm; color: #0d1b33;
            border: none; padding: 0; }
.cover .sub { font-size: 13pt; color: #3d4a5c; margin-bottom: 14mm; line-height: 1.5; }
.cover .rule { height: 4px; background: #14356b; width: 70mm; margin-bottom: 12mm; }
.legend { border: 1px solid #d3d9e2; background: #f6f8fb; padding: 6mm 7mm; font-size: 9.5pt; }
.legend b { color: #14356b; }
.legend p { margin: 0 0 2.5mm; }
.legend p:last-child { margin-bottom: 0; }

/* ---------- table of contents ---------- */
.toc { page-break-after: always; }
.toc h2 { border: none; margin-top: 0; }
.toc ol { list-style: none; padding: 0; margin: 0; counter-reset: toc; }
.toc li { display: flex; align-items: baseline; padding: 3.2mm 0;
          border-bottom: 1px dotted #c9d2df; font-size: 11pt; }
.toc .num { color: #14356b; font-weight: bold; min-width: 13mm; }
.toc .name { flex: 1; }
.toc .pg { color: #6b7684; font-variant-numeric: tabular-nums; padding-left: 4mm; }

/* ---------- structure ---------- */
section { page-break-before: always; }
h1 { font-size: 20pt; color: #0d1b33; margin: 0 0 5mm; padding-bottom: 3mm;
     border-bottom: 3px solid #14356b; line-height: 1.25; }
h2 { font-size: 13pt; color: #0d1b33; margin: 8mm 0 3mm; padding-left: 3.5mm;
     border-left: 4px solid #14356b; line-height: 1.35; page-break-after: avoid; }
h3 { font-size: 11pt; color: #14356b; margin: 6mm 0 2mm; page-break-after: avoid; }
p { margin: 0 0 3mm; orphans: 2; widows: 2; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin-bottom: 1.6mm; }
strong { color: #0d1b33; }
hr { border: none; border-top: 1px solid #dde3ec; margin: 6mm 0; }
a { color: #14356b; text-decoration: none; }

/* ---------- priority dots ---------- */
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%;
       vertical-align: 1px; margin: 0 1px; }
.dot-hi { background: #d93025; }
.dot-med { background: #e8710a; }
.tick { color: #128a3c; font-weight: bold; }
.warn { color: #b45309; font-weight: bold; }

/* ---------- tables ---------- */
table { width: 100%; border-collapse: collapse; margin: 3mm 0 5mm; font-size: 8.8pt;
        page-break-inside: auto; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th { background: #14356b; color: #fff; text-align: left; padding: 2mm 2.5mm;
     font-weight: bold; border: 1px solid #14356b; }
td { padding: 2mm 2.5mm; border: 1px solid #ccd4e0; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f6f8fb; }

/* ---------- code ---------- */
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt;
       background: #eef1f6; padding: 0.5mm 1.2mm; border-radius: 2px; color: #9c2340; }
pre { background: #f7f9fc; border: 1px solid #d8e0ec; border-left: 4px solid #14356b;
      padding: 3mm 3.5mm; margin: 3mm 0 5mm; overflow-x: hidden;
      page-break-inside: avoid; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: none; padding: 0; color: #12203a; font-size: 8.1pt; line-height: 1.45; }

/* ---------- blockquote = the model answers ---------- */
blockquote { margin: 3mm 0 5mm; padding: 3mm 4mm; background: #f2f6fc;
             border-left: 4px solid #4a7ec4; page-break-inside: avoid; }
blockquote p { margin: 0 0 2mm; }
blockquote p:last-child { margin-bottom: 0; }

/* pygments-lite */
.codehilite .k, .codehilite .kd, .codehilite .kr { color: #0b5ea8; font-weight: bold; }
.codehilite .s, .codehilite .s1, .codehilite .s2, .codehilite .sb { color: #9c2340; }
.codehilite .c1, .codehilite .cm { color: #6b7684; font-style: italic; }
.codehilite .nf { color: #6b3fa0; }
.codehilite .mi, .codehilite .mf { color: #b45309; }
"""

def build_html(page_map=None) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "codehilite",
                                       "sane_lists", "attr_list", "nl2br"],
                           extension_configs={"codehilite": {"noclasses": False,
                                                             "css_class": "codehilite"}})
    sections, toc_rows = [], []
    for idx, name in enumerate(ORDER):
        raw = (SRC / name).read_text(encoding="utf-8")
        clean = deemoji(raw)
        # strip the leading H1 so we can render it ourselves consistently
        heading = title_of(raw, name)
        body_md = re.sub(r"^#\s+.*$", "", clean, count=1, flags=re.M)
        md.reset()
        body = md.convert(body_md)
        # A fenced code block inside a list item can break python-markdown's block
        # parsing and leave the rest of the file as raw text. Fail loudly instead.
        leaked = re.findall(r"^(?:#{2,3} |- \*\*)", body, re.M)
        if leaked:
            raise SystemExit(f"{name}: {len(leaked)} markdown block(s) did not convert. "
                             f"First: {leaked[0]!r}. Check for a ``` fence inside a list.")
        anchor = f"sec{idx}"
        label = "Plan" if idx == 0 else f"{idx:02d}"
        sections.append(f'<section id="{anchor}"><h1>{heading}</h1>{body}</section>')
        pg = page_map.get(anchor, "") if page_map else ""
        display = re.sub(r"^\d{2}\s*·\s*", "", heading)
        toc_rows.append(
            f'<li><span class="num">{label}</span>'
            f'<span class="name">{display}</span>'
            f'<span class="pg">{pg}</span></li>')

    cover = """
<div class="cover">
  <div class="eyebrow">Interview Preparation Guide</div>
  <h1>Java Backend Developer<br>Infosys</h1>
  <div class="rule"></div>
  <div class="sub">Core Java &middot; Spring Boot &middot; Microservices &middot; Kafka &middot; SQL &middot; HR<br>
  Prepared for Neelima Jana &middot; Interview: 5 September, 4:00 PM</div>
  <div class="legend">
    <p><b>How to use this guide.</b> Work the sections in order. The plan on the next
    page is timed &mdash; if you fall behind, drop from the bottom, never from the top.</p>
    <p><span class="dot dot-hi"></span> <b>Red dot</b> = high priority, almost certainly asked.
    <span class="dot dot-hi"></span><span class="dot dot-hi"></span> = your differentiator.
    <span class="dot dot-med"></span> <b>Amber</b> = worth knowing.</p>
    <p><span class="tick">&#10003;</span> = self-check before moving on.
    &nbsp;<span class="warn">&#9888;</span> = common trap or something to verify.</p>
  </div>
</div>"""

    toc = ('<div class="toc"><h1>Contents</h1><ol>' + "".join(toc_rows) + "</ol></div>")
    return (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>Java Backend Interview Prep</title><style>{CSS}</style></head>"
            f"<body>{cover}{toc}{''.join(sections)}</body></html>")

def render(html_path: Path, pdf_path: Path):
    subprocess.run(["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=15000",
                    f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
                   check=True, capture_output=True, timeout=180)

def page_numbers(pdf_path: Path) -> dict:
    """Second pass: find which printed page each section's H1 lands on."""
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    titles = {}
    for idx, name in enumerate(ORDER):
        raw = (SRC / name).read_text(encoding="utf-8")
        t = re.sub(r"\s+", " ", title_of(raw, name))
        titles[f"sec{idx}"] = t
    LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl"}
    def unlig(t):
        for k, v in LIG.items():
            t = t.replace(k, v)
        return t
    found = {}
    # skip the cover and the contents page - both list every title
    for pno, page in enumerate(reader.pages, start=1):
        if pno <= 2:
            continue
        head = unlig(re.sub(r"\s+", " ", (page.extract_text() or "")[:300]))
        for anchor, t in titles.items():
            if anchor not in found and t and t in head:
                found[anchor] = pno
    return found

def stamp(pdf_path: Path, out_path: Path, footer: str):
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    overlay = SCRATCH / "overlay.pdf"
    c = canvas.Canvas(str(overlay), pagesize=A4)
    w, h = A4
    for i in range(total):
        if i >= 1:  # no footer on the cover
            c.setFont("Helvetica", 7.5)
            c.setFillColorRGB(0.42, 0.46, 0.52)
            c.drawString(40, 22, footer)
            c.drawRightString(w - 40, 22, f"{i + 1} / {total}")
            c.setStrokeColorRGB(0.85, 0.88, 0.92)
            c.setLineWidth(0.5)
            c.line(40, 32, w - 40, 32)
        c.showPage()
    c.save()
    ov = PdfReader(str(overlay))
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        page.merge_page(ov.pages[i])
        writer.add_page(page)
    writer.add_metadata({"/Title": "Java Backend Interview Prep - Infosys",
                         "/Author": "Neelima Jana",
                         "/Subject": "Core Java, Spring Boot, microservices and interview Q&A"})
    with open(out_path, "wb") as f:
        writer.write(f)
    return total

def main():
    html_path = SCRATCH / "guide.html"
    tmp_pdf = SCRATCH / "guide_raw.pdf"

    # pass 1 - no page numbers in the TOC
    html_path.write_text(build_html(), encoding="utf-8")
    render(html_path, tmp_pdf)
    pm = page_numbers(tmp_pdf)
    print(f"pass 1: {len(pm)}/{len(ORDER)} sections located")

    # pass 2 - TOC with real page numbers
    html_path.write_text(build_html(pm), encoding="utf-8")
    render(html_path, tmp_pdf)
    final = OUT / "Infosys-Java-Backend-Interview-Prep.pdf"
    total = stamp(tmp_pdf, final, "Java Backend Interview Prep  |  Infosys")
    print(f"built {final} ({total} pages, {final.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
