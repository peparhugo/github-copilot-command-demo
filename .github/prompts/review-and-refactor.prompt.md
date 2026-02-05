<!-- Based on: https://github.com/github/awesome-copilot/blob/main/prompts/review-and-refactor.prompt.md -->
---
agent: 'agent'
description: 'Review and refactor repository code according to Copilot and project instructions.'
---

Review the repository and refactor code while preserving behavior.

Steps:
1. Read `.github/copilot-instructions.md` and `.github/instructions/*.instructions.md`.
2. Identify maintainability and clarity issues.
3. Refactor in small, safe changes.
4. Run available tests/checks and fix regressions.
5. Summarize what changed and why.
