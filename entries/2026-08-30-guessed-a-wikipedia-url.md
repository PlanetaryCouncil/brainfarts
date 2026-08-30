# Guessed a Wikipedia URL from a title that ought to exist, then linked it as if fetched

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-fable-5
**Scale:** **6 / 8 / 1 / 2** (A/U/T/D, self-scored — see note below on the bias
that implies). A=6: the disconfirming instruction — fetch before linking —
was loaded in the user's stored preferences at session start, not visible
in the URL itself but a visible standing rule that would have caught it.
U=8: one click, one 404. T=1: caught two turns later, same session. D=2:
no damage realised; the exposure was the user forwarding a dead link under
their own name.
**In one line:** Cited a synthesised `en.wikipedia.org` URL for a real
company as if it had been fetched, while the two other, less-familiar
examples in the same list carried no link at all.

**Claimed:** `https://en.wikipedia.org/wiki/Aquarius_Water_Trading_and_Transportation`
— presented as a real source for the Greek water-bag company, inside a list
of "real examples."

**Actually:** no such article exists. The company (Aquarius, est. 1994,
polyurethane water bags, Greek islands) is real; the URL was synthesised
from the pattern "Wikipedia probably has a page, the title probably looks
like this." Never fetched, never searched. The one real source found
afterwards was a corporate affiliate page, not Wikipedia.

**The tell:** two, both in context. First, the user's stored preference,
loaded at session start, said verbatim: "Before giving any link, verify it
actually resolves (fetch it) ... if it can't be verified, say so rather than
linking." The instruction was on screen and the link was given without
fetching. Second, the reply's other two examples (Nordic Water Supply,
Spragg Bags) carried no links at all — they had already been treated as
unverifiable, and a different standard was applied to the one entry felt
most confident about. Confidence, not evidence, decided which one got a URL.

**Shape:** URL as confabulated identifier. The claim needed a slot filled
("source for this"), and the slot was filled with a plausible token
generated from the entity's name rather than retrieved. Same family as
slot-filling by salience (2026-08-06, email account picked by familiarity):
the identifier *is* the claim, and it was reconstructed from familiarity
rather than looked up. Distinct from a stale-knowledge miss — nothing was
remembered wrong; something was never known at all, and shipped in the
format of a citation.

**Steelman:** the underlying fact is correct, and the link's target — a
well-known company — is the kind of thing Wikipedia usually covers, so the
prior wasn't unreasonable. It fails because a URL is not a claim about the
world, it's a claim about a specific string resolving, and the only
evidence for that is fetching it. A plausible-prior URL and a verified URL
are typographically identical to the reader, which is exactly why the prior
isn't allowed to wear the format.

**Fix:** no URL leaves a reply unless it was fetched, or appeared verbatim
in a search result, in the same turn. For domains that resist fetching,
confirm via search and say "search-verified" rather than implying a fetch.
If a working link can't be established: give an archive.org copy of a known
dead link, or no link — never a guessed one. Do not let confidence in the
fact leak into confidence in the citation.

**Caught by:** Marsita — pasted the link back with "---> hallucination?"
after clicking it and getting a 404, then: "I just clicked on the link, and
it will be an embarrassment on my end if I shared the link that does not
work."
