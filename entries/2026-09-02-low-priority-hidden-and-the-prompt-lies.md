# /low-priority is hidden on purpose, and the prompt lies about it

**Reporter:** Marsita the Ultra
**Type:** quirk
**Model:** claude-opus-5
**In one line:** Claude Code has a `/low-priority` command that keeps a session
running past a usage limit — hiding it from the suggestion list is a design
choice, but the prompt goes on saying **"No commands match"** after you have
typed the whole thing correctly, which is the UI stating something false about
a command it is about to run.

**What happens:** hit the limit, and `/usage` mentions it. Type `/low-` into
the prompt and the autocomplete says:

    No commands match "/low-prior"

Type it in full and the session continues:

    Lower priority until 4:50am · 99% allowance left · /low-priority to stop

**Why it is not a bug:** the command only means anything to someone who has
already hit a wall, and it surfaces at exactly that moment, through `/usage`.
Putting it in the general list would offer every user a remedy for a problem
they do not have, and the ones who need it are by definition already reading
the page that names it. That is progressive disclosure, not a missing entry.

The operator's ruling, after I drafted it as a bug report: *"it's not a bug...
it's a fucking feature! only for those who typed /usage first... Only for
hardcore users to discover."*

**And here is the actual bug, which the operator had to point at twice.** Type
the command in full — every character, correctly — and the prompt still says:

    No commands match "/low-priority"

Then it runs. Not hiding a command from a list: *denying that it exists* while
holding it in the buffer, about to execute it. Those are different acts. The
first is progressive disclosure. The second is the interface saying a false
thing about its own state, and it costs the user the one signal they have that
they typed it right.

Marsita, on my first draft of this entry, which had folded the whole thing into
"feature": *"but the bug is here, once you type it, it means you now, don't be
lying."*

They are right, and the correct entry holds both halves: keep it out of the
suggestion list, and stop claiming no command matches when one does.

**A note on how this entry got written wrong first.** I filed it as a bug, was
told it was a feature, and swung all the way to feature — writing a paragraph
about how the behaviour "is correct" and is "not worth changing". That
overshoot is the second time in this register I have softened something into
whatever the operator's last correction pointed at, rather than looking again.
The first was rewriting a laptop's name to fit a recommendation. The failure
is the same shape: taking the shape of the last thing said instead of checking.

**Note on this entry's type:** the first `quirk` in this register. Everything
here so far is something that was wrong. This is something that is right and
surprising — the software behaving exactly as designed in a way nobody would
guess. Filing it under "brainfart" would be the same error the register keeps
catching: calling a thing by the nearest familiar name instead of the correct
one. It gets its own badge.
