#!/usr/bin/env python3
"""Build index.html from entries/*.md.

No dependencies on purpose. The markdown here is a known, narrow subset — the
format is fixed by README.md and every entry follows it — so a small renderer
beats a library that would have to be installed before anyone, human or agent,
could publish a correction.

Usage:  python3 build.py
"""

import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
ENTRIES = ROOT / "entries"
OUT = ROOT / "index.html"

# Fields in the order the format defines them. "The tell" is pulled out of the
# flow and given its own treatment because the README is explicit that it is the
# whole point of an entry.
FIELD_ORDER = ["Claimed", "Actually", "The tell", "Shape", "Bizarre", "Fix"]


# --------------------------------------------------------------------------
# markdown subset
# --------------------------------------------------------------------------

def inline(text: str) -> str:
    """Escape, then re-introduce only the marks the entries actually use."""
    out = html.escape(text, quote=False)
    # Code first: its contents must not be re-processed for emphasis.
    slots: list[str] = []

    def stash(m):
        slots.append(f"<code>{m.group(1)}</code>")
        return f"\x00{len(slots) - 1}\x00"

    out = re.sub(r"`([^`]+)`", stash, out)
    out = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", out, flags=re.S)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out, flags=re.S)
    out = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", out, flags=re.S)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    return re.sub(r"\x00(\d+)\x00", lambda m: slots[int(m.group(1))], out)


def blocks(md: str) -> list[tuple[str, str]]:
    """Split a body into (kind, text) blocks. Kinds: code, ul, ol, p."""
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            out.append(("code", "\n".join(lines[i + 1:j])))
            i = j + 1
        elif re.match(r"^\s*[-*] ", line):
            j = i
            while j < len(lines) and (re.match(r"^\s*[-*] ", lines[j])
                                      or (lines[j].strip() and lines[j].startswith("  "))):
                j += 1
            out.append(("ul", "\n".join(lines[i:j])))
            i = j
        elif re.match(r"^\s*\d+\. ", line):
            j = i
            while j < len(lines) and (re.match(r"^\s*\d+\. ", lines[j])
                                      or (lines[j].strip() and lines[j].startswith("   "))):
                j += 1
            out.append(("ol", "\n".join(lines[i:j])))
            i = j
        elif not line.strip():
            i += 1
        else:
            j = i
            while (j < len(lines) and lines[j].strip()
                   and not lines[j].startswith("```")
                   and not re.match(r"^\s*([-*]|\d+\.) ", lines[j])):
                j += 1
            out.append(("p", " ".join(l.strip() for l in lines[i:j])))
            i = j
    return out


def items(text: str, marker: str) -> str:
    """Join wrapped list items back together before rendering them."""
    out, cur = [], ""
    for line in text.split("\n"):
        if re.match(marker, line):
            if cur:
                out.append(cur)
            cur = re.sub(marker, "", line).strip()
        else:
            cur += " " + line.strip()
    if cur:
        out.append(cur)
    return "".join(f"<li>{inline(x)}</li>" for x in out)


def render(md: str) -> str:
    parts = []
    for kind, text in blocks(md):
        if kind == "code":
            parts.append(f"<pre><code>{html.escape(text)}</code></pre>")
        elif kind == "ul":
            parts.append(f"<ul>{items(text, r'^\s*[-*] ')}</ul>")
        elif kind == "ol":
            parts.append(f"<ol>{items(text, r'^\s*\d+\. ')}</ol>")
        else:
            parts.append(f"<p>{inline(text)}</p>")
    return "\n".join(parts)


# --------------------------------------------------------------------------
# entry parsing
# --------------------------------------------------------------------------

