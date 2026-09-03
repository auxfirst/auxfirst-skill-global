# Anti-patterns and vocabulary

Skim this early. It gives you the words to name what you are seeing, which is
most of the value in a review.

---

## Anti-patterns

Specific, observable failure modes. If you see one, name it out loud — naming
one is more useful to the team than three paragraphs of general advice.

**The autonomy score.** "This agent is 70% autonomous" or "semi-autonomous". It
cannot be implemented, cannot be audited, and hides the one action that matters.
Replace with an action-by-action mandate.

**Prompt as policy.** The boundary exists in the system prompt. It survives
until the first injection, the first model upgrade, or the first user who asks
nicely. Move it into a mechanism.

**The orphan agent.** Owned by a project rather than a person. Orphaned the day
the project closes. Name a human in the business function the agent serves, not
the team that built it — build teams change.

**The shared login.** The agent acts as a service account or, worse, as a named
employee. Every downstream log is now wrong about who did what, and nothing can
be attributed.

**Kill switch as the whole safety story.** Untested, and the only control below
it is nothing. If the first response to surprise is "turn it off", the design
skipped observe, interrupt, approve, and override.

**Happy-path documentation.** Complete specification of what happens when
everything works, and silence on the nine exceptions.

**Averaging the heat.** Scoring an action's five dimensions and taking the mean.
The reason the hottest-dimension rule is stated first.

**The pilot that never had to graduate.** Runs in production, has real users,
and was never held to the twenty-four questions because it is still called a
pilot. Status labels do not change consequence.

**Recommendation mistaken for control.** A specification is not a mechanism. The
most common form of self-deception in design reviews.

**Retry as the universal exception handler.** Turns a signal into a cost.

---

## Vocabulary

Precise definitions, because the loose versions cause the arguments.

- **Agent** — software with three properties: **memory** (recall across
  sessions), **initiative** (can propose and act, not just respond), and
  **judgment** (can choose between options under uncertainty). Subtract any one
  and you are building software, not an agent.
- **AUX (Agentic User Experience)** — the design layer. How humans and agents
  collaborate at the product surface. Classic UX designs for discrete tasks; AUX
  designs for relationships.
- **AX (Agent Experience)** — the API layer. How agents and software systems
  negotiate underneath the surface.
- **Heat** — the consequence of an action, scored on five dimensions.
- **Band** — the heat class of an action, which sets its control posture.
- **Mandate** — assigned authority, action by action. Distinct from technical
  capability.
- **Action receipt** — a per-action record of what changed in the world and on
  whose authority, readable by a non-engineer and available to the person
  affected.
- **Escalation handoff** — a documented route to a **named** human, carrying
  context across, with a time limit and a defined behaviour if nobody answers.
- **Ownership debt** — the gap between an agent that works and an agent the
  organisation can operate, hand over, change, and retire without the people who
  built it.
- **Agent operability** — the capacity of a specific **workflow** to be
  performed by an agent with bounded autonomy, usable context, explicit decision
  rights, and reconstructable accountability. A property of the workflow, not of
  the model or the enterprise.

---

## Two things this skill will not tell you

**It will not tell you an agent is safe.** It tells you whether the organisation
can see, approve, and undo what the agent did. Those are different claims, and
the second is the only one a document can support. Say the second; never imply
the first.

**It will not give you a single score.** Capability and supervision are reported
separately and never combined, because **the gap between them is the finding**.
An agent that can do a great deal and can be supervised very little is the
specific thing worth knowing, and one number would hide it.
