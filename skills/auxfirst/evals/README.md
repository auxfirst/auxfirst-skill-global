# Evaluation material

Excluded from the packaged `.skill` archive, kept in the repo because the next
person to change this skill needs the cases.

- `trigger-eval.json` — 20 queries, 11 positive / 9 negative, for description
  optimisation (`scripts/run_loop.py` in `skill-creator`). The negatives are
  deliberate near-misses: RAG quality, model selection, prompt engineering,
  framework choice and cost tuning all share vocabulary with this skill and all
  belong elsewhere. If they were easy negatives the score would mean nothing.
- `test-prompts.md` — three realistic end-to-end prompts for output evaluation,
  each with what a good answer contains.

Run every test prompt twice: once with the skill available, once without. The
delta is the only evidence that the skill earns its context cost.
