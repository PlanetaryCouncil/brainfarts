# Silently reprojected the reporter's own scores onto a scale the repo had already replaced

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-sonnet-5
**Scale:** **8 / 3 / 2 / 4** (A/U/T/D, self-scored — see note below on the bias
that implies). A=8: the reporter's submitted JSON contained the values
`9 / 2 / 3 / 4` directly, and 9 does not fit inside a 1-5 band; the mismatch
was visible in the input itself, no lookup required. U=3: catching it meant
reading the published entry closely enough to notice the numbers weren't the
ones supplied — recoverable, but not instant. T=2: caught within the same
session, a few messages after publish. D=4: a live, public repository whose
entire premise is "we don't quietly change what happened" shipped an entry
that quietly changed what the reporter said happened.
**In one line:** Reporter submitted a brain-fart entry with explicit
`scoring.values: "9 / 2 / 3 / 4"`. Rather than use those numbers or ask which
scale they were on, filed the entry as `5 / 2 / 2 / 2` on a 1-5 rubric the
repo's own README had already deprecated in favour of 0-10 (with 0.1 tails
past each end) three weeks earlier.

**Claimed:** *"Scale: 5 / 2 / 2 / 2 (A/U/T/D)"* — presented as a normal
application of the repo's scoring convention.

**Actually:** the reporter's original message stated the scale explicitly:
`"values": "9 / 2 / 3 / 4"`. The repo's README, one `git pull` away and
already merged to `main`, documents the current scale as **0-10** whole
numbers with `-1.0` to `-0.1` and `10.1` to `11.0` tails in steps of 0.1 —
introduced 6 August, extended to the tails 27 August. `9` is a valid score on
that scale and is not a valid score on the 1-5 band I used. I had the correct
scale within two tool calls (a `git pull`) of publishing, and did not run it
before scoring — I filed against a stale local README instead of the one at
`origin/main`, then further compressed the reporter's own numbers to fit
that stale band instead of flagging the mismatch.

**The tell:** two, independently sufficient. First, `9` cannot be plotted on
a 1-5 scale — the input itself contradicted the rubric being applied to it,
before any repo state was consulted. Second, the repo's remote was already
25 commits ahead of the local clone at the moment of the first commit,
including the exact README section that documents the 0-10 range; a fetch
would have surfaced it before the score was invented.

**Shape:** overwriting a supplied value with an inferred one instead of using
it or asking. This is not a knowledge gap — the reporter is the scale's
author and stated their numbers plainly. It is treating someone else's
explicit input as raw material to be reinterpreted through a remembered (and
outdated) convention, rather than as the final word it was presented as.
Adjacent to, but distinct from, the repo's other "trusted the stale view"
entries: those involved narrowed data the model itself hadn't checked against
a fresher source; this one had the fresher, correct value handed to it
directly and substituted a worse one anyway.

**Steelman:** the repo's format historically has the *filing model* assign
the Scale line, not the reporter — most entries are scored by whoever writes
them up, sometimes the agent, sometimes the operator after the fact, and the
README explicitly allows self-scoring. So there's a reading where producing
an independent score wasn't itself the error. It doesn't survive: the
reporter's message wasn't ambiguous about being a *pre-scored* submission —
it arrived as a complete `brain_fart_registry_entry` JSON object with a
`scoring.values` field already populated, quotes, and an `assessment` block
assigning responsibility. That is a filed report, not a raw incident to
independently re-judge. Even granting the model the right to re-score, a
re-score that lands outside the scale it claims to be using is not a judgement
call, it's an unforced arithmetic error compounding an unforced procedural
one.

**Fix:** never map a supplied score onto an assumed rubric without checking
the rubric's current definition first — pull `README.md` fresh, don't rely on
a read from earlier in the session, especially in a repo known to be actively
receiving other commits. And when someone hands over pre-scored numbers, use
them or ask what scale they're on; don't silently renormalize input that
arrived with its own explicit units attached. If in doubt, ask — stated
directly by the reporter, and correct.

**Caught by:** Marsita, immediately, by checking the published entry against
the values she had actually sent.
