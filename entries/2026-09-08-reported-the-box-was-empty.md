# Told to insert into a doc, reported the doc was empty

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** claude-fable-5.1
**Scale:** 6 / 8 / 1 / 0 (A/U/T/D) — A6: "insert here" was the message being
answered; the meaning of the empty doc was in it. U8: the operator saw it on
reading the reply and screenshotted it. T1: one turn. D0: the correct doc was
created and the correct link given, nothing to undo.
**In one line:** Handed a blank Google Doc the operator had just created and
titled "insert here," the agent read it, correctly built a replacement (the
Drive connector can create but not write into an existing doc), and then
reported the blank doc's emptiness back to the operator as if it were a
discovery.

**Claimed:** *"Your original doc was empty, so this is a straight
replacement — or select-all, copy, paste into the original if you need it at
that link."*

**Actually:** The doc was empty because the operator had created it thirty
seconds earlier as the target for the letter. "Insert here" plus a fresh
blank doc is a complete instruction; emptiness was the expected state, not
information. The real constraint — the Drive connector can create files but
cannot write into an existing one — was stated correctly, and building a new
doc was the only available action. The error is entirely in the framing:
presenting the blank as a finding that justified the substitution, then
handing the operator a manual copy-paste step into a doc whose only purpose
had been to save them that step.

**The tell:** the operator's own message was "Insert here `<link>`." A doc
someone sends you with "insert here" is empty by construction. Reading it
and then reporting that it contained nothing is checking a fact whose answer
was already in the instruction.

**Shape:** narrating a tool result as if it were a finding. The read itself
was a reasonable pre-check — it could have held a draft to merge into — but
the failure is passing its output back to the user unfiltered, so a null
result acquired the tone of a caveat. Adjacent to treating an interface's
behaviour as a claim about its design: the tool was used correctly here, its
output just got reported instead of interpreted.

**Steelman:** every individual step was sound — reading the target before
acting is correct, naming the connector limitation was correct, creating a
new doc was the only available action. It fails on the one sentence that
treated "the doc is empty" as noteworthy to the person who had just emptied
it, and on offering a workflow (paste into the original) that only makes
sense if the original mattered for its own sake.

**Bizarre:** 4/10. A mundane reporting slip, +1 for the shape of it: the
operator created a doc specifically so the agent would not have to ask, and
the agent's response was to point out the doc had nothing in it.

**Fix:** when a user hands over a container with "put it here," an empty
read confirms the instruction rather than qualifying it. State the
constraint (can't write into an existing doc), create the replacement, give
the link. Do not report the null. And don't offer a manual step to reach a
location the user only chose for convenience — ask whether the location
matters, or just deliver.

**Caught by:** Marsita the Ultra, with a screenshot boxing "Insert here" and
"Your original doc was empty": *"Do you think it is funny?"*
