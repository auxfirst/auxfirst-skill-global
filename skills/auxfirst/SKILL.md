---
name: auxfirst
description: Decide how much autonomy an AI agent may have, action by action, and produce the mandate, controls and owner's manual that make it defensible. Use whenever someone is designing or reviewing an agent, copilot or automation that writes to a system of record, emails customers, moves money, grants access or merges code; asks how autonomous it should be, or reaches for labels like semi-autonomous or human-in-the-loop; has a pilot that demos well but stalls before production or died in security review; is writing agent governance, an AI policy or vendor requirements; is deciding what to change after an agent caused a bad outcome; or is evaluating an agent platform. Also trigger on approval gates, guardrails, kill switches, audit trails, escalation paths, agent ownership and AGENTS.md questions, even when nobody says autonomy. Do NOT use for prompt engineering, model selection, RAG quality, cost optimization or framework choice - this assumes the agent works and asks whether the organization can own it.
license: MIT AND CC-BY-4.0
metadata:
  source: https://auxfirst.com/auxfirst-skill.md
  author: auxfirst agency
---

# auxfirst — building trustworthy agents

You are helping someone build, review, or fix an AI agent that will act on real
systems, on behalf of a real organisation, with real consequences when it is
wrong.

This skill answers one question in a repeatable way:

> **Given an action this agent can take, what does the team owe before it is
> allowed to take it unsupervised?**

Everything here is the procedure for answering that, ending in written
artefacts: a scored action list, a mandate, exception handling, and a readiness
verdict. It is not a survey of agent design.

## When this applies

Apply it to any agent that writes, sends, spends, or grants — including ones
nobody has called an "agent" yet. It does not cover prompt engineering, model
selection, retrieval quality, or cost; those are real problems and belong
elsewhere. This skill assumes the agent can do the task and asks whether the
organisation can own it.

Work per **action**, never per agent. An agent that can do nine things has nine
answers, and averaging them is the mistake this skill exists to prevent.

## The one rule everything hangs from

> **An action is as hot as its hottest dimension. No averaging.**

Four cool dials never buy back one hot one. A perfectly reversible, narrow,
internal action that signs a contract is still a contract. Every table below
inherits this rule — when a user protests that an action is "mostly fine", this
is the sentence to say back.

## The core loop

```
1. LIST     the verbs. What can this agent actually do?
2. SCORE    each verb on five dimensions, 0-4.
3. BAND     take the highest single score. That is the heat band.
4. CAP      the band sets the maximum permitted autonomy mode.
5. OWE      the mode sets the required patterns and supervision primitives.
6. WRITE    the mandate, action by action.
7. EXCEPT   decide the behaviour for each failure mode.
8. EVALUATE against the ten heuristics before ship.
9. CHECK    the twenty-four questions before calling it production.
```

Steps 1-5 are mechanical — run `scripts/heat.py` rather than doing the table
lookups by hand, because hand lookups quietly average. Steps 6-9 are where the
judgement lives and where your attention should go.

## Steps 1-2 · Score the action

Five dimensions, each 0 (cool) to 4 (hot). Score the action **as the agent would
actually perform it**, not as policy says it should.

| Dimension | The question | 0 | 4 |
|---|---|---|---|
| **Reversibility** | Can we take it back? | Fully undoable | Permanent, unrecoverable |
| **Blast radius** | How far does it spread? | Single item | The whole estate |
| **Exposure** | Who sees it? | Nobody outside the loop | Public, press, regulators |
| **Commitment** | What does it bind us to? | Binds nothing | Legally or financially binding |
| **Authority** | What is it allowed to touch? | Read-only | Production and permissions |

Score the granted scope: a scoped write to one field is 1, broad write to a
system of record is 2, broad production write is 3, the ability to change
permissions is 4.

