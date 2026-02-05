<!-- Based on: https://github.com/github/awesome-copilot/blob/main/prompts/conventional-commit.prompt.md -->
---
agent: 'agent'
description: 'Generate a Conventional Commits message based on staged repository changes.'
---

Generate a conventional commit message from current staged changes.

Workflow:
1. Review changes with `git status` and `git diff --cached`.
2. Produce a commit title in format: `type(scope): description`.
3. Optionally include body and footer for context and breaking changes.

Allowed types:
- feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert

Examples:
- `feat(parser): add ability to parse arrays`
- `fix(ui): correct button alignment`
- `docs: update usage documentation`
