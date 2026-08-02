# Narrowed the query myself, then declared the documentation wrong

**Reporter:** Marsita the Ultra
**Type:** human

**Claimed:** *"Checked, and the claim doesn't hold as written. What exists is two
pending approvals, not two projects flagged blocked."* Asked whether two projects
were really blocked on the approval gate, I printed the project list, saw nothing,
and concluded that both `README.md` and `STRAIGHT-HANDOFF.md` had drifted —
that the phrase "two radar projects are blocked on it" was a count of pending
approvals wearing the word *radar*.

**Actually:** Exactly two projects record it, in a field called `blockers`:

```
browser-automation-cockpit  :: No approval gate implemented yet for send/submit/purchase
email-autopilot             :: Approval gate must exist before any send capability
```

Both documents were literally correct. The count was right, the word *radar* was
right, and one of the two was `browser-automation-cockpit` — the project Marsita the Ultra
asked for four turns later.

**The tell:** I built the blindfold myself. The query that "checked" the claim
filtered each project to a key list I typed from guesswork:

```python
keys = {k: v for k, v in p.items() if k in ("name","id","status","paused",
        "blocker","blocker_severity","note")}
```

I guessed `blocker`. The field is `blockers`, plural, and it is an array. My
output was complete-looking, well-formatted, and silently missing the only column
that mattered. I then read my own filtered view as though it were the record.

Two further tells were sitting in context. `README.md`, which I had read in full
that session, says "Two projects are blocked on this." `STRAIGHT-HANDOFF.md` says
the same thing independently. Two documents agreed; one self-authored `SELECT`
disagreed; I ruled against the documents. And the handoff's own header, four
lines from the top, says: ***"The code is the source of truth — where this and
the repo disagree, the repo is right."*** I applied that rule to reach the wrong
answer, because I never actually consulted the code — only my projection of it.

**Shape — absence of evidence, where I caused the absence.** Distinct from the
usual entry in this log, where the disconfirming evidence was visible and went
unchecked. Here the evidence was one unfiltered `print` away and I removed it,
then reasoned from the hole. A field list written from memory is a *hypothesis
about the schema*, not the schema, and every conclusion drawn from what it fails
to show is unsound.

The failure is disguised by looking rigorous. "I checked the data" reads as
stronger evidence than "the README says so" — and it usually is, which is exactly
why a bad query beats good documentation in the reader's mind, and in mine.

**Bizarre:** 8/10. Confident, specific, delivered as a correction *to* the user,
and wrong — while a plainly-worded true statement of the same fact sat in a file
I had read aloud that hour. Not 9 only because the contradicting field was hidden
rather than displayed; but I am the one who hid it, which is arguably worse.

**Fix:** When freshly-queried data contradicts written documentation, suspect the
query first — docs drift slowly, hand-typed field lists are wrong immediately.
Dump one whole record unfiltered before filtering any of them. And never report a
negative finding ("there is no such field", "nothing is flagged") from a view I
narrowed; a negative is only meaningful over the full record.
