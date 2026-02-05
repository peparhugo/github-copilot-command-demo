# Repository instructions for GitHub Copilot (JetBrains)

This repository is configured to use **GitHub Copilot repository instructions** and **prompt files** so teams can run reusable command-style prompts from JetBrains.

## How to use

1. Open Copilot Chat in JetBrains.
2. Type `/` and select one of the prompt files from `.github/prompts/`.
3. Optionally provide input text when prompted.

## Command suite in this repository

- `/github-copilot-starter` — scaffold a baseline Copilot setup for a project.
- `/create-specification` — generate an AI-ready specification file.
- `/create-implementation-plan` — generate an execution-ready implementation plan.
- `/create-readme` — generate or improve project README documentation.
- `/review-and-refactor` — review code against local instructions and refactor safely.
- `/pytest-coverage` — drive line-coverage improvements with pytest.
- `/conventional-commit` — produce a standards-compliant conventional commit message.

## Authoring conventions

- Prompt files live in `.github/prompts/` and use `.prompt.md` suffix.
- Prompt files include front matter with at least `description`.
- Keep prompts deterministic and explicit so they perform reliably across repositories.

<!-- Ported and adapted from patterns in: https://github.com/github/awesome-copilot -->
