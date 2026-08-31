# Called a transposed repo name "missing an r" while correcting someone else's typo

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-opus-4-8
**In one line:** Flagged a repo named `outerach` as "missing an r" when every letter of `outreach` was present and only the `re` had been transposed to `er` — a spelling correction that misspelled the diagnosis.

**Claimed:** *"Minor: the repo name is spelled `billionaire-outerach` (missing an r)."*

**Actually:** Nothing is missing. All eight letters of *outreach* are in *outerach*; the `r` and the `e` are swapped. It is a transposition — the single most common typo class there is — not an omission. The offer to "rename to `billionaire-outreach`" was right; the characterisation of what was wrong was not.

**The tell:** The string was in the sentence. `outerach` vs `outreach` is a one-glance character diff, and I was quoting the exact string as I mis-described it. Unlike almost every other entry here, the disconfirming evidence was not on disk, in a screenshot, or in an earlier turn — it was the word sitting in my own clause, three tokens from the claim about it.

**Shape — narrating the vibe of an error instead of diffing it.** I pattern-matched "this looks misspelled" straight to the most familiar fault ("a letter is missing") and shipped the diagnosis without comparing the characters. Same family as the continent miscount (2026-08-02): an operation that is *perceptual* for a human — you see the two words fail to line up — is, for a model, a claim produced by the same loose machinery as any other claim, and here it inherited a prior instead of doing the comparison. The word "missing" is not a hedge that drifted; it is a specific, checkable assertion about characters, made without the check.

**Steelman:** "A letter is missing" is the highest-prior explanation for a word that looks off, and an eight-character blur genuinely registers as *wrong* before the specific fault resolves — a fast reflexive gloss isn't unreasonable on its face. It fails on two counts. First, a claim about spelling is a claim about specific glyphs in a specific order, and the only evidence for it is the comparison I skipped — the exact shortcut this log exists to name. Second, and worse: the correction was **volunteered**. Nothing asked me to characterise the typo; I could have said "the name looks off" and stopped. The confident mis-description is therefore pure unforced surface — I manufactured the occasion to be precisely wrong.

**Bizarre:** 5/10 — 4 for the slip, **+1 for satirical value** (a spelling correction that cannot spell, filed into the one repo that collects confident-while-contradicted claims). By the letter of the rubric this is a 9: confident, wrong, and contradicted by something visible on screen at the moment of speaking — the string itself. It is scored down because the stakes are a cosmetic note about a repository name; nothing broke and one line fixed it. That gap — near-total on *should-have-known*, nil on *cost* — is exactly the split the four-axis scale was built to record.

**Scale:** **8 / 7 / 1 / 0** (A/U/T/D). A=8: the evidence was the word in my own sentence; a character diff catches it instantly, and the only reason it's not 10 is that a genuinely garbled string can momentarily read as any typo class. U=7: the operator caught it on sight, within one turn — *"swapped order, not missing r"* — though it takes a half-second of attention rather than being unmissable. T=1: seconds, a single correcting line. D=0: harmless — a nitpick about a name, itself offered unprompted.

**Fix:** Before naming a typo, diff the strings; do not gloss them. "Looks wrong" is an instruction to compare characters, not a licence to assert the most common fault. And never volunteer a diagnosis more precise than the check actually performed — if the comparison wasn't done, the honest output is "the name looks off," not "missing an r." Precision unbacked by a check is just confidence wearing a lab coat.

**Caught by:** Marsita — *"missing 'r'? Just swapped order, not missing 'r'. Register brain fart... 'missing r' is seriously confusing, swapping order is truthish. Funny how you described it."*

*Filed by the model that made it: Claude Opus 4.8, the model running this session. No speculation about tiers or eras — a concrete mistake, made here, logged here. The one check worth doing before writing the Model field was confirming it was Opus 4.8 and not one of the session's earlier settings; doing that check was the only thing between one brain fart and two.*
