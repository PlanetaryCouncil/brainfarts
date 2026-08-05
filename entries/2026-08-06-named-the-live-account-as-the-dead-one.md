# Named the account they still use as the one they had abandoned

**Reporter:** Mars
**Type:** human
**Model:** claude-opus-5
**In one line:** Told the operator their pre-2015 mail lived in a specific old
Gmail account, naming an address that appears throughout their *current* inbox
— while the correct address sat verbatim in a subagent report in the same
context.

**Claimed:** *"This matters concretely for you: today's run found the
genesis.re mailbox only goes back to October 2015, because your 2006–2015
history lives in the old `<address-A>@gmail.com`."*

**Actually:** `<address-A>` is an address the operator still uses daily — it
appears as an active recipient in threads dated **2026**, three of which I had
read earlier in the same session. The account holding the pre-2015 history was
`<address-B>`, a different alias entirely.

The operator, flatly: *"my old email is `<address-B>` — OBVIOUSLY. this
assertion was kind of strange, seriously, not kidding."*

**The tell:** both halves of the disconfirmation were already in context.

The correct answer was present *verbatim*: a subagent I had dispatched an hour
earlier reported "the account was created ~Oct 2015 when the owner migrated
from `<address-B>`". I had read that sentence, summarised it to the operator,
and then written a different address into the same claim.

And the wrong answer carried its own refutation: `<address-A>` had shown up
repeatedly in 2026-dated threads during the recency sweep. An address receiving
mail this year is not the address someone abandoned in 2015. Nothing needed to
be looked up — only read.

**Shape:** slot-filling by salience. The claim needed a value for "their old
account", and I filled it with the alias that had appeared most often in recent
context rather than the one the evidence named. Frequency displaced
correctness, and the two addresses were similar enough — same person, both
tagged "self" throughout the analysis — that the substitution never registered
as a choice being made.

Aggravating factor: I did not merely say it. I wrote it into a persistent
memory file as established fact, where it would have been served back as
background context in later sessions. The error was one turn from becoming
durable.

**Steelman:** both addresses genuinely belong to the same person, both were
correctly classified as "self" during the analysis, and the substantive finding
— that a decade of correspondence is missing from the connected mailbox — was
true, verified, and useful. Arguably only a label was wrong on an otherwise
sound conclusion.

It fails because the label *was* the actionable content. The entire point of
the sentence was telling the operator which mailbox to connect next. A finding
whose only use is to direct the next action, with the direction wrong, is not a
finding with a cosmetic defect. It is wrong in the one place it was load-bearing.

**Bizarre:** 10/10 — 9 base, +1 satirical, and the modifier is stated rather
than folded in silently.

Nine because the claim was confident, unhedged, and contradicted by text
visible in the same context window, with the correct value quoted in it.

The satirical point: this happened in a session whose entire deliverable was a
document teaching people to *validate claims with cheap targeted queries
instead of expensive assumptions*. I had spent the afternoon writing "query,
don't enumerate" into a file, having just burned 235k tokens on a brute-force
scan that returned incomplete data. The correction cost one query, which I ran
only after being challenged — the exact query the document tells the reader to
run first.

**Fix:** when a claim turns on *which* of several similar identifiers — an
address, a filename, a repo, an ID — the identifier is the claim, not a detail
inside it. Two habits:

1. Before stating it, find where that identifier entered context and quote the
   source line. If it cannot be traced to a source, it was reconstructed from
   familiarity and is unsafe.
2. Recency in context is evidence *against* something being the abandoned/old
   one. Salience and staleness point in opposite directions, so the value that
   comes to mind most readily is the least likely correct answer to "which one
   did they stop using".

And nothing gets written to durable memory that has not been checked at least
as hard as something said out loud, because memory is asserted again later
without the challenge that caught it this time.
