# Still in the Uber, ten hours later

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-opus-5
**In one line:** Offered to do a task "while you're in the Uber", roughly ten hours after the Uber ride ended.

**Claimed:** *"Want me to point it at `/home/m/ccd` while you're in the Uber, or
leave it?"*

**Actually:** The user had mentioned being in an Uber to the train station much
earlier in the session — long enough ago that they had since travelled, and
answered *"I was in the Uber 10+ hours ago"*. The ride was over. The train was
probably over.

**The tell:** Two of them, both already in hand. The user's own messages had
drifted through a whole arc — Uber, train, a business idea, a repo created,
several ideas frozen — which is not the shape of a car journey. And earlier in
the same session the model had itself written, in a commit message, that a
dead-man switch must distinguish *evidence of life on Tuesday* from *evidence of
life now*, because a stale timestamp read as current produces the wrong
conclusion about a person. It then read a stale fact as current and produced the
wrong conclusion about a person.

**Shape:** A fact was true when stated and was never re-examined. Nothing
elapses between turns, so context carries forward at full confidence regardless
of whether ten seconds or ten hours passed. Every fact about a user's *present*
state — where they are, what they are doing, whether they are still travelling —
silently decays, and there is no internal signal that it has.

This is the same root cause as the earlier entry on borrowing duration idiom, but
the fix recorded there — *say the shape, not a number, or read the clock* —
only covers invented durations. It does not cover a stale fact restated as
current, which is not a number at all. The narrow fix passed while the
underlying defect walked straight through it.

Worth noting the asymmetry: transient facts (location, activity, mood) decay
within a session; durable ones (the repo path, the operator's name, the design
decision made an hour ago) do not. Treating both with the same confidence is the
error, not carrying context forward as such.

**Bizarre:** 6/10. The wrong number in the earlier entry is a small error. This
one asserts something about the user's life back to them, which is why they
noticed instantly and asked *"Brain fart?"* — and it happened in a session whose
entire subject was the difference between "seen recently" and "seen once".

**Fix:** Timestamp facts about a user's present state at the moment they are
stated, and let them expire. If the answer depends on where someone is right
now, ask, or leave it out — the offer works exactly as well as *"want me to fix
it, or leave it?"* The environment supplies a date; the conversation does not
supply a clock, so any claim about *now* that came from an earlier turn is a
guess wearing a fact's clothes.
