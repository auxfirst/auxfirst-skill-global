# The Agent Owner's Manual

Read this when the work is documentation, handover, or governance rather than
design — and whenever someone asks "who owns this agent?" and the answer is a
team name.

---

## The ten questions

For every important production agent, the organisation should be able to answer:

1. What is it?
2. Why do we have it?
3. Who owns it?
4. What is it allowed to do?
5. What can it technically do?
6. What systems and data does it touch?
7. Where do humans intervene?
8. What happens when it fails?
9. What changed?
10. How do we stop it?

**4 and 5 are separate questions on purpose.** The gap between assigned
authority and technical capability is the single most useful number in the
document, and it is the number nobody produces unless the form forces them to.

---

## The fifteen-field manual

The ten questions are the diagnostic. This is the document that answers them —
a practical minimum, one per agent. For many organisations, simply filling these
in properly exposes the most important gaps.

| # | Field | # | Field |
|---|---|---|---|
| 01 | Agent name | 09 | What it can read |
| 02 | Purpose | 10 | What it can change |
| 03 | Business owner | 11 | Autonomous actions |
| 04 | Technical owner | 12 | Approval-required actions |
| 05 | Trigger | 13 | Prohibited actions |
| 06 | Users | 14 | Escalation path |
| 07 | Data sources | 15 | Shutdown procedure |
| 08 | Connected systems | | |

Fields 11, 12 and 13 are the mandate, transcribed. Fields 09 and 10 are
technical capability. **If 10 is broader than 11+12, that difference is the
attack surface**, and it belongs in the risk register.

**Business owner and technical owner are two fields for a reason.** One named
person in the business function the agent serves, and one who can change how it
works. An agent with only a technical owner is orphaned the day the project
closes.

Blank form: `assets/owners-manual-template.md`.

---

## Five forms of human control

An organisation does not have meaningful oversight merely because someone can
disable the agent. Meaningful control starts earlier:

| # | Control | The question |
|---|---|---|
| 01 | **Observe** | Can a person understand what the agent is doing? |
| 02 | **Interrupt** | Can an active workflow be stopped? |
| 03 | **Approve** | Which consequential actions pause before execution? |
| 04 | **Override** | Can a human replace or correct the agent's decision? |
| 05 | **Disable** | Can the entire agent be taken out of operation? |

When a team's whole safety story is control 05, say so plainly: they skipped
observe, interrupt, approve and override, and the first response to any surprise
is an outage.

---

## Four production rules

Deliberately simple. Use them as gates, not aspirations.

> **No owner → no production.**
> **No mandate → no autonomy.**
> **No visibility → no trust.**
> **No shutdown procedure → no deployment.**

The goal is not to slow adoption. It is to make successful deployments easier to
own, hand over, and scale.

---

## The machine-readable sibling: AGENTS.md

If the agents run inside a workspace, the machine half of this has a convention
already: **AGENTS.md**, the file coding agents read to learn how work is done in
a project. The Owner's Manual is the business-layer companion — the same
questions, addressed to people rather than to the agent.

Worth knowing before writing either. A February 2026 ETH Zurich evaluation
([arXiv:2602.11988](https://arxiv.org/abs/2602.11988)) tested coding agents with
no context file, an LLM-generated one, and a developer-committed one, across
SWE-bench tasks and a fresh set of real repository issues. Four findings that
should change how these files get written:

- Context files **do not generally improve task success rates**
- They **increase inference cost by over 20% on average**
- **Instructions in the files are well followed** by the agents
- **Repository overviews — popular and recommended by model providers — are not
  helpful**

The operational reading: **write instructions, not overviews.** Every line is a
lever the agent will pull, so completeness is not the goal and is not free. A
companion January 2026 study ([arXiv:2601.20404](https://arxiv.org/abs/2601.20404))
measured the same artefact's effect on runtime and token consumption across 10
repositories and 124 pull requests.

Apply the same discipline to the Owner's Manual itself: fifteen fields answered
precisely beats forty answered vaguely.
