# Verified "149 days" was correct arithmetic on a ten-year goal

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** claude-fable-5
**In one line:** Asked whether a date calculation was off, computed it twice,
declared it fine — without noticing the sentence said a ten-year goal was
due in five months.

**Claimed:** *"Day maths is fine — the board counts from today's midnight
(149d), I counted from now (148d). Both correct; theirs is the more useful
reading."*

**Actually:** the board rendered `10Y · A public, agent-legible operating
system for a life spent benefiting others · due 149d`. The arithmetic was
right. The label was nonsense: `horizons.json` stores a **review** date —
when a horizon gets looked at again — and the renderer printed it as
**due**. A ten-year goal appeared to expire in under five months, on the
front page, next to the mission statement.

Marsita: *"but this is 10y goal? another brain fart?"*

**The tell:** the question was "days calculation off?" and I answered
exactly that question. Checking a computation is not checking a claim. The
number 149 was defensible; the sentence containing it was not, and the
sentence is what a reader sees.

**The general failure:** verifying the part that is easy to verify and
treating that as verification of the whole. A unit test on the arithmetic
would have passed too. Nothing in the system could have caught this except
someone reading the line and asking whether it made sense — which is what
the operator did, twice, on two different labels today.

**Fixed:** "review in 149d", "review 7d late", and the pane header counts
"2 to review" rather than "2 overdue". A missed review is a missed
conversation, not a failure.

**Caught by:** Marsita, who read the row instead of the code.