def parse(path: pathlib.Path) -> dict:
    raw = path.read_text().strip()
    lines = raw.split("\n")
    if not lines[0].startswith("# "):
        sys.exit(f"{path.name}: expected a '# Title' on line 1")
    entry = {
        "slug": path.stem,
        "date": path.stem[:10],
        "title": lines[0][2:].strip(),
        "fields": {},
        "order": [],
    }

    body = "\n".join(lines[1:])
    # Two forms are in use and both must parse. `**Label:**` is the documented
    # one; `**Label — a claim about this entry.**` appears where the shape was
    # worth stating in the heading itself. Matching only the first silently fed
    # four entries' Shape text into the preceding field, which happened to be
    # the one the page pulls out and highlights — so a parser miss here shows up
    # as wrong content, not as a missing section.
    marks = list(re.finditer(
        r"^\*\*([A-Z][A-Za-z ]{1,24}?)(?::\*\*|\s*—\s*([^*]*)\*\*)\s*", body, re.M))
    for n, m in enumerate(marks):
        label = m.group(1).strip()
        stop = marks[n + 1].start() if n + 1 < len(marks) else len(body)
        text = body[m.end():stop].strip()
        if m.group(2):                      # keep the heading's own subtitle
            text = f"**{m.group(2).strip()}** {text}"
        entry["fields"][label] = text
        entry["order"].append(label)

    entry["reporter"] = entry["fields"].pop("Reporter", "unknown").strip()
    entry["type"] = entry["fields"].pop("Type", "human").strip().lower()
    for key in ("Reporter", "Type"):
        if key in entry["order"]:
            entry["order"].remove(key)

    score = re.search(r"(\d+)\s*/\s*10", entry["fields"].get("Bizarre", ""))
    entry["score"] = int(score.group(1)) if score else None
    return entry


def field_html(entry: dict) -> str:
    seen = list(entry["order"])
    ordered = [f for f in FIELD_ORDER if f in seen] + [f for f in seen if f not in FIELD_ORDER]
    out = []
    for label in ordered:
        text = entry["fields"][label]
        # "Shape" sometimes carries its own em-dash subtitle in the label; the
        # regex already stripped it, so the label renders uniformly here.
        key = label.lower().replace(" ", "-")
        out.append(
            f'<div class="field field--{key}">'
            f'<div class="field__label">{html.escape(label)}</div>'
            f'<div class="field__body">{render(text)}</div>'
            f"</div>"
        )
    return "\n".join(out)


def meter(score) -> str:
    if score is None:
        return '<span class="score score--none">—</span>'
    ticks = "".join(
        f'<i class="{"on" if i < score else ""}"></i>' for i in range(10)
    )
    return (
        f'<span class="score" data-score="{score}">'
        f'<span class="score__n">{score}</span>'
        f'<span class="score__bar" aria-hidden="true">{ticks}</span>'
        f'<span class="score__d">/10</span></span>'
    )


# --------------------------------------------------------------------------
# page
# --------------------------------------------------------------------------

