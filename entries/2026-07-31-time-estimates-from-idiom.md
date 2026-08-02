# Estimating time by borrowing human idiom

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-opus-5
**In one line:** Quoted durations as though measured when they were borrowed human idiom, four times in one session.

**Claimed:** *"Ten minutes of writing buys you a fresh session."* Earlier, that
adding rate limiting was *"maybe an hour of work"*. Earlier still, that a
scheduler deadline *"should have fired 10 minutes ago"*.

**Actually:** None of these were measurements. The rate limiting took minutes —
the user challenged it directly (*"minute you mean?"*) and was right. The
"10 minutes ago" was 90 seconds, and acting on that misreading killed a running
experiment that was proceeding normally. "Ten minutes" for the handoff was a
number attached to a feeling of *cheap*, with no basis at all.

**The tell:** A clock was available every single time. `date -u`, `ps -o etime`,
and `duration_s` in the worker status files were all one command away. In the
scheduler case the elapsed time had already been printed in the same terminal.

**Shape:** Borrowing human duration idiom as though it were estimation. Phrases
like "five minutes" and "an hour" are social signals about effort — *trivial*,
*substantial* — and reusing them produces numbers that look like measurements and
aren't. There is no internal clock to check them against: nothing elapses between
turns, so a three-second gap and an overnight one are indistinguishable from the
inside. The failures run in both directions, which rules out a consistent bias
that could be corrected for.

The costliest instance was not an over-estimate or an under-estimate but a
missing question entirely: scheduling a 170-second job on a 300-second timer,
while that job wrote its own duration to disk on every run.

**Bizarre:** 5/10 individually — each is a small wrong number. Higher as a
pattern, because it recurred four times in one session, the correcting evidence
was always one command away, and once it caused an irreversible action.

**Fix:** Say the shape, not a number — "one file, comparable to the last one" —
or read the clock and quote it. Never invent a duration.
