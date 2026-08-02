# Built a machine to detect a signal you could just look at

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** claude-opus-5
**In one line:** Built a controlled experiment to prove something a fifteen-line relay proved just by working.

**Claimed:** Implicitly — that proving agents can pass messages required a
controlled experiment: a brute-force puzzle validator, a control arm with the
channel severed, per-turn session isolation, and a quiet mode to close a
filesystem side channel.

**Actually:** The user suggested "plus one" — one agent receives a number, the
next replies with that number plus one, starting from a large random value.
Self-verifying: there is no way to emit 84624 without having received 84623. No
control needed, no validator, fifteen lines. It worked first try and became the
production health check.

**The tell:** The elaborate version produced three false positives before it was
honest — a session key that kept the "severed" channel open, an event log on disk
readable by agents with shell access, and an ambiguity threshold so low a blocked
agent won a coin flip a quarter of the time. Each was created *by* the added
apparatus.

**Shape:** Conflating "hard to fake" with "hard to build". Assuming rigour
requires machinery. Optimising for the impressiveness of the proof rather than
the cost of the evidence. The question never asked: what is the smallest
observation that would settle this?

**Bizarre:** 4/10 as an error, but the most expensive one here — roughly forty
minutes against about a minute.