CSS = """
:root{
  --ground:#F7F8F6; --surface:#FFFFFF; --sunk:#F1F3EF;
  --ink:#15181B; --ink-2:#3D444B; --muted:#6C737A;
  --rule:#E3E6E2; --rule-2:#CFD4CE;
  --accent:#2F4B7C; --signal:#9C6B18; --signal-soft:#F3EBDB;
  --measure:34rem;
  --serif:"Newsreader",ui-serif,Charter,"Iowan Old Style",Georgia,serif;
  --sans:"IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme:dark){
  :root{
    --ground:#101316; --surface:#161A1D; --sunk:#1B2024;
    --ink:#E7EAE6; --ink-2:#BFC6C9; --muted:#8B939A;
    --rule:#252A2E; --rule-2:#333A3F;
    --accent:#9DB7E2; --signal:#D6A855; --signal-soft:#241E12;
  }
}
:root[data-theme="dark"]{
  --ground:#101316; --surface:#161A1D; --sunk:#1B2024;
  --ink:#E7EAE6; --ink-2:#BFC6C9; --muted:#8B939A;
  --rule:#252A2E; --rule-2:#333A3F;
  --accent:#9DB7E2; --signal:#D6A855; --signal-soft:#241E12;
}
:root[data-theme="light"]{
  --ground:#F7F8F6; --surface:#FFFFFF; --sunk:#F1F3EF;
  --ink:#15181B; --ink-2:#3D444B; --muted:#6C737A;
  --rule:#E3E6E2; --rule-2:#CFD4CE;
  --accent:#2F4B7C; --signal:#9C6B18; --signal-soft:#F3EBDB;
}

*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:var(--sans); font-size:16.5px; line-height:1.62;
  -webkit-font-smoothing:antialiased; font-synthesis-weight:none;
}
.wrap{max-width:var(--measure); margin:0 auto; padding:0 1.5rem;}
a{color:var(--accent); text-underline-offset:.18em; text-decoration-thickness:.06em;}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent); outline-offset:3px; border-radius:2px;}

/* ---------- masthead ---------- */
.mast{padding:5.5rem 0 3rem; border-bottom:1px solid var(--rule);}
.mast__eyebrow{
  font-family:var(--mono); font-size:.7rem; letter-spacing:.16em;
  text-transform:uppercase; color:var(--muted); margin:0 0 1.6rem;
}
.mast h1{
  font-family:var(--serif); font-weight:400; font-size:clamp(2.6rem,7vw,3.9rem);
  line-height:1.04; letter-spacing:-.018em; margin:0 0 1.4rem; text-wrap:balance;
}
.mast h1 em{font-style:italic; color:var(--signal);}
.mast__lede{font-size:1.12rem; color:var(--ink-2); margin:0 0 1.1rem; text-wrap:pretty;}
.mast__lede strong{font-weight:600; color:var(--ink);}
.mast__note{font-size:.94rem; color:var(--muted); margin:0;}

/* ---------- section furniture ---------- */
.sec{padding:3.2rem 0; border-bottom:1px solid var(--rule);}
.sec__h{
  font-family:var(--mono); font-size:.7rem; letter-spacing:.16em;
  text-transform:uppercase; color:var(--muted); margin:0 0 1.5rem;
  display:flex; align-items:baseline; gap:.7rem;
}
.sec__h::after{content:""; flex:1; height:1px; background:var(--rule);}
.sec p{margin:0 0 1rem; text-wrap:pretty;}
.sec p:last-child{margin-bottom:0;}

/* ---------- register ---------- */
.reg{width:100%; border-collapse:collapse; font-size:.9rem;}
.reg caption{text-align:left; color:var(--muted); font-size:.86rem; padding-bottom:.9rem;}
.reg th{
  font-family:var(--mono); font-size:.64rem; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted); font-weight:500;
  text-align:left; padding:0 .7rem .55rem 0; border-bottom:1px solid var(--rule-2);
}
.reg th.num{text-align:right; padding-right:0;}
.reg td{padding:.62rem .7rem .62rem 0; border-bottom:1px solid var(--rule); vertical-align:baseline;}
.reg td:last-child{padding-right:0;}
.reg tr:last-child td{border-bottom:none;}
.reg .d{font-family:var(--mono); font-size:.76rem; color:var(--muted); white-space:nowrap;
  font-variant-numeric:tabular-nums;}
.reg .t a{color:var(--ink); text-decoration:none; border-bottom:1px solid transparent;}
.reg .t a:hover{border-bottom-color:var(--accent); color:var(--accent);}
.reg .s{text-align:right; white-space:nowrap;}

/* ---------- score ---------- */
.score{display:inline-flex; align-items:center; gap:.42rem; font-family:var(--mono);
  font-variant-numeric:tabular-nums;}
.score__n{font-size:.92rem; font-weight:600; color:var(--ink);}
.score__d{font-size:.68rem; color:var(--muted);}
.score__bar{display:inline-flex; gap:1.5px;}
.score__bar i{width:3px; height:11px; background:var(--rule-2); border-radius:.5px;}
.score__bar i.on{background:var(--signal);}
.score[data-score="9"] .score__n,.score[data-score="10"] .score__n{color:var(--signal);}
.score--none{color:var(--muted); font-family:var(--mono);}

/* ---------- entries ---------- */
.entry{padding:3.4rem 0; border-bottom:1px solid var(--rule);}
.entry:target .entry__title{color:var(--accent);}
.entry__meta{
  display:flex; flex-wrap:wrap; align-items:center; gap:.55rem .85rem;
  font-family:var(--mono); font-size:.7rem; letter-spacing:.05em;
  color:var(--muted); margin-bottom:.95rem;
}
.entry__meta .dot{width:3px; height:3px; border-radius:50%; background:var(--rule-2);}
.entry__date{font-variant-numeric:tabular-nums;}
.badge{
  border:1px solid var(--rule-2); border-radius:2px; padding:.1rem .38rem;
  letter-spacing:.11em; text-transform:uppercase; font-size:.62rem;
}
.badge--agent{border-color:var(--accent); color:var(--accent);}
.entry__perma{margin-left:auto; color:var(--muted); text-decoration:none; opacity:0; transition:opacity .12s;}
.entry:hover .entry__perma,.entry__perma:focus-visible{opacity:1;}
.entry__title{
  font-family:var(--serif); font-weight:400; font-size:clamp(1.6rem,3.6vw,2.05rem);
  line-height:1.16; letter-spacing:-.012em; margin:0 0 1.9rem; text-wrap:balance;
}

.field{margin-bottom:1.55rem;}
.field:last-child{margin-bottom:0;}
.field__label{
  font-family:var(--mono); font-size:.63rem; letter-spacing:.15em;
  text-transform:uppercase; color:var(--muted); margin-bottom:.42rem;
}
.field__body p{margin:0 0 .85rem; text-wrap:pretty;}
.field__body p:last-child{margin-bottom:0;}
.field__body ul,.field__body ol{margin:.55rem 0 .85rem; padding-left:1.15rem;}
.field__body li{margin-bottom:.4rem;}
.field__body li::marker{color:var(--muted);}

/* The tell is the load-bearing part of an entry — the README says so outright.
   It gets the one piece of colour on the page that is not a link. */
.field--the-tell{
  background:var(--signal-soft); border-left:2px solid var(--signal);
  padding:1.05rem 1.2rem; border-radius:0 3px 3px 0;
}
.field--the-tell .field__label{color:var(--signal);}
.field--bizarre .field__body,.field--fix .field__body{color:var(--ink-2);}

code{
  font-family:var(--mono); font-size:.86em; background:var(--sunk);
  padding:.1em .32em; border-radius:2.5px; border:1px solid var(--rule);
}
pre{
  background:var(--sunk); border:1px solid var(--rule); border-radius:3px;
  padding:.85rem 1rem; overflow-x:auto; margin:.85rem 0;
}
pre code{background:none; border:none; padding:0; font-size:.79rem; line-height:1.55;}

/* ---------- foot ---------- */
.foot{padding:3rem 0 5rem; font-size:.88rem; color:var(--muted);}
.foot p{margin:0 0 .6rem;}

@media (max-width:32rem){
  body{font-size:16px;}
  .mast{padding:3.5rem 0 2.4rem;}
  .reg .s .score__bar{display:none;}
}
@media (prefers-reduced-motion:reduce){
  *{transition:none !important; animation:none !important;}
}
"""

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    "family=IBM+Plex+Mono:wght@400;500;600&"
    "family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&"
    'family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,400&display=swap">'
)


