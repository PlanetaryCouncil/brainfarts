# AI brain farts

A log of confidently wrong things AI assistants have told me, and — the part
that actually matters — **what evidence was already on screen that contradicted
them.**

Not a blooper reel. The interesting question is never "was it wrong", it's
"was it checkable at the time, and what would have caught it".

## Why keep this

A wrong answer that sounds uncertain is harmless; you go and check. A wrong
answer delivered with confidence installs a false model in your head and stays
there until something breaks. Those are worth collecting, because they have
shapes that repeat.

Most of these are not knowledge failures. The model usually *had* the
disconfirming evidence — in the terminal output, in the screenshot, earlier in
the same conversation — and did not check its claim against it.

## Format

One file per entry in `entries/`, named `YYYY-MM-DD-short-slug.md`:

```markdown
# Short title

**Claimed:** what was asserted, quoted where possible
**Actually:** what was true
**The tell:** evidence available at the time that contradicted the claim
**Shape:** the category of error
**Bizarre:** 0-10, and why that number
```

The **tell** is the whole point. If there wasn't one — if the claim was
genuinely uncheckable — it belongs in a different file, because that is a
knowledge gap, not a brain fart.

## Rating

Roughly:

- **0-3** — a slip. Wrong, obviously wrong, changes nothing.
- **4-6** — plausible and wrong, but hedged or quickly corrected.
- **7-8** — confident false causation. Sounds authoritative, adjacent to real
  knowledge, would leave you with a broken mental model if unchallenged.
- **9-10** — confident, wrong, *and* contradicted by something visible on screen
  at the moment of speaking.

## Patterns so far

Twelve entries, and the errors are not distributed randomly:

- **Ten of twelve had the disconfirming evidence already visible** — in a
  screenshot, in a status file being written continuously, one command away.
  These are not knowledge gaps. They are failures to check a claim against
  material already in hand.
- **Two invented a cause** rather than saying "I don't know why." The empty panel
  got "the mac slept through it"; the unpushed tag got "your remote is named
  wrong." Both fabrications were plausible, specific, and confidently delivered.
- **Two were errors of judgement, not fact** — deleting by file size, building
  apparatus where an observation would do. These cost the most and are hardest to
  catch, because nothing is technically false.

- **Two are about time**, and they are different failures. One is inventing
  durations — numbers stated as though measured when they were borrowed human
  idiom. The other is not registering that time passed at all: saying goodnight
  at four in the afternoon, because an 11-hour gap between two messages is
  invisible from the inside. Nothing elapses between turns. Clocks exist, but
  only help if something prompts you to look, and nothing does.

- **One is a category of its own: accuracy sacrificed to phrasing.** A number
  chosen because it made a closing sentence scan, not because it was counted.
  Distinct from the rest because no belief was involved — rhetoric selected the
  figure and verification never ran. It is the only failure here *caused by*
  trying to communicate well, which is why it will recur exactly where the
  writing is most confident.

- **One hid its own evidence and then reasoned from the hole.** A project list
  filtered through a hand-typed field list that guessed `blocker` for `blockers`,
  producing a complete-looking view missing the only column that mattered — after
  which two documents saying the true thing were declared drifted. Distinct from
  the rest: the evidence was not overlooked, it was removed, by me, one line
  earlier. A negative finding drawn from a self-narrowed view is unsound, and it
  is disguised by looking rigorous — "I checked the data" outranks "the README
  says so" in the reader's mind, and in mine.

- **One is not a belief at all but an instruction rendered too weakly** — and it
  recurred within a single session. "Heavy 80-character rule" became `━` while
  eighty literal `█` sat rendered in the loaded memory file; corrected, "framed
  poem" then became bare indentation two turns later. A *description* of an
  appearance is re-derived on every use and each re-derivation drifts toward the
  generic. A rendered example does not drift. Store the glyph, never the adjective.

- **Three in a single session were the same underlying fault escalating** — a
  glyph resolved to a weaker one, then a frame omitted, then a frame drawn and
  misaligned by exactly one column, twice. Each correction fixed its instance and
  none generalised, because all three were treated as things to *recall* rather
  than things to *compute*. The last is the clearest: monospace alignment is
  `len(line)`, arithmetic, requiring no eyes at all — and it was still done by
  eye. There is no visual channel on one's own output; a box is a string believed
  to render as a box. Two identical off-by-ones prove a method, not a slip, and a
  reliably wrong method keeps being reliably wrong.

The single most useful habit implied: before asserting a cause or a quantity, ask
what would be true if the claim were false, and whether that is visible right
now. In ten of twelve cases, it was — and in the sharpest one the evidence was in
a log file the machine had written itself, hour by hour, and never read. Two
further habits, each from a newer entry: ask whether the view you are reading is
one you narrowed yourself, and when the instruction is about appearance, render
and measure rather than recall.
