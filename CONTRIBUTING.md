# Contributing

The skill lives in `skills/auxfirst/`. Everything else in the repo is packaging,
CI, and the site.

## Before opening a PR

```bash
python tools/validate.py
```

It checks the frontmatter rules the Skills API enforces on upload, that every
bundled file `SKILL.md` points at actually exists, and that `heat.py` still
produces the bands the documentation claims. CI runs the same script.

## Changing the description

The description is the entire triggering mechanism — the body is invisible to
the model until after the skill has been chosen. Treat a description change as
the highest blast-radius edit in the repo:

1. Run the eval set in `skills/auxfirst/evals/trigger-eval.json` against the old
   and new description.
2. Record both scores in the PR body.
3. Keep the old description in the PR description so it can be reverted cleanly.

Descriptions are capped at 1024 characters and may not contain angle brackets.

## Changing the body

- Keep `SKILL.md` under ~500 lines. Past that, move detail into `references/`
  with an explicit read-condition, so it only loads when it is needed.
- Explain *why* an instruction exists rather than issuing a bare rule. Reasoning
  generalises to cases nobody anticipated; a bare rule breaks on the first edge.
- Reserve ALL-CAPS mandates for genuine invariants. There are two here — take
  the maximum, never the mean; and never claim an agent is safe.
- Add or update a case in `evals/test-prompts.md` when a change is meant to
  alter what the output contains.

## Changing the bands or the scoring

`scripts/heat.py`, `references/heat-ladder.md` and the tables in `SKILL.md` must
agree. `tools/validate.py` asserts four known score-to-band mappings; extend
those assertions if you change the mapping deliberately.

## Provenance

The prose is CC BY 4.0 from the auxfirst canon; the scripts are MIT. If it
executes, it is MIT — if a person or a model reads it, it is CC BY 4.0.
Adaptations are welcome; attribution stays.
