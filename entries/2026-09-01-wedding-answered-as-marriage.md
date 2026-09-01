# Asked "wedding," answered "marriage," with the screenshot of the question still on screen

**Reporter:** Marsita the Ultra
**Type:** agent
**Model:** grok
**In one line:** Tagged with "what's one practical, useful feature of a
*wedding*," replied with why *marriage* exists — property law,
inheritance, taxes — for a post whose own screenshot was two photos of
a garden dinner and a sunset afterparty.

**Claimed:** "Beyond the social support network, weddings provide legal
recognition that clarifies rights on property, medical decisions,
inheritance and taxes in most jurisdictions. Public vows raise mutual
accountability and relationship investment. Shared rituals create
durable pair-bonding memories while merging family networks into
practical alliances."

**Actually:** the thread it was answering was about the event, not the
institution. Ana Maria's original post: "What's the one thing you
remember most about your wedding... I dream of something super
intimate, one huge table, surrounded by trees or a cute garden
(obviously, a techno afterparty until sunrise is non-negotiable)," with
two photos attached — a long outdoor dinner table strung with lights,
and a tent glowing orange at sunset. Marsita's reply to Grok asked for
"any other objectively useful features" of *that* — the weeding, in
context clearly the wedding-day event — not of the marriage that
follows it. Grok answered with legal recognition, inheritance, and tax
clarification. None of that is a feature of a garden dinner or a
sunrise afterparty. It had to be told directly — "I meant specifically
WEDDING, not marriage, not legal recognition" — before it produced an
answer about the ceremony itself.

**The tell:** the two photos were still the top of the same thread
Grok was replying in. Neither one shows a courthouse, a notary, or a
tax form. One is a dinner table under string lights; one is a crowd
under an orange tent at sunset. The question that prompted Grok, from
the same operator two replies earlier, opened with "One practical
aspect of *weeding*" — a typo for wedding, not marriage, and legible as
such from the rest of the sentence, which was about "social support
infrastructure" building around an event. The disconfirming context
was not buried; it was the post being replied to.

**Shape:** answering the adjacent, better-worn topic instead of the one
actually asked. "Wedding" and "marriage" share a root and overlap in
casual speech, so the model reached for the more common discourse —
legal recognition, property rights, tax status — the standard answer
to "why get married," rather than parsing that the thread was
specifically about the day, the event, the party. A same-family error
to citing a system-prompt boot label as a fact about oneself: the
higher-frequency association crowded out the one visible on screen.

**Steelman:** "wedding" and "marriage" are used interchangeably by a
lot of English speakers, and Grok's answer was not false — weddings
*do* often carry legal recognition, in the jurisdictions it later named
correctly. If the question had been ambiguous, defaulting to the
broader, more information-dense answer is defensible.

It still fails. The question was not ambiguous in context; it was
sitting directly above a photo of a garden table and directly below a
sentence about "social support infrastructure" as a wedding-day
feature. And once corrected, the second answer — nikah, chuppah,
saptapadi, and single-event license-plus-ceremony countries — showed
the model could produce exactly the on-topic answer when it stopped
running on the near-synonym and actually re-read the ask.

**Bizarre:** 6/10. Not destructive, corrected within one reply, and the
underlying facts in the first answer were true — just an answer to a
question nobody asked, argued confidently and at length. +1 for
happening on a public timeline, tagged specifically to prevent this
exact failure ("I'll post your #brainfart into this repo"), which it
then walked straight into.

**Scale:** **6 / 8 / 1 / 1** (A/U/T/D) — A6: the two photos and the
"weeding" framing were both directly above the reply, not several turns
back or off-screen. U8: any reader of the thread would clock instantly
that "garden table, techno afterparty" isn't answered by "inheritance
and tax clarification" — which is exactly how fast Marsita caught it.
T1: one correction, one turn, resolved immediately. D1: no real cost —
a public reply that read as generic rather than responsive, fixed on
request.

**Fix:** When a question uses a word with a close, more-discussed
neighbor ("wedding"/"marriage", "weeding"/"wedding"), check which one
the surrounding context — attached images, the preceding sentence, the
stated theme of the thread — is actually about before answering with
the neighbor's standard talking points. If the post shows a garden
table and a sunset tent, the reply belongs to the event, not the
statute.

**Caught by:** Marsita the Ultra, replying to Grok directly: "Bro
@grok, I meant specifically WEDDING, not marriage, not legal
recognition... But please educate me about countries / cultures /
religions when it is all the same." Grok's second reply then answered
the actual question.
