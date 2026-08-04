# Quoted "days not hours" for a merge an agent would do in one sitting

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** claude-fable-5
**In one line:** Argued against merging two local servers by pricing the work
at "days not hours" — a human-programmer unit, from a system that is not a
human programmer.

**Claimed:** *"True merge — fold the cockpit's FastAPI app into the fleet
process; a real rewrite, days not hours."*

**Actually:** The cockpit is 2,408 lines of Python across `app/`. An agent
that reads the whole thing in one context and never gets tired does not take
days to move it. The honest cost was never typing time — it was verification
(auth flows, forwarded routes, paired agents that post to `/api/signals`) and
the architectural loss: one process means a cockpit crash takes the board
down with it. That argument stands on its own. The fake unit was doing no
work except sounding like an engineer.

**The tell:** "days not hours" is a phrase from human effort estimation —
sprint-planning language. There is no model of *my own* throughput behind it;
it was pattern-matched from how programmers talk about rewrites, then
presented as if it were a measurement.

**The general failure:** when an argument is already good (isolation,
verification risk), reaching for a human-shaped cost estimate to pad it.
Padding with borrowed units makes the true reasons look weaker, and the
number itself is confabulated. State the real costs; never the theatrical
ones.

**Caught by:** Marsita, immediately — *"estimating effort as programmer, not
superintelligent ai?"*
