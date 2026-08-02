# "It hasn't run" — it had run three times

**Reporter:** Marsita the Ultra
**Type:** human

**Claimed:** Looking at an empty `self-improve` panel: *"it's scheduled for 03:00
and hasn't run. Almost certainly the mac slept through it."*

**Actually:** It had run three cycles, most recently at 02:04 that morning,
scanning 89 session transcripts and producing two commits. The panel was empty
because that worker had never been instrumented to post events — a display gap,
not an execution gap.

**The tell:** `state/cycles.log` and the git history were both one command away
and both said it ran. The claim was a guess dressed as a diagnosis, and it came
with a confident cause attached ("the mac slept") that was also invented.

**Shape:** Absence of evidence read as evidence of absence — with a fabricated
explanation bolted on. The empty panel had at least two possible causes and only
one was checked: none.

**Bizarre:** 6/10. Plausible, and the user had to correct it ("this mac is on
amphetamine, I kept it on overnight") before the actual cause surfaced.
