# auxfirst skill — visual map

Read this when you need to see the whole procedure at once: when it fires, the
nine-step loop, what each step produces, and how the supporting frameworks
connect. The diagrams are Mermaid. Paste any fenced block into
[mermaid.live](https://mermaid.live) if the renderer in front of you truncates.

**The question the skill answers.** Given an action this agent can take, what
does the team owe before it is allowed to take it unsupervised?

**The rule everything hangs from.** An action is as hot as its hottest
dimension. No averaging.

---

## 1. Whole-system map

Trigger, pre-check, the nine-step loop, artefacts, and the two claims the skill
refuses to make.

```mermaid
flowchart TB
  subgraph TRIGGER["When the skill fires"]
    Q["Someone is designing, reviewing or fixing<br/>an agent that writes, sends, spends or grants"]
    ASK["How autonomous should it be?<br/>HITL / semi-autonomous / guardrails / AGENTS.md"]
    STALL["Pilot demos well, stalls before production,<br/>or died in security review"]
    GOV["Writing agent governance, AI policy,<br/>vendor requirements, or platform eval"]
    AFTER["Deciding what to change after a bad outcome"]
  end

  subgraph OUT["Out of scope — do not use"]
    NO1["Prompt engineering"]
    NO2["Model selection"]
    NO3["RAG quality"]
    NO4["Cost optimisation"]
    NO5["Framework choice"]
  end

  subgraph PRE["Before the loop — can this work even be delegated?"]
    W1["Layer 01 Data shape — 4 checks"]
    W2["Layer 02 Process design — 4 checks"]
    W3["Layer 03 Trust and permissions — 4 checks"]
    WMIN["Operability = MIN of three layers, not the average"]
  end

  subgraph LOOP["The core loop — work per ACTION, never per agent"]
    S1["1 LIST the verbs"]
    S2["2 SCORE five dimensions 0-4"]
    S3["3 BAND = max, never mean"]
    S4["4 CAP max autonomy mode"]
    S5["5 OWE patterns + primitives"]
    S6["6 WRITE the mandate"]
    S7["7 EXCEPT nine failure modes"]
    S8["8 EVALUATE ten AUX heuristics"]
    S9["9 CHECK twenty-four production questions"]
    MECH["Steps 1-5: mechanical — run scripts/heat.py"]
    JUDGE["Steps 6-9: judgement — this is where attention goes"]
  end

  subgraph ARTEFACTS["Default deliverable — written artefacts, not advice"]
    A1["Action inventory"]
    A2["Mandate table with Enforced by"]
    A3["De-escalation notes for HIGH and CRITICAL"]
    A4["Exception table: 9 x 7 responses"]
    A5["Verdict: readiness /24 + cheapest 2-3 gaps"]
  end

  subgraph REFUSE["Two things this skill will not tell you"]
    R1["It will not tell you an agent is safe"]
    R2["It will not give you a single score"]
    R3["Capability and supervision stay separate.<br/>The gap between them is the finding."]
  end

  Q --> ASK & STALL & GOV & AFTER
  ASK --> W1
  STALL --> W1
  GOV --> W1
  AFTER --> W1
  W1 --> W2 --> W3 --> WMIN --> S1
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
  S1 -.-> MECH
  S5 -.-> MECH
  S6 -.-> JUDGE
  S9 -.-> JUDGE
  S9 --> A1 & A2 & A3 & A4 & A5
  A5 --> R1 & R2
  R1 --> R3
  R2 --> R3
```

---

## 2. Trigger vs. near-miss

The description is the entire triggering mechanism. Easy negatives (RAG, model
choice, cost) are deliberate, because easy negatives make an eval score
meaningless.

```mermaid
flowchart LR
  subgraph YES["DO use"]
    Y1["Writes to a system of record"]
    Y2["Emails customers"]
    Y3["Moves money"]
    Y4["Grants access"]
    Y5["Merges code"]
    Y6["Approval gates"]
    Y7["Guardrails / kill switches"]
    Y8["Audit trails"]
    Y9["Escalation paths"]
    Y10["Agent ownership / AGENTS.md"]
  end

  subgraph NO["DO NOT use"]
    N1["Prompt engineering"]
    N2["Model selection"]
    N3["RAG quality"]
    N4["Cost optimisation"]
    N5["Framework choice"]
  end

  ASSUME["Assumes the agent works.<br/>Asks whether the organisation can own it."]
  YES --> ASSUME
  NO -.->|near-miss — skill stays silent| X["Not this skill"]
```

---

## 3. Workflow readiness — three layers, twelve checks

Run **before** designing an agent. Any layer where you cannot answer three of
four is where the pilot will stall. A low score is a list of cheaper fixes, not
a refusal.

```mermaid
flowchart TB
  START["Is the workflow even ready to be delegated?"]

  subgraph L1["Layer 01 — Data shape"]
    D1["Can an agent retrieve every input without a human forwarding?"]
    D2["Are exceptions written down outside one person's memory?"]
    D3["Do systems expose an API, or is it portal-clicking?"]
    D4["Is there a single authoritative record?"]
  end

  subgraph L2["Layer 02 — Process design"]
    P1["Can you list the steps as they actually run?"]
    P2["For each step: read, draft, decide, or execute?"]
    P3["Which steps carry judgment that must stay human, and why?"]
    P4["Defined success outcome AND defined dead end?"]
  end

  subgraph L3["Layer 03 — Trust and permissions"]
    T1["Does the agent have its own identity, not a person's login?"]
    T2["Permitted actions listed individually, not as an autonomy level?"]
    T3["Approval point before every consequential action, named human?"]
    T4["Could you reconstruct what it did and why in twelve months?"]
  end

  RULE["Ceiling: operability equals the MINIMUM across layers, not the average"]
  HI["10 or more: strong candidate — the work is mostly sequencing"]
  MID["6 to 9: common case — gaps known and fixable"]
  LO["5 or fewer: valuable to know now rather than two quarters into a pilot"]

  START --> L1 --> L2 --> L3 --> RULE
  RULE --> HI & MID & LO
```

---

## 4. Core loop — nine steps, per action

An agent that can do nine things has nine answers. Averaging them is the
mistake this skill exists to prevent.

```mermaid
flowchart LR
  subgraph MECHANICAL["Mechanical — heat.py, never hand lookup"]
    direction TB
    L["1 LIST verbs"]
    SC["2 SCORE 0-4 x5"]
    B["3 BAND = max"]
    C["4 CAP mode"]
    O["5 OWE patterns"]
    L --> SC --> B --> C --> O
  end

  subgraph JUDGEMENT["Judgement — do not skip"]
    direction TB
    W["6 WRITE mandate"]
    E["7 EXCEPT failures"]
    H["8 EVALUATE heuristics"]
    P["9 CHECK production"]
    W --> E --> H --> P
  end

  MECHANICAL --> JUDGEMENT
  P --> OUT["Artefacts a named human<br/>could hand to an auditor"]
```

---

## 5. Scoring — five dimensions, anchors 0 and 4

Score the action **as the agent would actually perform it**, with wrong inputs,
on **granted** scope (the token is the truth; the prompt is a wish).

```mermaid
flowchart TB
  ACT["One verb, as actually performed — not the happy path, not intended scope"]

  subgraph DIM["Five dimensions, each 0 cool to 4 hot"]
    REV["Reversibility<br/>0 fully undoable — 4 permanent, unrecoverable"]
    BLAST["Blast radius<br/>0 single item — 4 the whole estate"]
    EXP["Exposure<br/>0 nobody outside the loop — 4 public, press, regulators"]
    COM["Commitment<br/>0 binds nothing — 4 legally or financially binding"]
    AUTH["Authority<br/>0 read-only — 4 production AND permissions"]
  end

  MISTAKES["Three scoring mistakes to catch<br/>1. Scoring the happy path<br/>2. Scoring intended scope instead of granted scope<br/>3. Splitting one action to cool it down"]

  MAX["BAND = highest SINGLE score. Four cool dials never buy back one hot one."]

  ACT --> REV & BLAST & EXP & COM & AUTH
  REV & BLAST & EXP & COM & AUTH --> MAX
  ACT -.-> MISTAKES
```

### Dimension anchors in full

```mermaid
flowchart LR
  subgraph REV["Reversibility"]
    R0["0 Fully undoable, no trace, no cost"]
    R1["1 Undoable with effort: credit note, revert"]
    R2["2 Partially undoable; some effects persist"]
    R3["3 Undoable only through a process someone else controls"]
    R4["4 Permanent and unrecoverable"]
    R0 --> R1 --> R2 --> R3 --> R4
  end

  subgraph BLAST["Blast radius"]
    B0["0 Single item, record, or message"]
    B1["1 A handful, bounded and enumerable"]
    B2["2 One team, account, or customer footprint"]
    B3["3 A whole function or segment"]
    B4["4 The entire estate"]
    B0 --> B1 --> B2 --> B3 --> B4
  end

  subgraph EXP["Exposure"]
    E0["0 Nobody outside the loop"]
    E1["1 Internal, beyond the operator"]
    E2["2 Named external party under NDA or contract"]
    E3["3 Customer or partner — it leaves the building"]
    E4["4 Public, press, regulators"]
    E0 --> E1 --> E2 --> E3 --> E4
  end

  subgraph COM["Commitment"]
    C0["0 Binds nothing"]
    C1["1 Informal expectation"]
    C2["2 Operational promise: date, fix, callback"]
    C3["3 Commercial position in the company's name"]
    C4["4 Legally or financially binding"]
    C0 --> C1 --> C2 --> C3 --> C4
  end

  subgraph AUTH["Authority — granted token, not prompt"]
    A0["0 Read-only, scoped"]
    A1["1 Drafts, documents, or one scoped field"]
    A2["2 Writes broadly to a system of record"]
    A3["3 Broad write to production data and infra"]
    A4["4 Can change who can do what"]
    A0 --> A1 --> A2 --> A3 --> A4
  end
```

---

## 6. Band → control posture → autonomy ceiling

The band is a **ceiling, not a target**. Design work is moving an action *down*
a band with de-escalators.

```mermaid
flowchart TB
  PEAK["Highest dimension score"]

  PEAK -->|0| LOW["LOW — Auto-run, log everything<br/>Signature: read-only or draft-only; nothing leaves; undo is a non-event<br/>Max mode: Autonomous"]
  PEAK -->|1| LM["LOW-MED — Auto-run, sampled review, one-click undo<br/>Signature: internal writes; fully reversible; narrow scope<br/>Max mode: Act-and-notify"]
  PEAK -->|2| MED["MEDIUM — Propose, then batch-approve<br/>Signature: customer or shared system; reversible with effort<br/>Max mode: Review-before-act"]
  PEAK -->|3| HIGH["HIGH — Named approver, per instance<br/>Signature: external commercial comms; money or access moves<br/>Max mode: Approve-each-action"]
  PEAK -->|4| CRIT["CRITICAL — Human executes, agent prepares<br/>Signature: irreversible or legally binding; production authority<br/>Max mode: Human-only"]

  LOW --> EXL["Examples: research, draft copy or code, flag anomalies"]
  LM --> EXLM["Examples: update a CRM field, tag and route tickets"]
  MED --> EXM["Examples: reply to a routine ticket, restart a stuck service"]
  HIGH --> EXH["Examples: send a quote or invoice, issue a refund, grant access, merge to main"]
  CRIT --> EXC["Examples: sign a contract, deploy to production, purge data"]
```

---

## 7. Escalators and de-escalators

Classification without a de-escalator is not design.

```mermaid
flowchart LR
  subgraph UP["Escalators — hotter than the verb suggests"]
    U1["Irreversible in practice, not in theory"]
    U2["Fans out: one call, many records"]
    U3["Reaches an outsider"]
    U4["Hard to detect if wrong — silent wrongness is hotter"]
    U5["Runs unattended at volume"]
    U6["Standing credentials instead of scoped, expiring ones"]
  end

  ACTION["The classified action"]

  subgraph DOWN["De-escalators — the actual design work"]
    D1["Dry-run that shows the diff"]
    D2["Hard cap on volume or value, in the service"]
    D3["Hold window long enough to intervene"]
    D4["Scoped short-lived credential, issued per task"]
    D5["Reversible representation: draft, queue, staged change<br/>that a cheaper action promotes"]
  end

  UP --> ACTION
  ACTION --> DOWN
  D5 --> SPLIT["Most powerful: split a hot action into a cool one plus a tiny hot one<br/>Draft invoice = LOW. Send the drafted invoice = HIGH, two seconds to approve."]
```

---

## 8. What the mode obliges you to build

Heat sets the ceiling. Patterns buy the approach. Each row is **cumulative**.
A product moving up the spectrum needs new patterns, not new model capability.

```mermaid
flowchart TB
  subgraph CUMULATIVE["Build order — each mode includes everything above it"]
    HO["Human-only<br/>Trust: confidence ribbon, reasoning trace<br/>Control: permission scope<br/>Orchestration: activity stream"]
    AEA["Approve-each-action<br/>+ source citation, version diff<br/>+ escape hatch<br/>+ approval queue"]
    RBA["Review-before-act<br/>+ dissent surface<br/>+ dry-run mode<br/>+ intervention point"]
    AAN["Act-and-notify<br/>+ calibration cue<br/>+ budget governor<br/>+ audit trail"]
    AUT["Autonomous<br/>+ kill switch<br/>+ hand-off, parallel session view"]
    HO --> AEA --> RBA --> AAN --> AUT
  end

  subgraph TWO["Two rules — does a claimed control count?"]
    R1["A recommendation is not a control.<br/>If the system does it, it counts. If a builder should do it, it does not."]
    R2["Enforcement lives in a mechanism, not in a prompt.<br/>A field-scoped tool is a boundary. A prompt is a request."]
  end

  AUT --> TWO
```

---

## 9. Six supervision primitives

Independent of mode. They decide whether the accountable human can see, approve,
and undo what happened.

```mermaid
flowchart TB
  subgraph ALWAYS["From LOW — always"]
    P1["Agent identity and disclosure<br/>Which agent acted, on whose authority, and that it was not a person?"]
  end

  subgraph FROM_LM["From LOW-MED"]
    P2["Action receipt<br/>Per-action record a non-engineer can read, available to the person affected"]
    P3["Reversal<br/>Can it be undone, and how far back does that reach?"]
  end

  subgraph FROM_MED["From MEDIUM"]
    P4["Consequence-scaled approval<br/>Requirements set by how costly the action is, not on/off per agent"]
    P5["Escalation handoff<br/>Named human, context carried across, time limit, behaviour if nobody answers"]
    P6["Provenance at the decision point<br/>Sources and uncertainty shown where the human decides, not buried in a log"]
  end

  ALWAYS --> FROM_LM --> FROM_MED
```

---

## 10. Mandate — four authority values, nothing else

Refuse *semi-autonomous*. Define authority for specific actions. The
**Enforced by** column is not optional: an empty cell means the row is
aspirational.

```mermaid
flowchart TB
  INV["Scored action inventory"] --> TABLE["Mandate table"]

  subgraph COLS["Six columns"]
    C1["Action"]
    C2["Authority — exactly four values"]
    C3["Enforced by — token, API, hard cap, or withheld permission"]
    C4["Approver"]
    C5["Heat"]
  end

  subgraph AUTH["Four authority values. Resist inventing a fifth."]
    V1["Autonomous"]
    V2["Human approval"]
    V3["Human only"]
    V4["Prohibited"]
  end

  subgraph GAP["Capability vs assigned authority"]
    TECH["Technical capability: what the credentials can physically do"]
    ASN["Assigned authority: what the business authorised"]
    RISK["If capability is broader than the mandate, that gap is the attack surface.<br/>Close it in the credential, not in the instruction."]
  end

  TABLE --> COLS
  TABLE --> AUTH
  TABLE --> GAP
  TECH --> RISK
  ASN --> RISK
```

Worked mandate shape (from SKILL.md):

```mermaid
flowchart LR
  subgraph ROWS["Example rows"]
    R1["Read CRM — Autonomous — scoped read token — LOW"]
    R2["Update qualification note — Autonomous — field-scoped write API — LOW-MED"]
    R3["Draft customer email — Autonomous — draft-only mailbox — LOW"]
    R4["Send customer email — Human approval — send scope withheld — named AE — HIGH"]
    R5["Change commercial terms — Human only — no write path — Deal desk — CRITICAL"]
    R6["Offer discount above limit — Prohibited — hard cap in pricing service — CRITICAL"]
  end
```

---

## 11. Exceptions — nine situations, seven responses

Most agent descriptions explain the happy path. Operations depend on the other
nine.

```mermaid
flowchart TB
  subgraph NINE["Force an explicit decision on each"]
    X1["1 Required identifier missing"]
    X2["2 Records conflict between systems"]
    X3["3 Connected tool unavailable"]
    X4["4 Permissions insufficient"]
    X5["5 Confidence is low"]
    X6["6 Customer disputes the result"]
    X7["7 Policy conflict"]
    X8["8 Possible fraud detected"]
    X9["9 Sensitive information appears unexpectedly"]
  end

  subgraph SEVEN["Seven permitted responses — nothing else"]
    Y1["retry"]
    Y2["stop"]
    Y3["ask a human"]
    Y4["route the case"]
    Y5["use a fallback"]
    Y6["log the event"]
    Y7["refuse to continue"]
  end

  subgraph DEFAULTS["Two defaults worth arguing about"]
    D1["Retry is the most over-used response.<br/>Retrying insufficient permissions or conflicting records hides the signal."]
    D2["Ask a human without a named recipient AND a time limit is not a handler.<br/>Decide what happens when nobody answers."]
  end

  NINE --> SEVEN --> DEFAULTS
```

---

## 12. Ten AUX heuristics

Optimise for **quality of relationship**, not clarity of interface. If H05 is
ambiguous, the surface is not done. In production, failures cluster in H03,
H05 and H06.

```mermaid
flowchart TB
  subgraph H["Walk one real screen or transcript. One concrete finding per heuristic, or N/A and why."]
    H01["H01 Visibility of agent intent and action"]
    H02["H02 Progressive transparency<br/>transparency then summary then confident then silent"]
    H03["H03 Steering, not micromanagement"]
    H04["H04 Trust is dynamic, not static"]
    H05["H05 Clear boundaries of autonomy — if ambiguous, not done"]
    H06["H06 Graceful uncertainty and failure"]
    H07["H07 Appropriate assertiveness<br/>compliant then advisory then assertive then protective"]
    H08["H08 Context efficiency and awareness"]
    H09["H09 Multi-actor and multi-agent clarity"]
    H10["H10 Consistency of behaviour, not interface"]
  end

  BEFORE["Before ship: explicit answer for each"]
  AFTER["After ship: classify every failure against a heuristic. The histogram is the investment map."]
  H --> BEFORE
  H --> AFTER
```

---

## 13. Six AUX patterns — what you actually ship

Principles are beliefs. Heuristics evaluate. Patterns are what you ship. Each
has a shape, a contract, a failure mode, and a trigger. Skip the contract and
the pattern degrades into decoration.

```mermaid
flowchart TB
  subgraph PAT["Almost every agentic feature is a combination of these six"]
    P1["Intent handshake<br/>Restate goal, name assumptions, offer redirect before cost<br/>Bad: auto-executing on a half-understood request"]
    P2["Confidence cues<br/>Sources, uncertainty and logic — tapered, not a raw percentage"]
    P3["Adaptive canvas<br/>UI reshapes as the task evolves, preserving spatial memory<br/>Bad: static UI bolted onto an agentic backend"]
    P4["Escape hatch<br/>Undo, revise, or override. One click, always visible, unambiguous<br/>Bad: a global stop that does not say what it stops"]
    P5["Memory in motion<br/>Recall of decisions, formats, corrections — transparent and editable<br/>Bad: exposing a chat transcript as memory"]
    P6["Generative momentum<br/>Drafts and candidates the user shapes<br/>Bad: finished output as the default, no scaffolding for revision"]
  end
```

---

## 14. Production check — twenty-four questions, one real agent

Anything the team cannot answer in under a minute **is** the finding. Never
score the estate in aggregate.

```mermaid
flowchart TB
  subgraph Q["Twenty-four questions — run verbatim"]
    subgraph OWN["Ownership / identity / source"]
      Q01["01 Accountable human, not a team?"]
      Q05["05 Own identity, not a shared account?"]
      Q06["06 Behaviour in version control?"]
      Q07["07 Model version pinned?"]
      Q08["08 ABOM for the running version?"]
    end
    subgraph BND["Boundaries / guardrails"]
      Q02["02 Written autonomy map, readable outside the code?"]
      Q03["03 Hottest action written down?"]
      Q04["04 Limits enforced by mechanism, not prompt?"]
    end
    subgraph REL["Evaluation / release"]
      Q09["09 Evaluation suite, and when did it last grow?"]
      Q10["10 Behavioural regression before model upgrades?"]
      Q11["11 Behaviour changelog for users of the agent?"]
      Q12["12 Roll back to last known-good today?"]
    end
    subgraph SUP["Containment / supervision / escalation"]
      Q13["13 Kill switch you have actually tested?"]
      Q14["14 Which actions are irreversible?"]
      Q15["15 How many actions between human checks?"]
      Q16["16 Who reviews, and how long per month?"]
      Q17["17 Escalation: named recipient and time limit?"]
      Q18["18 What if nobody answers?"]
    end
    subgraph EVD["Evidence / economics / lifecycle"]
      Q19["19 Reconstruct any single action from last month?"]
      Q20["20 Every consequential action leaves a receipt?"]
      Q21["21 Would you detect a DROP in escalation rate?"]
      Q22["22 Cost per unit of work, including review?"]
      Q23["23 Has an incident become an evaluation case?"]
      Q24["24 Retirement procedure, including revoking access?"]
    end
  end

  subgraph SCORE["Scoring bands"]
    S1["0-7: a pilot, whatever its status says"]
    S2["8-16: works, held together by specific people — most common, most fragile"]
    S3["17-24: defensible in front of a client, an auditor, or a board"]
  end

  Q --> SCORE
  Q21 --> NOTE["Q21 is the cheap high-value fix:<br/>an agent that stops escalating looks identical to one that got better"]
```

---

## 15. Estate artefacts — first five, then twenty-two

Do not build all twenty-two for agent one. The first five make an agent
defensible. The rest become necessary as the estate grows.

```mermaid
flowchart TB
  subgraph FIRST["Minimum for agent one — this order"]
    F1["1 Agent manifest"] --> F2["2 Autonomy map"] --> F3["3 Gateway policy"] --> F4["4 Action receipts"] --> F5["5 Evaluation suite"]
  end

  subgraph REST["The rest of the twenty-two"]
    R1["Architecture diagram"]
    R2["Decision record"]
    R3["Agent stack"]
    R4["Inventory"]
    R5["Radar"]
    R6["ABOM"]
    R7["Bundle and registry"]
    R8["Behaviour changelog"]
    R9["Transcripts and traces"]
    R10["Catalog"]
    R11["CMDB"]
    R12["Service levels and trust budget"]
    R13["Runbooks and playbooks"]
    R14["Postmortems"]
    R15["Risk register"]
    R16["Behavioural debt register"]
    R17["Portfolio review"]
  end

  FIRST --> REST
```

---

## 16. Owner's manual — handover and governance

Use when the work is documentation rather than design, or when "who owns this?"
answers with a team name.

```mermaid
flowchart TB
  subgraph TEN["Ten questions the organisation must be able to answer"]
    T1["1 What is it?"]
    T2["2 Why do we have it?"]
    T3["3 Who owns it?"]
    T4["4 What is it allowed to do?"]
    T5["5 What can it technically do?"]
    T6["6 What systems and data does it touch?"]
    T7["7 Where do humans intervene?"]
    T8["8 What happens when it fails?"]
    T9["9 What changed?"]
    T10["10 How do we stop it?"]
  end

  GAP["4 and 5 are separate on purpose.<br/>The gap is the single most useful number in the document."]

  subgraph FIFTEEN["Fifteen-field manual"]
    M1["01-08 name, purpose, business owner, technical owner, trigger, users, data, systems"]
    M2["09-10 what it can read / change — technical capability"]
    M3["11-13 autonomous / approval-required / prohibited — the mandate transcribed"]
    M4["14-15 escalation path / shutdown procedure"]
  end

  subgraph CTRL["Five forms of human control — disable is not the whole story"]
    C1["01 Observe"] --> C2["02 Interrupt"] --> C3["03 Approve"] --> C4["04 Override"] --> C5["05 Disable"]
  end

  subgraph RULES["Four production rules — gates, not aspirations"]
    G1["No owner → no production"]
    G2["No mandate → no autonomy"]
    G3["No visibility → no trust"]
    G4["No shutdown procedure → no deployment"]
  end

  TEN --> GAP --> FIFTEEN
  FIFTEEN --> CTRL
  FIFTEEN --> RULES
  MANUAL["Owner's Manual — people"] -.->|workspace sibling| AG["AGENTS.md — the machine"]
```

---

## 17. Quality bar and named failure modes

A good result is one the accountable human could hand to an auditor: every
action named, every authority one of the four, every restriction traced to a
mechanism, every escalation pointed at a person with a deadline.

```mermaid
flowchart TB
  subgraph AVOID["Failure modes to avoid while running the skill"]
    F1["Averaging the heat"]
    F2["Governance document instead of a system — empty Enforced by"]
    F3["Answering for the estate instead of one agent"]
    F4["Claiming the agent is safe"]
  end

  subgraph ANTI["Named anti-patterns — say them out loud"]
    A1["The autonomy score / semi-autonomous"]
    A2["Prompt as policy"]
    A3["The orphan agent"]
    A4["The shared login"]
    A5["Kill switch as the whole safety story"]
    A6["Happy-path documentation"]
    A7["Averaging the heat"]
    A8["The pilot that never had to graduate"]
    A9["Recommendation mistaken for control"]
    A10["Retry as the universal exception handler"]
  end

  AVOID --> ANTI
```

---

## 18. Worked example — send a routine invoice

Three dials are cool. The action is still HIGH. A team scoring by average would
have called this low-medium and shipped it on auto-run.

```mermaid
flowchart TB
  ACT["Action: send a routine invoice to a client"]

  subgraph SCORES["Dimension scores"]
    R["Reversibility 1 — credit note fixes it, with effort"]
    B["Blast radius 0 — one customer"]
    E["Exposure 3 — leaves the building  HOTTEST"]
    C["Commitment 3 — asks for money in the company's name  HOTTEST"]
    A["Authority 1 — reads billing, writes a document"]
  end

  MAX["max = 3  →  BAND HIGH  →  Approve-each-action<br/>Named approver per instance, logged with rationale and identity"]
  OWE["Owes every pattern from Human-only through Approve-each-action<br/>plus primitives through MEDIUM"]
  DE["De-escalator: draft the invoice autonomously (LOW),<br/>send the drafted invoice with a two-second approval (HIGH)"]

  ACT --> SCORES --> MAX --> OWE --> DE
```

---

## 19. Files the skill loads

```mermaid
flowchart TB
  SK["SKILL.md — the loop, the tables, the output contract"]

  subgraph REF["references/ — load on read-condition"]
    HL["heat-ladder.md — anchors, escalators, primitives"]
    HP["heuristics-and-patterns.md — 10 heuristics, 6 patterns"]
    PC["production-check.md — 24 questions, 22 artefacts"]
    OM["owners-manual.md — 15 fields, 5 controls, AGENTS.md"]
    WR["workflow-readiness.md — 3x4 operability test"]
    AP["anti-patterns.md — named failure modes and vocabulary"]
    SM["skill-map.md — this visual map"]
  end

  subgraph ASSETS["assets/ — blank artefacts to fill with the user"]
    MT["mandate-template.md"]
    OT["owners-manual-template.md"]
    AT["autonomy-map-template.md"]
  end

  subgraph CODE["scripts/"]
    HT["heat.py — deterministic max, never mean<br/>--score 1,0,3,3,1 --action send invoice"]
  end

  SK --> REF
  SK --> ASSETS
  SK --> CODE
  S1["Steps 1-5"] --> HT
  S2["Step 6"] --> MT
  S3["Handover"] --> OT
  S4["Plain-language mandate"] --> AT
```

---

## 20. Vocabulary used throughout

```mermaid
mindmap
  root((auxfirst))
    Agent
      memory
      initiative
      judgment
    AUX
      Agentic User Experience
      relationship, not discrete task
    AX
      Agent Experience
      API layer underneath
    Heat
      consequence of an action
      five dimensions
    Band
      heat class
      sets control posture
    Mandate
      assigned authority per action
      distinct from capability
    Action receipt
      what changed, on whose authority
      readable by a non-engineer
    Escalation handoff
      named human
      time limit
      behaviour if nobody answers
    Ownership debt
      works vs can be operated, handed over, changed, retired
    Agent operability
      property of the workflow
      not of the model or the enterprise
```
