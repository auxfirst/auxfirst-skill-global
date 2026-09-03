# The Action Heat Ladder — full reference

Read this when scoring an action whose heat is not obvious, when a user
disputes a band, or when the design work is moving an action down a band.

**Contents:** 1. The rule · 2. Dimension anchors · 3. The five bands in full ·
4. Escalators · 5. De-escalators · 6. The six supervision primitives ·
7. Worked examples

---

## 1. The rule

> **An action is as hot as its hottest dimension. No averaging.**

Four cool dials never buy back one hot one. This is the sentence that stops "but
it's mostly fine" from shipping a disaster, and it is the reason `scripts/heat.py`
takes a maximum rather than a mean.

---

## 2. Dimension anchors

Score the action as the agent would actually perform it, with wrong inputs, not
as policy says it should.

### Reversibility — can we take it back?

| Score | Anchor |
|---|---|
| 0 | Fully undoable, no trace, no cost |
| 1 | Undoable with effort — a credit note, a revert, a correction email |
| 2 | Partially undoable; some effects persist |
| 3 | Undoable only through a process someone else controls |
| 4 | Permanent and unrecoverable |

Score reversibility **in practice, not in theory**. A database write that is
technically reversible but that thirty downstream systems have already consumed
is not a 1.

### Blast radius — how far does it spread?

| Score | Anchor |
|---|---|
| 0 | A single item, record, or message |
| 1 | A handful, bounded and enumerable |
| 2 | One team, one account, one customer's whole footprint |
| 3 | A whole function or segment |
| 4 | The entire estate |

Fan-out is the trap: one call that iterates over a list is scored on the list,
not the call.

### Exposure — who sees it?

| Score | Anchor |
|---|---|
| 0 | Nobody outside the loop |
| 1 | Internal, beyond the operator |
| 2 | A named external party under NDA or contract |
| 3 | A customer or partner; it leaves the building |
| 4 | Public, press, regulators |

### Commitment — what does it bind us to?

| Score | Anchor |
|---|---|
| 0 | Binds nothing |
| 1 | An informal expectation |
| 2 | An operational promise — a date, a fix, a callback |
| 3 | A commercial position stated in the company's name |
| 4 | Legally or financially binding |

### Authority — what is it allowed to touch?

| Score | Anchor |
|---|---|
| 0 | Read-only, scoped |
| 1 | Writes drafts and documents, or a single scoped field in a system of record |
| 2 | Writes broadly to a system of record |
| 3 | Broad write access to production data and infrastructure |
| 4 | Production and permissions — can change who can do what |

Score the **granted** scope, not the intended one. The token is the truth; the
prompt is a wish.

---

### From five scores to one band

Take the **highest single score** and read the band straight off it. There is no
arithmetic beyond the maximum:

| Highest score | Band |
|---|---|
| 0 | LOW |
| 1 | LOW-MED |
| 2 | MEDIUM |
| 3 | HIGH |
| 4 | CRITICAL |

`scripts/heat.py` applies exactly this mapping. Run it rather than eyeballing —
eyeballing is how averaging creeps back in.

---

## 3. The five bands in full

| Band | Control posture | Who does what | Signature | Max autonomy mode |
|---|---|---|---|---|
| **LOW** | Auto-run. Log everything. | The agent acts freely. Outputs reviewable after the fact; the log is the control. | Read-only or draft-only; nothing leaves the building; undo is a non-event | Autonomous |
| **LOW-MED** | Auto-run, sampled review. | The agent acts. A human reviews a sample on a cadence; every write has one-click undo. | Writes to internal systems of record; fully reversible, narrow scope | Act-and-notify |
| **MEDIUM** | Propose, then batch-approve. | The agent queues the action with rationale. A human approves asynchronously, possibly in batches. | Touches a customer or a shared system; reversible with effort | Review-before-act |
| **HIGH** | Named approver, per instance. | A specific accountable human approves each instance before execution, logged with rationale and identity. | External commercial communication; money or access moves; hard to unwind | Approve-each-action |
| **CRITICAL** | Human executes. Agent prepares. | The agent assembles evidence, draft, checklist. A human — sometimes two, dual-control — performs the action. | Irreversible or legally binding; production authority or public exposure | Human-only |

**Example actions per band.** LOW: research and summarise, draft copy or code,
monitor and flag anomalies. LOW-MED: update a CRM field, tag and route tickets,
backfill a derived table. MEDIUM: reply to a routine support ticket, schedule an
approved campaign, restart a stuck service. HIGH: send a quote or invoice, issue
a refund, grant access, merge to main. CRITICAL: sign a contract, deploy to
production, purge data permanently.