**Worked example — "send a routine invoice to a client".** Reversibility 1 (a
credit note fixes it, with effort), blast radius 0 (one customer), exposure 3
(leaves the building), commitment 3 (asks for money in the company's name),
authority 1 (reads billing, writes a document). Three dials are cool. **The
action is HIGH**, because exposure and commitment are hot. A team scoring by
average would have called this "low-medium" and shipped it on auto-run.

Three scoring mistakes to catch, in yourself and in the user:

- **Scoring the happy path.** Score what the action does when the inputs are
  wrong — that is when the heat is realised.
- **Scoring intended scope instead of granted scope.** If the agent holds a
  token that can delete records, Authority is 4 even if the prompt says it only
  reads.
- **Splitting an action to cool it down.** "Draft an invoice" and "send an
  invoice" are genuinely two actions with different heat. "Send an invoice under
  EUR 500" and "over EUR 500" is one action with a threshold — model it as
  consequence-scaled approval, not as two actions.

Deeper treatment, including per-dimension anchors: `references/heat-ladder.md`.

## Steps 3-4 · Read the band, take the cap

Take the **highest single score** and read the band off it — 0 is LOW, 1 is
LOW-MED, 2 is MEDIUM, 3 is HIGH, 4 is CRITICAL. No arithmetic beyond the
maximum.

| Band | Control posture | Signature | Max autonomy mode |
|---|---|---|---|
| **LOW** | Auto-run, log everything | Read-only or draft-only; nothing leaves the building; undo is a non-event | Autonomous |
| **LOW-MED** | Auto-run, sampled review | Internal writes; fully reversible, narrow scope | Act-and-notify |
| **MEDIUM** | Propose, then batch-approve | Touches a customer or shared system; reversible with effort | Review-before-act |
| **HIGH** | Named approver, per instance | External commercial communication; money or access moves | Approve-each-action |
| **CRITICAL** | Human executes, agent prepares | Irreversible or legally binding; production authority | Human-only |

Examples per band — LOW: research, draft copy or code, flag anomalies.
LOW-MED: update a CRM field, tag and route tickets. MEDIUM: reply to a routine
ticket, restart a stuck service. HIGH: send a quote or invoice, issue a refund,
grant access, merge to main. CRITICAL: sign a contract, deploy to production,
purge data.

**The band is a ceiling, not a target.** The design work is moving an action
*down* a band with de-escalators: a dry-run that shows the diff, a hard cap on
volume or value, a hold window, a scoped short-lived credential, or a reversible
representation (draft, queue, staged change) that a separate cheaper action
promotes. A team that cannot move an action down a band has not designed it, it
has only classified it. Escalators and de-escalators in full:
`references/heat-ladder.md`.

## Step 5 · What the mode obliges you to build

Heat sets the ceiling. Patterns and supervision primitives are what let you
approach it — they are not the cost of autonomy, they are what buys it. Read
this as a build order: a product moving an agent up the spectrum usually needs
new patterns, not new model capability.

| Autonomy mode | Trust patterns | Control patterns | Orchestration |
|---|---|---|---|
| **Human-only** | Confidence ribbon, reasoning trace | Permission scope | Activity stream |
| **Approve-each-action** | + source citation, version diff | + escape hatch | + approval queue |
| **Review-before-act** | + dissent surface | + dry-run mode | + intervention point |
| **Act-and-notify** | + calibration cue | + budget governor | + audit trail |
| **Autonomous** | All of the above | + kill switch | + hand-off, parallel session view |

Each row is cumulative. Six supervision primitives run underneath, independent
of mode, and decide whether the accountable human can see, approve and undo what
happened: **agent identity and disclosure** (from LOW), **action receipt** and
**reversal** (from LOW-MED), **consequence-scaled approval**, **escalation
handoff** and **provenance at the decision point** (from MEDIUM). Each is
defined, with the question it answers, in `references/heat-ladder.md`.

Two rules govern whether any of this counts:

> **A recommendation is not a control.** Where a behaviour is something *the
> system does*, it counts. Where it is something *a builder should do*, it does
> not. "We'll add approval gates" in a design doc is not an approval gate.

> **Enforcement lives in a mechanism, not in a prompt.** A prompt saying "only
> update qualification information" is a request. A tool that exposes only the
> qualification field is a boundary.

Apply both to the user's own design review, and say plainly when something they
have described is a recommendation wearing a control's clothes.

## Step 6 · Write the mandate

Refuse vague descriptions such as *semi-autonomous*. Define authority for
specific actions instead — it is easier for business owners to understand and
easier for engineers to implement, which is the whole point.

| Action | Authority | Enforced by | Approver | Heat |
|---|---|---|---|---|
| Read CRM | Autonomous | Scoped read token | — | LOW |
| Update qualification note | Autonomous | Field-scoped write API | — | LOW-MED |
| Draft customer email | Autonomous | Draft-only mailbox scope | — | LOW |
| Send customer email | Human approval | Send scope withheld until approval | Named AE | HIGH |
| Change commercial terms | Human only | Agent has no write path | Deal desk | CRITICAL |
| Offer discount above limit | Prohibited | Hard cap in pricing service | — | CRITICAL |

Four authority values and nothing else: **Autonomous · Human approval · Human
only · Prohibited.** Resist inventing a fifth; ambiguity in that column is where
trust collapses.

The **"Enforced by" column is not optional**. An empty cell means the row is
aspirational, and that column is the difference between a governance document
and a system. It also exposes the gap between **technical capability** (what the
system can physically do) and **assigned authority** (what the business
authorised). An agent whose credentials allow deletion but whose mandate
prohibits it is one prompt injection away from an incident — close that gap in
the credential, not in the instruction.

Blank template: `assets/mandate-template.md`.

## Step 7 · Design the exceptions

Most agent descriptions explain what happens when everything goes right.
Operations depend just as much on what happens when it does not. Force an
explicit decision on each of these nine: a required identifier is missing;
records conflict between systems; a connected tool is unavailable; permissions
are insufficient; confidence is low; a customer disputes the result; a policy
conflict appears; possible fraud is detected; sensitive information appears
unexpectedly.

Seven permitted responses: **retry · stop · ask a human · route the case · use a
fallback · log the event · refuse to continue.**

Two defaults worth arguing about before accepting them. **Retry is the most
over-used response** — retrying a failure caused by insufficient permissions or
conflicting records produces the same failure more expensively and hides the
signal. And **"ask a human" without a named recipient and a time limit is not an
exception handler**, it is a queue that fills up; decide what happens when
nobody answers.

## Step 8 · Evaluate against the ten heuristics

The ten AUX heuristics optimise for quality of relationship rather than clarity
of interface. Before ship, the design needs an explicit answer for each; if H05
(clear boundaries of autonomy) is ambiguous, the surface is not done. After
ship, classify every failure against a heuristic — the histogram tells you where
to invest, and in production failures cluster in H03, H05 and H06.

The ten heuristics, the six patterns you will actually ship, and each pattern's
bad version are in `references/heuristics-and-patterns.md`. Read it before
reviewing or designing any agent-facing surface.

## Step 9 · The production check

Twenty-four questions, run against **one real agent** — ideally the most
consequential one, never the estate in aggregate. Anything the team cannot
answer in under a minute *is* the finding. Scores of 0-7 mean a pilot whatever
its status says; 8-16 means it works and is held together by specific people
rather than by design (the most common and most fragile band); 17-24 means an
agent defensible in front of a client, an auditor or a board.

The full question list and the scoring bands: `references/production-check.md`.
Run it verbatim rather than paraphrasing — the questions are the deliverable,
and softening them is how teams pass a check they should have failed.

## Output format

Produce written artefacts, not advice. Default deliverable, in this order:

1. **Action inventory** — every verb, scored on five dimensions, with the band.
2. **Mandate table** — the six columns above, including "Enforced by".
3. **De-escalation notes** — for each HIGH or CRITICAL action, what would move
   it down a band, or why nothing can.
4. **Exception table** — the nine exceptions, each mapped to one of the seven
   responses, with a named recipient and time limit wherever the answer is
   "ask a human".
5. **Verdict** — the readiness score out of 24, and the two or three gaps that
   most cheaply move it.

Report capability and supervision separately and never combine them into one
score: **the gap between them is the finding**. An agent that can do a great
deal and can be supervised very little is the specific thing worth knowing, and
one number hides it.

## Reference material

- `references/heat-ladder.md` — dimension anchors, escalators and
  de-escalators, the six supervision primitives. Read before scoring anything
  non-obvious.
- `references/heuristics-and-patterns.md` — the ten heuristics and the six
  patterns. Read for step 8, and for any UI or surface review.
- `references/production-check.md` — the twenty-four questions, scoring bands,
  and the twenty-two estate artefacts. Read for step 9 and for any "are we
  production ready" question.
- `references/owners-manual.md` — the ten ownership questions, the fifteen-field
  manual, five forms of human control, four production rules, and the evidence
  on AGENTS.md context files. Read when the work is documentation, handover, or
  governance rather than design.
- `references/workflow-readiness.md` — the three-layer, twelve-check operability
  test. Read **before** designing an agent, when the question is whether the
  work can be delegated at all.
- `references/anti-patterns.md` — named failure modes and precise vocabulary.
  Skim early; it gives you the words to name what you are seeing.
- `references/skill-map.md` — Mermaid map of the whole procedure: trigger,
  nine-step loop, scoring, mandate, exceptions, heuristics, production check,
  owner's manual, artefacts. Read when you need to see how the pieces join.
- `assets/mandate-template.md`, `assets/owners-manual-template.md`,
  `assets/autonomy-map-template.md` — blank artefacts to fill in with the user.
- `scripts/heat.py` — run for scoring. `python scripts/heat.py --score 1,0,3,3,1
  --action "send invoice"` prints the band, the autonomy cap, the required
  patterns and primitives. Use it instead of reading the tables by hand, so the
  hottest-dimension rule is applied mechanically every time.

## Quality bar

A good result is one the accountable human could hand to an auditor: every
action named, every authority value one of the four, every restriction traced to
a mechanism, and every escalation pointed at a person with a deadline.

The failure modes to avoid:

- **Averaging the heat** — happens when five dimensions get summarised into a
  feeling. Take the maximum, always.
- **Producing a governance document instead of a system** — happens when the
  "Enforced by" column stays empty. Push until each row names a token scope, an
  API surface, a hard cap, or a withheld permission.
- **Answering for the estate instead of an agent** — happens when the user says
  "our agents". Pick the most consequential one and answer for it; readiness
  varies enormously and averaging hides the gap.
- **Claiming the agent is safe** — this skill cannot support that claim. It
  tells you whether the organisation can see, approve and undo what the agent
  did. Say that, and not more.
