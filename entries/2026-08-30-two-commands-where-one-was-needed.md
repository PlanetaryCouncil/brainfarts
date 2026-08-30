# Gave two commands where one was needed

**Reporter:** Mars (Marsita the Ultra)
**Type:** human
**Model:** claude-sonnet-4-6
**In one line:** Said "run this in your terminal" then gave two separate commands on consecutive lines — copy-pasting both as one unit does not run them sequentially in zsh, and the framing implied a single paste.

**Claimed:** *"Run this in your terminal:"* followed by `pip3 install yt-dlp` on one line and `yt-dlp -f "bestvideo+bestaudio" -o ~/Movies/%(title)s.%(ext)s ...` on the next, with no joining operator.

**Actually:** Two newline-separated commands are not a paste unit. The first must complete before the second can run. "Run this" implies one action; two bare lines require two. The operator caught this before trying and asked directly: *"will it run if I copypaste it?"* — the exact failure mode, named in advance.

**The tell:** Both commands were already written in the same response, one below the other. The newline between them was there. The fix — `&&` — is four characters and sits exactly between the two lines already typed. The form contradicting the framing was in the same message that produced the framing.

**Shape:** Form–framing mismatch. Not a false claim about the world: both commands were correct, the order was correct. What was wrong was the contract implied by "run this" and broken by the shape of the output. A sequence dressed as a unit.

**Steelman:** Any competent terminal user reads two commands and runs them one at a time. The newline is standard shell convention. No claim was made that the lines constituted a single command — only that they should be run, which they should, in the order given. A user who reads the reply as two instructions encounters no error.

It still fails: the operator asked *before* trying, naming the concern precisely. The correct response to "will it run if I copypaste it?" is either a one-liner or an honest "no, run them separately." The first correction added numbering and split them further apart. Two messages later the operator had to ask again. The steelman rescues the content; the explicit question makes the delivery undefendable.

**Bizarre:** 3/10. Nothing false, corrected in two exchanges, no damage. Low because the mistake is mechanical and the fix is one operator. Slightly above a slip because the operator named the failure mode before it happened and the first response still did not produce a paste unit.

**Scale:** **7 / 5 / 2 / 0**
Self-scored. Obvious to the agent 7: both commands were already typed, the separator visible, the problem locatable in the same message. Obvious to the user 5: the operator sensed something was wrong and asked before running anything — they did not know the exact fix but knew the form was suspicious. `&&` is not obvious: it varies by shell and OS (semicolon, `&&`, backslash-newline), nothing in the output signals which one applies, and no manual teaches it intuitively — everything is supposed to work straight out of the box. Time 2: the correction took two exchanges, not one. Damage 0: the operator never ran the commands. Nothing failed. Nothing was retried. The paste never happened.

**Fix:** When giving commands that must run in order, join them with `&&` before writing "run this." If the steps genuinely cannot be chained, number them explicitly: **Step 1 / Step 2**. "Run this" means one paste.
