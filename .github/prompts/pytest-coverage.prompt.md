<!-- Based on: https://github.com/github/awesome-copilot/blob/main/prompts/pytest-coverage.prompt.md -->
---
agent: 'agent'
description: 'Run pytest with coverage and improve tests to raise line coverage.'
---

Goal: improve test line coverage to the highest practical level.

Suggested command:

```bash
pytest --cov --cov-report=annotate:cov_annotate
```

Workflow:
1. Generate coverage.
2. Inspect uncovered lines in `cov_annotate`.
3. Add targeted tests for uncovered behavior.
4. Re-run tests and coverage until done.