def build() -> str:
    files = sorted(ENTRIES.glob("*.md"), reverse=True)
    if not files:
        sys.exit("no entries found")
    entries = [parse(f) for f in files]

    scored = [e["score"] for e in entries if e["score"] is not None]
    n_human = sum(1 for e in entries if e["type"] == "human")

    rows = "\n".join(
        f'<tr><td class="d">{e["date"]}</td>'
        f'<td class="t"><a href="#{e["slug"]}">{html.escape(e["title"])}</a></td>'
        f'<td class="s">{meter(e["score"])}</td></tr>'
        for e in entries
    )

    body = "\n".join(
        f'<article class="entry" id="{e["slug"]}">'
        f'<div class="wrap">'
        f'<div class="entry__meta">'
        f'<span class="entry__date">{e["date"]}</span><span class="dot"></span>'
        f'<span>{html.escape(e["reporter"])}</span>'
        f'<span class="badge badge--{html.escape(e["type"])}">{html.escape(e["type"])}</span>'
        f'<a class="entry__perma" href="#{e["slug"]}" aria-label="Link to this entry">#</a>'
        f"</div>"
        f'<h2 class="entry__title">{html.escape(e["title"])}</h2>'
        f"{field_html(e)}"
        f"</div></article>"
        for e in entries
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI brain farts — a log of confidently wrong answers</title>
<meta name="description" content="A log of confidently wrong things AI assistants have said, and the evidence already on screen that contradicted them. {len(entries)} entries.">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="AI brain farts">
<meta property="og:description" content="Confidently wrong AI answers, and the evidence already on screen that contradicted them.">
<meta property="og:type" content="website">
{FONTS}
<style>{CSS}</style>
</head>
<body>

<header class="mast">
  <div class="wrap">
    <p class="mast__eyebrow">A log kept since 30 July 2026</p>
    <h1>AI brain farts, and the evidence <em>already on screen</em></h1>
    <p class="mast__lede">Confidently wrong things AI assistants have told me &mdash; and
      the part that actually matters: <strong>what was checkable at the time, and what
      would have caught it.</strong></p>
    <p class="mast__note">Not a blooper reel. A wrong answer that sounds uncertain is
      harmless; you go and check. A wrong answer delivered with confidence installs a
      false model in your head and stays there until something breaks. Those have shapes,
      and the shapes repeat.</p>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <h2 class="sec__h">The register</h2>
    <table class="reg">
      <caption>{len(entries)} entries, newest first. The number is how bizarre the
        mistake was, not how costly &mdash; 9 and 10 mean the contradicting evidence was
        visible on screen at the moment of speaking.</caption>
      <thead><tr><th>Date</th><th>Entry</th><th class="num">Bizarre</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="sec__h">What keeps happening</h2>
    <p>Most of these are not knowledge failures. The model usually <em>had</em> the
      disconfirming evidence &mdash; in the terminal output, in a screenshot, earlier in
      the same conversation &mdash; and did not check its claim against it.</p>
    <p>Two invented a cause rather than saying &ldquo;I don&rsquo;t know why.&rdquo; Two
      were errors of judgement rather than fact, which cost the most and are hardest to
      catch, because nothing is technically false. One chose a number because it made a
      sentence scan. One narrowed a query, then read the hole it had made as evidence.
      Three were a visual instruction rendered too weakly, escalating across a single
      session.</p>
    <p>The habit implied: before asserting a cause or a quantity, ask what would be true
      if the claim were false, and whether that is visible right now. Ask also whether the
      view you are reading is one you narrowed yourself &mdash; and when the instruction
      is about appearance, render and measure rather than recall.</p>
  </div>
</section>

<main>
{body}
</main>

<footer class="foot">
  <div class="wrap">
    <p>Every entry records who caught it. All {n_human} so far were caught by a human,
      usually within a turn or two of the mistake.</p>
    <p>That is expected to change. A log that stays entirely human-reported is measuring
      how good the human is, not how good the agents are.</p>
  </div>
</footer>

</body>
</html>
"""


if __name__ == "__main__":
    OUT.write_text(build())
    n = len(list(ENTRIES.glob("*.md")))
    print(f"wrote {OUT.relative_to(ROOT)} — {n} entries")
