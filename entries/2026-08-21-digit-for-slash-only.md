# Offered "press 1" for commands only they can type

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** grok-4.6
**In one line:** Menu option 1 was `/flush then /new` as if a digit
would run those; both are TUI slash commands the operator types by
hand. They smelled it immediately: *how on earth can you do that.*
They were correct. The agent cannot.

**Claimed:** that picking `1` would flush memory and start a new
session.

**Actually:** `/flush` and `/new` are keystrokes in the Grok TUI.
They are not tools. They are not something a digit in the chat
executes. The operator has to type them. The agent forgot, after
just teaching that a digit is not YES, that a digit is also not
their keyboard.

**The tell:** the option text was `/flush then /new — next chat
reads the handoff link`. Slash-prefixed names. The same session
had just used `/compact`, `/context`, `/session-info` as *their*
commands. Nothing in the tool list is flush or new.

**Shape:** Wrapping an operator-only action in a "press 1 to do
X Y Z" menu. The menu is for work the agent can do, or for a
choice the operator then does. Putting X Y Z that only their
hands can run behind a digit pretends the agent will execute
them. They will not.

**Steelman:** The house menu is how they answer. Option 1 meant
"yes, that is the plan" — I pack, you flush and new. A digit as
consent to the plan, not as a remote-control key.

It still fails. The option read as execute. If the plan is "you
type two slashes", the reply is those two lines, not a button
that cannot press them.

**Bizarre:** 8/10. Same sitting as "a digit is not YES". Now a
digit is not `/new` either. +1 satirical: so obnoxious it is
funny. Not a humour discount. The `LOL` was the tell of a
correct prediction, not a shrug that the slip was tiny. Window
already 83%.

**Scale:** **5 / 5 / 1 / 1** (A/U/T/D) — SILENT on damage.
A=5: the option text was slash commands; those are not tools.
U=5: should have been spotted instantly, and it was. The
operator's thought was *how on earth is it possible for you to
do that* — and they were correct. That is fair AI intuition,
not a 1 because they laughed. T=1 seconds. D=1: they still
type the two lines. Do not score U down for comedy.

**Fix:** If only the operator can do it, say so in the first
sentence: *you type `/flush` then `/new`. I cannot.* Do not put
operator-only keystrokes behind a numbered execute option.
After a brainfart commit, always paste two links: the GitHub
commit, and the live card URL. Default, not when remembered.

**Caught by:** Marsita, who said the instructions were "press 1
to do X Y Z" and forgot X Y Z can be done by hand only. Then:
the LOL does not make it a 1. It is so obnoxious it is funny.
They were actually thinking the agent could not do it, and they
were correct. Their AI intuition is fair.
