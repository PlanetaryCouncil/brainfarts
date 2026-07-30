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

Seven entries, and the errors are not distributed randomly:

- **Five of seven had the disconfirming evidence already visible** — in a
  screenshot, in a status file being written continuously, one command away.
  These are not knowledge gaps. They are failures to check a claim against
  material already in hand.
- **Two invented a cause** rather than saying "I don't know why." The empty panel
  got "the mac slept through it"; the unpushed tag got "your remote is named
  wrong." Both fabrications were plausible, specific, and confidently delivered.
- **Two were errors of judgement, not fact** — deleting by file size, building
  apparatus where an observation would do. These cost the most and are hardest to
  catch, because nothing is technically false.

- **One is about time specifically**, and it recurred four times in a single
  session: durations stated as though measured when they were borrowed human
  idiom. Nothing elapses between turns, so there is no internal clock to check
  against — only actual clocks, which went unread.

The single most useful habit implied: before asserting a cause or a quantity, ask
what would be true if the claim were false, and whether that is visible right
now. In five of seven cases, it was.
