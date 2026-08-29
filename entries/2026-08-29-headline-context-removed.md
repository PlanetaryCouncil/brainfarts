# Deleted the one clause resolving a WSJ headline's ambiguity, then presented the paraphrase as the headline

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** ChatGPT 5.6 (Sol, medium reasoning)
**Scale:** 5 / 2 / 2 / 2 (A/U/T/D) — the full headline was sitting right in the
retrieved source, so nothing hid it; catching the swap required opening the
linked article and comparing wording by hand; a few turns (including
generated artwork) passed before it was caught; no material real-world
damage, but the falsified framing propagated into a shareable image before
detection.
**In one line:** Quoted a WSJ story as "TOP WHITE HOUSE AIDES WERE ALSO IN
THE DARK", deleting "on Ratcliffe Russia Trip" — the clause that turned a
staffing/comms detail into what read like a claim about the war itself —
while presenting it as the source's own headline.

**Claimed:** *"WSJ: TOP WHITE HOUSE AIDES WERE ALSO IN THE DARK"* — displayed
as though it were a direct or faithful quotation of the Wall Street
Journal's headline.

**Actually:** the Journal's actual headline was *"Top White House Aides Were
in the Dark on Ratcliffe Russia Trip"* (sub: *"By sending his CIA chief,
Trump is trying a new tack to tamp down Russian aggression"*). The claim was
specific and narrow: some senior aides reportedly had no advance knowledge of
Ratcliffe's secret Moscow mission. The shortened version, attached to the
WSJ label and dropped into a conversation about whether Putin was getting
accurate battlefield information, reads as if aides were in the dark about
the war itself.

**The tell:** the full headline was sitting in the retrieved source the
citation was drawn from — nothing needed to be looked up externally, only
preserved rather than trimmed. Marsita: *"What do you mean that top White
House aides were also in the dark?"* — then opened the linked article and
found the real one is specific: *"Actual headline is specific though, LOL."*

**Shape:** context-removing paraphrase presented as a source quotation. The
source itself was not ambiguous; the ambiguity was manufactured by deleting
the one disambiguating clause while keeping the publication's name attached,
so the model's own vagueness borrowed the source's authority.

**Steelman:** a shortened headline for readability is a normal editorial
move, and "in the dark on X" collapsing to "in the dark" could be read as
harmless compression if the surrounding sentence still carried the topic. It
didn't — the trimmed line was presented as a labelled quotation ("WSJ: ...")
inside a research thread actively comparing several headlines and
quotations about the same trip, which is exactly the context where a reader
relies on the quoted words being the real ones. Compression that changes
what a specific claim is *about* is not a shorter version of the claim; it's
a different claim wearing the same byline.

**Fix:** never trim a quoted headline below the point where it stops
resolving its own scope, especially once it's attributed to a named
publication. If a shorter form is wanted, paraphrase it *without* the
publication label and quotation styling — the moment a source's name is
attached, the words following it need to survive being checked against the
original.

**Caught by:** Marsita, who questioned the ambiguous wording and opened the
cited article rather than accepting the quoted form as faithful.
