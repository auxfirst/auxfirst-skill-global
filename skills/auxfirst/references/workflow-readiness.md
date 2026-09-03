# Is the workflow even ready?

Read this **before** designing an agent, when the real question is whether the
work can be delegated at all. Running it after the build is how pilots discover
in month four that the blocker was never the model.

Three layers, four checks each. **Any layer where you cannot answer three of
four is where the pilot will stall.**

---

## Layer 01 · Data shape

- Can an agent retrieve every input this workflow needs without a human
  forwarding something?
- Are exceptions and edge cases written down anywhere other than in an
  experienced person's memory?
- Do the systems expose an API, or does the work depend on someone clicking
  through a portal?
- Is there a single authoritative version of the record the work updates?

## Layer 02 · Process design

- Can you list the steps in order, as the workflow actually runs rather than as
  the process doc claims?
- For each step, can you say whether it should be read, drafted, decided, or
  executed by an agent?
- Do you know which steps carry judgment that must stay human, and why?
- Is there a defined outcome that counts as success, and a defined state that
  counts as a dead end?

## Layer 03 · Trust and permissions

- Does the agent have its own identity, or would it act under a person's login?
- Can you state permitted actions individually, rather than as an autonomy
  level?
- Is there an approval point before every consequential action, with a named
  human behind it?
- If someone asked in twelve months what the agent did and why, could you
  reconstruct it from the log?

---

## The ceiling rule

Operability equals the **minimum** across the three layers, not the average. A
capable agent inside an inoperable workflow is still an inoperable system.

## Reading the result

- **Ten or more:** strong candidate. The work is mostly sequencing.
- **Six to nine:** the common case. Gaps are known and fixable.
- **Five or fewer:** valuable to know now rather than two quarters into a pilot.

A low score is not a refusal. It is a list of the specific things to fix first,
and most of them — writing down the exceptions, giving the agent its own
identity, finding the authoritative record — are cheaper than the pilot that
would have failed without them.

**Agent operability** is a property of the *workflow*, not of the model or the
enterprise: the capacity of a specific workflow to be performed by an agent with
bounded autonomy, usable context, explicit decision rights, and reconstructable
accountability.
