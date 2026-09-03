# The production check — twenty-four questions

Read this for step 9, and whenever someone asks whether an agent is "production
ready".

Run the questions against **one real agent** — ideally the most consequential
one. Answer for that agent, not the estate: readiness varies enormously by
agent, and averaging hides exactly the gap you are looking for.

**Anything the team cannot answer in under a minute *is* the finding.** Record
it as unanswered rather than going away to find out; the time-to-answer is the
measurement.

---

## The questions

| # | Question | Area |
|---|---|---|
| 01 | Can you name the accountable human, not a team? | Ownership |
| 02 | Is there a written autonomy map, readable outside the code? | Boundaries |
| 03 | Is the hottest action it can take written down? | Boundaries |
| 04 | Are limits enforced by mechanism, not by prompt? | Guardrails |
| 05 | Does it act under its own identity, not a shared account? | Identity |
| 06 | Does its behaviour live in version control? | Source |
| 07 | Is the model version pinned? | Dependencies |
| 08 | Is there an ABOM for the running version? | Composition |
| 09 | Is there an evaluation suite, and when did it last grow? | Evaluation |
| 10 | Does it run behavioural regression before model upgrades? | Evaluation |
| 11 | Do users of the agent get a behaviour changelog? | Release |
| 12 | Can you roll back to the last known-good version today? | Release |
| 13 | Is there a kill switch you have actually tested? | Containment |
| 14 | Which of its actions are irreversible? | Reversal |
| 15 | How many actions can it take between human checks? | Supervision |
| 16 | Who reviews its work, and how long does that take per month? | Supervision |
| 17 | Does escalation have a named recipient and a time limit? | Escalation |
| 18 | What happens if nobody answers an escalation? | Escalation |
| 19 | Can you reconstruct any single action it took last month? | Evidence |
| 20 | Does every consequential action leave a receipt? | Evidence |
| 21 | Would you detect a drop in its escalation rate? | Observability |
| 22 | Do you know its cost per unit of work, including review? | Economics |
| 23 | Has an incident ever become an evaluation case? | Learning |
| 24 | Is there a retirement procedure, including revoking access? | Lifecycle |

---

## Scoring bands

- **0-7 — a pilot, whatever its status says.** It may be useful and may be in
  production, but the organisation cannot operate it independently of the people
  who built it.
- **8-16 — it works, and it is held together by specific people rather than by
  design.** The most common band and the most fragile: it survives until someone
  leaves.
- **17-24 — an agent you could defend in front of a client, an auditor or a
  board.** Which is the only definition of production that matters.

---

## Question 21 deserves special attention

*Would you detect a drop in its escalation rate?*

Most monitoring watches for errors going up. An agent that quietly stops
escalating is an agent that has started guessing, and it looks identical to an
agent that has got better. Escalation rate is the one metric where a downward
trend needs the same alarm as an upward one.

If the team has no answer to 21, that is usually the cheapest high-value fix on
the whole list: it is one alert on a number they are probably already logging.

---

## The artefacts an agent estate needs

In a two-person team, one person holds most of this in their head. In an
organisation running forty agents across six functions, it has to be written
down, automated, and connected.

| Artefact | Answers |
|---|---|
| Agent architecture diagram | How the system is put together |
| Agent decision record | Why it was designed this way |
| Agent stack | What technologies it uses |
| Agent inventory | What we have, and where |
| Agent radar | Where our practice is heading |
| ABOM (agent bill of materials) | What is inside this agent's behaviour |
| Evaluation suite | How well it behaves, and how it fails |
| Agent bundle and registry | Exactly what was released |
| Agent manifest | What it is allowed to do, and who it answers to |
| Autonomy map | Autonomous, confirmed, blocked — in plain language |
| Gateway policy | What is actually enforced, not just intended |
| Behaviour changelog | What changed in the agent's character |
| Transcripts and traces | What happened, step by step |
| Action receipts | What changed in the world, on whose authority |
| Agent catalog | What exists and who owns it |
| Agent CMDB | What connects to what |
| Service levels and trust budget | How good it must be, and what freedom it has earned |
| Runbooks and playbooks | What we do when it goes wrong |
| Postmortems | What the incident taught the system |
| Risk register | How this estate could cause harm |
| Behavioural debt register | What shortcuts we are still paying for |
| Portfolio review | What to invest in, standardise, or retire |

**Do not build all twenty-two for agent one.** The order that matters for a first
agent: **agent manifest → autonomy map → gateway policy → action receipts →
evaluation suite.** Those five are the minimum that makes an agent defensible.

The rest become necessary as the estate grows. The aggregate artefacts
(inventory, CMDB, portfolio review) are cheap to start at agent one and
expensive to reconstruct at agent nine — which is the argument for starting them
early even though nobody needs them yet.
