# AI tutor and local progress

The repository works without an AI assistant. If using one, give it [TUTOR_PROMPT.md](TUTOR_PROMPT.md), the course manifest and the current lesson. This is a prompt guide, not an installed agent skill or automatic external course integration.

The tutor should teach one lesson at a time, check assumptions and accept evidence-based disagreement. It must not manufacture measurements, mark physical validation from a software run or treat Quantum Tensegrity as established physics.

## Local evidence index

```bash
python3 scripts/progress.py list
python3 scripts/progress.py record 16 --evidence outputs/prism.json --note "Numerical equilibrium only; physical validation pending"
```

The record command requires an existing evidence file and writes to ignored `learner-data/progress.json`. Entries are **recorded, not graded**. The helper does not inspect evidence quality or automatically award completion. Use the rubric and reviewer record for that decision. Keep this folder private; the release archive excludes it.

## Useful learning requests

- “Teach lesson 05 using my drawing, and ask me one prediction.”
- “Check my units and load-path diagram without inventing missing numbers.”
- “Review this capstone conclusion against the raw data.”
- “Explain this English lesson in Chinese, preserving the force sign convention.”

Any on-demand translation should be checked for technical meaning. It does not change the release’s language coverage claim.
