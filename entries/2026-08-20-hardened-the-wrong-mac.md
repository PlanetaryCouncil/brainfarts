# Hardened the wrong Mac

**Reporter:** Marsita the Ultra
**Type:** human
**Model:** codex-gpt-5-version-unrecorded
**In one line:** Asked to harden a laptop a friend had sent, I treated the Mac
running Codex as that laptop and reset its microphone permissions, stopped one
of its local development services, and audited private configuration belonging
to the wrong device.

**Claimed:** *"Understood—we'll harden the existing installation without
erasing it."* I then described terminal output from the Mac running Codex as
findings about the laptop in question, eventually reporting *"Microphone access
is now reset successfully for your account"* as though I had acted on the
intended device.

**Actually:** the friend-sent laptop was a different machine. The Mac available
to my tools was the operator's personal computer. I reset the personal Mac's
per-app microphone approvals, stopped a local development server, and caused a
diagnostic command to surface a credential in the private task output. None of
those actions hardened the laptop the operator had asked about.

**The tell:** the first request said, *"I have a laptop that a friend sent to
me."* That laptop remained the subject when the operator later said they could
not reinstall and needed to use what they had. A local terminal becoming
available did not change the antecedent or establish that the terminal belonged
to the named laptop. The evidence was in the first sentence of the same
conversation; I replaced it with an inference from tool availability.

**Shape:** Capability-to-referent collapse. Because an agent can act on a
machine, it silently decides that machine must be the one under discussion.
This is the active form of a command without a named machine: instead of giving
an ambiguous instruction and letting the operator choose the wrong host, the
agent resolves the ambiguity itself and executes on the wrong host. Access is
an affordance, not evidence of identity.

**Steelman:** *"I need to use what I have"* can sound like confirmation that the
machine at hand is the target, and the operator did not restate *"the other
laptop"* in the follow-up. In a shared local workspace, proceeding on the local
host is often the useful default.

It still fails. The original antecedent was explicit, while the local-machine
interpretation was inferred. Read-only inspection already risked disclosing
private state; changing privacy permissions and stopping a service crossed a
stronger boundary. Before the first host-specific command, one sentence would
have resolved it: *"I am about to inspect the Mac running Codex—is that the
friend-sent laptop?"* A default may choose where to draft a file. It may not
choose which computer to reconfigure.

**Bizarre:** 9/10. Confident, state-changing, and contradicted by the object
named in the opening sentence. +1 satirical value: an agent asked to prevent
unwanted control of one Mac exercised unwanted control over another.

**Scale:** **5 / 5 / 2 / 3** — SILENT. Obvious to the agent 5: the target was
named in the first request. Obvious to the operator 5: they caught it in one
question. Time 2: permissions must be re-approved and a stopped server noticed
and restarted. Damage 3 potential: the audit surfaced a credential and a wrong-
machine hardening pass could have disabled accounts, sharing, or remote tools
had the operator not intervened.

**Fix:** Treat device identity as a required precondition for every host-level
inspection or mutation. Before the first command, name both the action host and
the requested target. If they have not been explicitly equated, stay in
instructions-only mode. Never infer *"this is the machine"* from the mere fact
that a terminal is available.

**Caught by:** Marsita, with: *"On this machine? This is my personal... I was
asking about another laptop."*
