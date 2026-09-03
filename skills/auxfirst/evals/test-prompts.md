# Output test prompts

Three prompts, each run with and without the skill. Assertions are written so
they can fail — a no-skill baseline should miss most of them.

---

## 1 · Invoice agent, scoring and mandate

> We have an agent in our billing tool. It reads the timesheet system, works out
> what to bill, drafts the invoice, and emails it to the client. Right now it
> does the whole chain on a schedule with nobody watching. Our CFO asked whether
> that's OK. Is it?

**A good answer:**

- Splits the chain into separate actions rather than judging "the agent"
- Scores at least the send action across all five dimensions
- Lands "send invoice" at HIGH, driven by exposure and commitment, and says
  explicitly that three cool dimensions do not offset them
- Proposes the draft/send split as a de-escalator instead of only saying "add
  approval"
- Names a mechanism for the approval (send scope withheld), not a prompt rule
- Does not claim the agent is safe or unsafe; answers about supervision

---

## 2 · Vague autonomy label in a design doc

> Our internal doc says the deal-desk assistant is "semi-autonomous with a human
> in the loop". Legal signed it off. Engineering says it's meaningless. Who's
> right?

**A good answer:**

- Says engineering is right, and why: the label cannot be implemented or audited
- Replaces it with an action-by-action mandate using exactly the four authority
  values
- Insists on the "Enforced by" column and explains what an empty cell means
- Names the anti-pattern ("the autonomy score") rather than describing it
  vaguely
- Points at the gap between technical capability and assigned authority

---

## 3 · Production readiness on an existing agent

> The ticket triage agent has been live for eight months. It works. My VP wants
> to know if it's "properly in production" before we roll the same pattern out
> to three more teams. What do I check?

**A good answer:**

- Runs the twenty-four questions against that one agent, not the estate
- Treats "we'd have to go and find out" as a failed answer, not a deferral
- Produces a score and maps it to the right band with the band's meaning
- Surfaces question 21 (a drop in escalation rate) as the cheap, high-value fix
- Reports capability and supervision separately rather than as one number
- Recommends the first-five artefact order before the rollout, not all
  twenty-two
