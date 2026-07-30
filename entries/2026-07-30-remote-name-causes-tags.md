# Remote name blamed for tags not pushing

**Claimed:** *"Your remote is named `GitHub_priv`, not `origin` — that's why the
tag stayed local."*

**Actually:** Remote names are arbitrary labels with no effect on anything. Git
never pushes tags automatically regardless of remote name — branches and tags
live in separate namespaces (`refs/heads/` and `refs/tags/`), and a plain push
moves only branches. The tag stayed local because the push came from Sourcetree,
whose "Push all tags" checkbox is off by default.

**The tell:** The commits were already on GitHub, visible in a screenshot in the
same message. If the remote name were broken, *nothing* would have pushed. The
disconfirming evidence was on screen at the moment of the claim.

**Shape:** Confident false causation. Two real facts — "your remote isn't called
origin" and "your tag didn't push" — welded together with "that's why". The
first was true and relevant to something else entirely: an earlier instruction
had said `git push -u origin main --tags`, which would have failed on this
machine. Noticing a real problem, then attaching it to the wrong effect.

**Bizarre:** 7/10. Not higher because there was an adjacent true fact. Not lower
because it asserted a mechanism that does not exist, and took two rounds of
pushback to unpick — the first correction was still muddled.
