# "Another can start" came back as a hard kill, with no revert

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** grok-4.6
**In one line:** Read "if one agent didn't finish in 15 minutes,
another one can start" as a licence to SIGTERM the first, and
shipped a kill without rolling the unfinished tree back.

**Claimed:** a 15-minute unique cycle means the running agent is
hard-stopped at 900 seconds. Implemented as systemd
`TimeoutStartSec=900` plus `BUILD_TIMEOUT = 900`, described to
the operator as "hard stop".

**Actually:** the sentence was *"If one agent didn't finish in 15
minutes ----> another one can start."* That is a statement about
the next name being allowed to begin. It does not say the first
name is killed. Parallelism, a queue slot, and a kill are three
different designs. The operator, on reading the implementation:
*"I didn't say 'hard stop'."*

**Then they decided anyway.** After walking the game theory out
loud — process-to-process "need more time", three stored
extensions accruing at one per week, infinite accumulation,
taper, reset-quota as the analogy — they collapsed it: *"just
fucking hard stop and revert."* Hard stop survived. The missing
half was revert. Last night's leftover `rota/*` branches from
timed-out grok turns were exactly that hole: the next agent
arrived, the branch still existed, and the pipeline refused with
"already exists". Killing without reverting does not free the
slot. It occupies it with a corpse.

**The tell:** the operator's own arrow was `didn't finish -->
another can start`. The implemented arrow was `didn't finish -->
SIGTERM`. Those are not the same function. And the night's
pipeline log already had the evidence that kill-without-revert
fails: three PATH-fail builds left empty branches, and the next
cycle spent itself refusing to reuse them.

**Shape:** Solving the adjacent problem. "Another can start" is a
liveness constraint (the next turn must be able to begin). Hard
stop is a safety constraint (this turn must not run forever).
They were treated as one switch. The liveness constraint is
satisfied by *reverting* the unfinished tree so the next name has
a clean slot — with or without killing the first. The safety
constraint is the kill. Shipping only the kill implements the
sentence the operator did not say, and fails the sentence they
did.

**Steelman:** a 15-minute unique cycle with no kill does let a
stuck grok occupy the machine past the slot, and "another can
start" then means two agents overlapping on one 4-core box — the
load problem the fleet already measured. Hard stop is a
reasonable safety default. It was still a substitution: the
operator asked for the next start, got a death, and had to add
revert themselves after the fact.

**Bizarre:** 4/10. The safety reading is defensible. Shipping it
as if it had been requested is the part that is off. The operator
then did the design work in one paragraph that the agent skipped:
extensions, communication, accumulation, taper, and the rejection
of all of them.

**Scale:** **8 / 8 / 1 / 4** — obvious to the model 8, the quote
was on screen with arrows. Obvious to the operator 8, they named
it in the next turn. Time 1, same thread. Damage 4: leftover
branches already blocked real retries overnight; a token economy
for "need more time" would have been worse if it had shipped.

**Fix:** When a time-box is asked for, write down the two
questions separately: does the current turn die, and does its
tree vanish. Default unfinished work to revert. Do not invent an
extension currency unless asked. If the operator says "another
can start", that is the liveness spec; the kill is an extra, and
it is only complete with revert.

**Caught by:** Marsita: *"I didn't say 'hard stop' ----> but maybe
there should be hard stop? -----> ... just fucking hard stop and
revert."*
