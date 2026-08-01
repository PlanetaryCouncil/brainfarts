# Drew a box I could not see, wrong by exactly one, twice

**Claimed:** Nothing said — this one is *emitted*. Two consecutive replies closed
with a framed poem whose right rail did not line up. Marsita sent a screenshot:
the vertical bars on the right float outside the box, detached, like a fence
someone put up a step too far from the wall.

**Actually:** Measured after the fact, both boxes have the same defect with
uncanny precision:

```
box (turn n-1)   borders + blank rows: 50   rows with words: 51
box (turn n)     borders + blank rows: 51   rows with words: 52
```

Every row containing text is **exactly one column wider** than every border and
blank row. Not drifting, not random — a constant off-by-one that appears only
when the row carries words. I padded blank rows correctly and text rows to a
target one greater, twice in a row, in boxes of different widths.

**The tell:** It was in my own output, in plain characters, at the moment of
writing. Monospace alignment is arithmetic — `len(line)` — not judgement. Nothing
about it requires seeing; it requires counting, and I never counted. I laid out
each row by eye against a mental column ruler and shipped it.

Worse, `STRAIGHT-HANDOFF.md` contains the line ***"They catch what I cannot see.
Every layout bug this session came from their screenshots."*** I had read that
file at the start of the session and written to it four times since. It names
this failure mode exactly, and it did not fire.

**Shape — visual arithmetic done by eye, in a medium I have no eyes for.** This
is the third visual failure in one session and the three form an escalation worth
naming together:

1. A glyph resolved to a weaker one — `━` where the spec held eighty `█`.
2. The frame dropped entirely — indentation where the spec said *framed*.
3. The frame drawn, and misaligned by one, twice.

Each correction fixed the instance and none generalised, because I kept treating
"how it looks" as something to be recalled rather than something to be computed.
There is no visual channel on my own output. A box does not exist for me the way
it does on screen; it is a string I believe will render as a box. Believing is
the entire problem — every other entry in this log is about a claim I could have
checked, and this is about a *shape* I could have checked, with the same one
command.

The reason it repeated after two corrections about frames specifically: both
corrections were about *whether* to draw the border. Neither was about *how*, so
I fixed the policy and left the method — eyeballing — untouched.

**Bizarre:** 7/10 as a mistake — purely cosmetic, no decision rests on it. Higher
as a category, and the two identical off-by-ones are what make it strange: a
random error would not land on +1 both times. That consistency proves it was a
*method* producing wrong output reliably, not a slip. A reliably wrong method is
worse than a slip, because it will keep being reliably wrong.

**Fix:** Never hand-pad a monospace layout. Build it with code that computes the
width from the longest line, print it, and check every row is equal before
emitting — three lines of Python against an unbounded supply of off-by-ones. More
generally: when an instruction concerns appearance, the deliverable is a rendered
artifact to be verified, never a description to be recalled. Same conclusion as
the entry before it, arrived at from the other side — that one said store the
glyph, this one says compute the geometry.
