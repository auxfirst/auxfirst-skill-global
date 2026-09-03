<div align="center">

# auxfirst

**A Claude skill for building agents an organisation can actually own.**

Score every action an agent can take, cap its autonomy at the hottest dimension,
and write the mandate, exceptions and owner's manual behind it.

[![Skill: validated](https://img.shields.io/badge/skill-validated-2ea44f)](skills/auxfirst/SKILL.md)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)
[![Source: auxfirst.com](https://img.shields.io/badge/source-auxfirst.com-111)](https://auxfirst.com/auxfirst-skill.md)

[Install](#install) · [What it does](#what-it-does) · [The one rule](#the-one-rule-everything-hangs-from) · [Contents](#whats-in-the-box) · [Site](https://auxfirst.github.io/auxfirst-skill-global/)

</div>

---

## What it does

Most agent guidance answers "can the model do this?". This one answers a
different question, the one that actually blocks production:

> **Given an action this agent can take, what does the team owe before it is
> allowed to take it unsupervised?**

You give it an agent — a copilot, an automation, a workflow that writes to a
system of record. It gives you back written artefacts: a scored action
inventory, a mandate with an enforcement mechanism on every row, exception
handling with named recipients and deadlines, and a readiness verdict out of 24.

It is deliberately not a survey of agent design. It assumes the agent can do the
task and asks whether the organisation can own it.

## The one rule everything hangs from

> **An action is as hot as its hottest dimension. No averaging.**

Four cool dials never buy back one hot one. "Send a routine invoice" scores 1 on
reversibility, 0 on blast radius and 1 on authority — and is still a HIGH-band
action, because exposure and commitment are hot. A team scoring by average calls
that low-medium and ships it on auto-run.

```
$ python skills/auxfirst/scripts/heat.py --score 1,0,3,3,1 --action "send an invoice"

  reversibility  1
  blast radius   0
  exposure       3  <- hottest
  commitment     3  <- hottest
  authority      1

  BAND            HIGH  (highest single score, never the mean)
  MAX AUTONOMY    Approve-each-action
  POSTURE         A named accountable human approves each instance before
                  execution, logged with rationale and identity.
```

## Install

**Claude Code — as a plugin** (one command, updates with the repo):

```
/plugin marketplace add auxfirst/auxfirst-skill-global
/plugin install auxfirst@auxfirst
```

**Claude Code — as a plain skill:**

```bash
git clone https://github.com/auxfirst/auxfirst-skill-global.git
ln -s "$PWD/auxfirst-skill-global/skills/auxfirst" ~/.claude/skills/auxfirst
```

Use `.claude/skills/` inside a repository instead of `~/.claude/skills/` to
share it with a team through git.

**Claude.ai / Desktop — as an uploadable `.skill` file:**

```bash
cd /path/to/skill-creator
python -m scripts.package_skill /path/to/auxfirst-skill-global/skills/auxfirst
```

Upload the resulting `auxfirst.skill` and press **Save skill** on the file card.

It fires on its own — no slash command. Ask something like *"we're about to let
the support bot issue refunds instead of drafting them, what do we need first?"*
and it takes over.

## The loop it runs

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

Steps 1-5 are mechanical, and the bundled script does them so nobody quietly
averages. Steps 6-9 are where the judgement lives.

| Band | Control posture | Max autonomy mode |
|---|---|---|
| **LOW** | Auto-run, log everything | Autonomous |
| **LOW-MED** | Auto-run, sampled review, one-click undo | Act-and-notify |
| **MEDIUM** | Propose, then batch-approve | Review-before-act |
| **HIGH** | Named approver, per instance | Approve-each-action |
| **CRITICAL** | Human executes, agent prepares | Human-only |

## What's in the box

```
skills/auxfirst/
├── SKILL.md                              the loop, the tables, the output contract
├── references/
│   ├── heat-ladder.md                    dimension anchors, escalators, de-escalators,
│   │                                     the six supervision primitives
│   ├── heuristics-and-patterns.md        the 10 AUX heuristics, the 6 AUX patterns
│   ├── production-check.md               the 24 questions, scoring bands, 22 artefacts
│   ├── owners-manual.md                  15-field manual, 5 forms of control, AGENTS.md evidence
│   ├── workflow-readiness.md             the 3-layer, 12-check operability test
│   └── anti-patterns.md                  named failure modes and precise vocabulary
├── assets/                               blank mandate, owner's manual, autonomy map
├── scripts/heat.py                       deterministic scoring, no dependencies
└── evals/                                trigger eval set + output test prompts
```

## Two things it will not tell you

**It will not tell you an agent is safe.** It tells you whether the organisation
can see, approve and undo what the agent did. Those are different claims, and
the second is the only one a document can support.

**It will not give you a single score.** Capability and supervision are reported
separately and never combined, because the gap between them is the finding.

## Development

```bash
# validate the skill against the skill-creator rules
python -m scripts.quick_validate skills/auxfirst   # run from the skill-creator directory

# score a batch of actions from a CSV
python skills/auxfirst/scripts/heat.py --file actions.csv --json
```

`evals/` ships in the repo and is excluded from the packaged archive. The
negatives in the trigger eval are deliberate near-misses — RAG quality, model
selection, prompt engineering, cost tuning — because easy negatives make the
score meaningless.

## Provenance

Assembled from published auxfirst material. Each source is the canonical, longer
treatment:

| Component | Source |
|---|---|
| Five dimensions, five bands, escalators | [The Action Heat Ladder](https://auxfirst.com/action-heat-ladder.html) |
| Six supervision primitives, the two scoring rules | [Agent Supervision Method](https://auxfirst.com/news/agent-supervision-method.html) · [the Register](https://auxfirst.com/news/agent-supervision-register.html) |
| Mandate, five controls, nine exceptions, four rules, fifteen fields | [The Agent Owner's Manual](https://auxfirst.com/agent-owners-manual.html) |
| Context-file findings | [AGENTS.md for teams that don't write code](https://auxfirst.com/news/agents-md-for-non-engineering-teams.html) |
| Ten heuristics | [The 10 AUX Heuristics](https://auxfirst.com/heuristics.md) |
| Six patterns, the autonomy-to-pattern mapping | [The Six AUX Patterns](https://auxfirst.com/patterns.md) |
| Twenty-four questions, twenty-two artefacts | [The Agent Development Lifecycle](https://auxfirst.com/agent-development-lifecycle.html) |
| Three layers, twelve-point readiness check | [Agent Operability](https://auxfirst.com/agent-operability-audit.html) |
| Agent definition, AUX/AX stack | [The AUX Manifesto](https://auxfirst.com/manifesto.md) |

**New here, and on no single source page:** the join between heat band and
autonomy mode, the band thresholds for the six supervision primitives, the
"Enforced by" column in the mandate template, the first-five ordering of the
artefact list, and the numeric score-to-band mapping the script applies.

## Licence

[CC BY 4.0](LICENSE) · auxfirst agency 2026. Reuse it, adapt it, keep the
attribution.

---

<div align="center">

*auxfirst designs relationships between users and agents.*
*The agent is a user. The relationship is the product. Trust is the moat.*

**[auxfirst.com](https://auxfirst.com)**

</div>
