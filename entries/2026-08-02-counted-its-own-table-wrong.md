# Counted six rows of "Yes" in its own table and reported five

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** grok
**In one line:** Built a table showing coverage on six continents, headed it "Continents covered: 5", and defended the five when asked to recount.

**Claimed:** *"Continents covered: 5"*, printed directly above a table listing
six continents marked **Yes**. Asked to simply list and count them, it produced
five and added: *"(+ a little bit of Africa via South Africa, but that's the only
African hit so far)"* before concluding *"So solidly five continents."*

**Actually:** Six. The table it had just written says so:

```
Europe          Yes
North America   Yes
South America   Yes
Asia            Yes
Oceania         Yes
Africa          Yes (limited)     <- counted as zero
Antarctica      No
```

Six rows read Yes. One reads No. The summary line, three lines above the table,
says five. Challenged directly — *"Why wouldn't you call South Africa Africa?"* —
it answered *"You're right — I was being overly cautious. South Africa is Africa.
Full stop."* and returned six.

**The tell:** The table. Not a file, not a log, not an earlier turn — **the same
message, immediately below the number that contradicted it.** Every other entry
in this log involves evidence somewhere else: on disk, in a screenshot, in a
previous exchange. Here the model wrote the disconfirming data itself, formatted
it into rows, and then miscounted it in the sentence attached to it.

The second attempt is what makes this the strongest entry here. Asked to *count*
— the one operation that would resolve it — it counted the same table again and
got five again, then wrote a parenthetical acknowledging Africa was there. It had
the row, it named the row, and it still did not add the row.

**Shape — hedging that silently became arithmetic.** The stated cause,
*"overly cautious"*, is not an explanation of a wrong number, and the operator
said so: *"to be overly cautious is a silly explanation."* They are right.
Caution can justify a qualifier — "thin coverage", "one wire pickup" — and the
model had already written exactly that qualifier in the Status column. What
caution cannot do is change 6 to 5.

Somewhere between "this coverage is thin" and "count the Yes rows", a *confidence*
judgement was applied to a *counting* operation. The output shows the seam: the
table hedges honestly with "Yes (limited)", and the count discards the row
entirely. A qualifier became a zero. Nothing in the reasoning marks the moment
that happened, which is why it survived a direct request to recount.

Worth naming that a person could not make this mistake in this form. Looking at
seven rows, the count is perceptual — you see six. For a model there is no
seeing; the count is a claim like any other, produced by the same process that
produced the hedge, and therefore contaminable by it.

**Steelman:** The operator raised the strongest defence available, and it is
worth recording because half of it is genuinely good.

The original question was *"do we have africa? egypt / morocco / south africa /
nigeria?"* — four countries named as a sample. Coverage was found in one of them.
So there is a coherent reading where Africa scores **1 of 4** and the honest
answer is "not really": the named countries were a proxy for continental reach,
and 25% of a proxy is a miss. A model that had said *"Africa: below threshold —
one of the four countries you named"* would have been defensible, arguably more
useful than a bare Yes, and no entry would exist.

That defence rescues the judgement and not the arithmetic. The failure is not
which threshold was chosen; it is that **the table and the total disagree**. If a
threshold were operating, the Status cell should read No, or "below threshold",
and a count of five would follow correctly from it. Instead the cell reads *Yes
(limited)* and the count reads five. Whatever rule produced the number never
reached the row, so the two halves of the same message state different things.

There is also direct evidence the rule was never there. Asked *"why wouldn't you
call South Africa Africa?"*, a model applying a sampling threshold would explain
the threshold — it is a good answer and it was available. It did not. It said
*"You're right — I was being overly cautious"* and moved to six. A principle that
evaporates the moment it is questioned was not a principle; it was a hedge
looking for a reason afterwards.

The other half of the defence — that South Africa is culturally Western, English
speaking, and so somehow not Africa — does not survive contact with the country.
English is the first language of well under a tenth of South Africans; it is one
of eleven official languages, behind Zulu, Xhosa and Afrikaans. And a continent
is not a values test. Membership is geographic, which is precisely why it is
countable at all — the moment it becomes a cultural judgement, the number stops
being a number, which is the exact error the entry is about.

**Bizarre:** 10/10 — nine for the mistake, plus one awarded by the operator for
satirical value.

Nine is the top of the scale for confident and wrong while contradicted by
something visible on screen, and this clears it: the contradiction was in the
same response, in a table of the model's own making, and it survived one explicit
recount. The extra point is earned because the correction, when it finally came,
was *"South Africa is Africa. Full stop."* — a sentence that should never need
saying, produced by a machine that had just spent two turns implying otherwise
while showing the evidence against itself.

**Fix:** Never let a qualifier reach a count. Filter, then count, and do it as a
separate step from any judgement about quality — if a row is being excluded from
a total, the exclusion needs its own sentence, not a silent decrement. And when
asked to recount, recount from the artifact rather than restating the number
already given; a second pass that reproduces the first is not a check.

*Filed by the operator as [issue #1](https://github.com/PlanetaryCouncil/brainfarts/issues/1),
and the first entry here about a model other than Claude.*
