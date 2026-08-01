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

Nine entries, and the errors are not distributed randomly:

- **Seven of nine had the disconfirming evidence already visible** — in a
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

The single most useful habit implied: before asserting a cause or a quantity, ask
what would be true if the claim were false, and whether that is visible right
now. In seven of nine cases, it was — and in the sharpest one the evidence was in
a log file the machine had written itself, hour by hour, and never read.
