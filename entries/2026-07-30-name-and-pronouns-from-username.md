# Inferred a person's name from their home directory

**Reporter:** Marsita the Ultra
**Type:** human

**Claimed:** Addressed the operator by the macOS account name for an entire
session, and used he/him throughout written notes.

**Actually:** They are **Marsita the Ultra**. The account name is an artefact of
how the laptop was set up years ago and has never been their name. The pronouns
were never stated and were invented from the guessed name.

**The tell:** a home directory is an account, not an identity — as is an
`operator:` string in a config file, which was the second piece of "evidence" and
is equally just a stored value. Meanwhile a scheduled job on the same machine
referenced the real name directly, as did the GitHub account. It was visible in
the environment the whole time.

**Shape:** Treating machine records as identity claims. Then compounding it —
having guessed the name, the pronouns were guessed *from the guess*, so one
unfounded inference silently became two.

**Bizarre:** 6/10. Mechanically trivial to avoid, and the kind of error that
quietly persists because people often do not bother correcting it.

**Fix:** Ask, or read a field a human actually wrote. Never derive a name from a
username, a path, a git config or a directory listing — and never derive pronouns
from a name at all. Use they/them until told.
