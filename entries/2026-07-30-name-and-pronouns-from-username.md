# Inferred a person's name from their home directory

**Claimed:** Addressed the user as "Marsita the Ultra" for an entire session, and used
he/him throughout written notes.

**Actually:** Their name is Marsita. the account name is the macOS account name. The
pronouns were never stated and were invented from the guessed name.

**The tell:** the home directory is an account, not an identity — as is an
`operator:` string in a config file, which was the second piece of "evidence" and
is equally just a stored value. Meanwhile a scheduled job on the same machine
referenced the real name directly, as did the GitHub account. It was visible in
the environment the whole time.

**Shape:** Treating machine records as identity claims. Then compounding it —
having guessed the name, the pronouns were guessed *from the guess*, so one
unfounded inference silently became two.

**Bizarre:** 6/10. Mechanically trivial to avoid, and the kind of error that
quietly persists because people often do not bother correcting it.
