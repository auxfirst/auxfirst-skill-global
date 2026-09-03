# The ten AUX heuristics and the six AUX patterns

Read this for step 8 of the core loop, and before reviewing or designing any
surface where a human and an agent meet.

Traditional usability heuristics optimise for clarity of interface. These
optimise for **quality of relationship**. Run a shipped agent feature through
them and expect to find at least three trust gaps.

---

## The ten heuristics

| # | Heuristic | The question |
|---|---|---|
| **H01** | Visibility of agent intent and action | Can the user answer what the agent is trying to do right now, and what it is about to do next? |
| **H02** | Progressive transparency | Does explanation depth match relationship maturity? Trajectory: transparency → summary → confident → silent |
| **H03** | Steering, not micromanagement | Do users guide via intent and correction, rather than step-by-step control? |
| **H04** | Trust is dynamic, not static | Does behaviour evolve as trust develops — and move back down when it fails? |
| **H05** | Clear boundaries of autonomy | At any moment, does the user know what is autonomous, what needs confirmation, and what is blocked? |
| **H06** | Graceful uncertainty and failure | When unsure, does it ask, escalate, or return a partial result — rather than hallucinate? |
| **H07** | Appropriate assertiveness | Does it push back when something seems wrong? Spectrum: compliant → advisory → assertive → protective |
| **H08** | Context efficiency and awareness | Does it use context intelligently rather than exhaustively? |
| **H09** | Multi-actor and multi-agent clarity | Is it always obvious who acted, who delegated, and who owns the outcome? |
| **H10** | Consistency of behaviour, not interface | The surface may adapt. The decision logic, trust boundaries, and tone must not. |

**Before ship:** does the design have an explicit answer for each? If H05 is
ambiguous, the surface is not done — a user who cannot tell what is autonomous
cannot supervise anything.

**After ship:** classify every failure against a heuristic. The histogram tells
you which one to invest in next. In production, failures cluster in H03, H05 and
H06 — loss of user control and transparency gaps — so that is usually where the
largest unrealised wins are.

Using this as a review method: take one real screen or transcript, walk the ten
in order, and write one concrete finding per heuristic or explicitly record
"not applicable and why". A review that produces ten vague observations is worth
less than one that produces three findings with a screenshot attached.

---

## The six patterns

Principles are what you believe. Heuristics are how you evaluate. **Patterns are
what you ship.** Almost every agentic feature is a combination of these six.

| Pattern | What it is | Deploy when | The bad version |
|---|---|---|---|
| **Intent handshake** | The agent restates the goal, names its assumptions, offers a redirect before cost is incurred | The action is non-trivial, expensive, irreversible, or sensitive | Auto-executing on a half-understood request |
| **Confidence cues** | Sources, uncertainty and logic made visible — tapered, not overwhelming | The agent produces an output the user might act on | A raw confidence percentage; users have no statistical intuition to act on it |
| **Adaptive canvas** | The interface reshapes as the task evolves, preserving spatial memory | The task surface changes shape mid-flow | A static UI bolted onto an agentic backend |
| **Escape hatch** | An obvious way to undo, revise, or override. One click, always visible, unambiguous about what it cancels | The agent has authority to act | A single global "stop" that does not say what it stops |
| **Memory in motion** | Recall across time — decisions, formats, corrections — transparent and editable | The agent operates across sessions | Exposing a chat transcript as "memory". That is logs. Real memory editors surface the abstractions the agent formed |
| **Generative momentum** | The agent initiates drafts and candidates, inviting the user to shape them | The user benefits from a starting point | Finished output as the default, with no scaffolding for revision |

A pattern is not a component. A component is reusable code; a pattern is a
reusable **expectation**. Each carries a shape (what the user sees), a contract
(what agent and human each owe), a failure mode, and a trigger. Skip the
contract and the pattern degrades into decoration — an escape hatch nobody
trusts is worse than none, because it advertises a control that does not hold.

---

## Autonomy mode to pattern mapping

Heat sets the ceiling; these are what let you approach it. Each row is
cumulative — "Autonomous" means everything above it plus its own.

| Autonomy mode | Trust patterns | Control patterns | Orchestration |
|---|---|---|---|
| **Human-only** | Confidence ribbon, reasoning trace | Permission scope | Activity stream |
| **Approve-each-action** | + source citation, version diff | + escape hatch | + approval queue |
| **Review-before-act** | + dissent surface | + dry-run mode | + intervention point |
| **Act-and-notify** | + calibration cue | + budget governor | + audit trail |
| **Autonomous** | All of the above | + kill switch | + hand-off, parallel session view |

Read it as a build order. A product moving an agent up the spectrum does not
need new model capability. It needs new patterns.