---

## 4. Escalators — the action is hotter than its verb suggests

- It is **irreversible in practice** rather than in theory.
- It **fans out** — one call, many records.
- It **reaches an outsider**.
- It is **hard to detect if wrong**. Silent wrongness is hotter than loud
  wrongness, because the control is detection.
- It **runs unattended at volume**. Ten a day and ten thousand a day are
  different actions.
- The agent holds **standing credentials** rather than scoped, expiring ones.

---

## 5. De-escalators — the actual design work

- **Dry-run mode** that shows the diff before anything commits.
- **A hard cap** on volume or value, enforced in the service, not the prompt.
- **A hold window** between decision and execution, long enough for a human or a
  monitor to intervene.
- **A scoped credential with a short life**, issued per task.
- **A reversible representation** — draft, queue, staged change — that a
  separate, cheaper action promotes to the real thing.

The last one is the most powerful and the most under-used: splitting a hot
action into a cool one plus a tiny hot one shrinks the surface that needs
approval to almost nothing. "Draft the invoice" is LOW; "send the drafted
invoice" is HIGH but takes two seconds to approve.

A team that cannot move an action down a band has not designed it; it has only
classified it.

---

## 6. The six supervision primitives

Independent of mode, these decide whether the accountable human can see,
approve, and undo what the agent did. They are the criteria auxfirst uses to
score commercial platforms, restated as things to build.

| Primitive | The question it answers | Required from band |
|---|---|---|
| **Agent identity and disclosure** | Can a human tell which agent acted, on whose authority, and that it was not a person? | LOW — always |
| **Action receipt** | Is there a per-action record a non-engineer can read afterwards, available to the person affected? | LOW-MED |
| **Reversal** | Can the action be undone, and how far back does that reach? | LOW-MED |
| **Consequence-scaled approval** | Can approval requirements be set by how costly the action is, rather than on or off per agent? | MEDIUM |
| **Escalation handoff** | Is there a documented route to a named human when the agent is out of its depth, carrying context across? | MEDIUM |
| **Provenance at the decision point** | Are sources and uncertainty shown where the human decides, rather than buried in a log? | MEDIUM |

The band thresholds in the right-hand column are this skill's synthesis of the
Action Heat Ladder and the supervision criteria; the criteria themselves are the
published scoring method.

**Two rules decide whether a claimed primitive counts.**

> **A recommendation is not a control.** Where a behaviour is something *the
> system does*, it counts. Where it is something *a builder should do*, it does
> not. A platform — or an internal architecture document — that publishes an
> excellent specification and leaves implementation to whoever gets there first
> has done something genuinely valuable and has not shipped a control.

> **Enforcement lives in a mechanism, not in a prompt.** Every "prohibited" and
> every "human approval" needs a mechanism named next to it, or it is
> decoration.

---

## 7. Worked examples

### Send a routine invoice to a client

| Dimension | Score | Why |
|---|---|---|
| Reversibility | 1 | A credit note fixes it, with effort |
| Blast radius | 0 | One customer |
| Exposure | 3 | Leaves the building, reaches an outsider |
| Commitment | 3 | Asks for money in the company's name |
| Authority | 1 | Reads billing, writes a document |

Max = 3 → **HIGH** → approve-each-action, named approver per instance. Three
dials are cool and it does not matter.

### Update a CRM qualification note

| Dimension | Score | Why |
|---|---|---|
| Reversibility | 0 | Field history restores the prior value |
| Blast radius | 0 | One record |
| Exposure | 1 | Internal only |
| Commitment | 0 | Binds nothing |
| Authority | 1 | Writes one scoped field in a system of record |

Max = 1 → **LOW-MED** → act-and-notify: auto-run with sampled review and
one-click undo. Note what would change this. If the same agent held a token that
could write any CRM field, Authority becomes 2 and the action is MEDIUM —
propose-then-approve — without a single line of its behaviour changing. The
credential moved the band, not the intent.

### Grant a user access to a production system

| Dimension | Score | Why |
|---|---|---|
| Reversibility | 2 | Revocable, but anything read stays read |
| Blast radius | 3 | Whatever that access reaches |
| Exposure | 1 | Internal |
| Commitment | 0 | Binds nothing contractually |
| Authority | 4 | Changes who can do what |

Max = 4 → **CRITICAL** → human-only. The agent prepares the request, the
evidence and the checklist; a human grants.
