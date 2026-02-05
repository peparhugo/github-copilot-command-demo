# github-copilot-command-demo

Demo repository that configures **GitHub Copilot repository instructions** and a **suite of reusable prompt commands** for JetBrains.

## Included Copilot command suite

The command prompts are stored in `.github/prompts/`:

- `github-copilot-starter.prompt.md`
- `create-specification.prompt.md`
- `create-implementation-plan.prompt.md`
- `create-readme.prompt.md`
- `review-and-refactor.prompt.md`
- `pytest-coverage.prompt.md`
- `conventional-commit.prompt.md`

## How to use in JetBrains

1. Open Copilot Chat.
2. Type `/` to open available prompt files.
3. Select one of the prompts from this repo.
4. Provide optional input when requested.

Repository-level guidance is defined in `.github/copilot-instructions.md`.

## Source

This setup is ported and adapted from patterns in:

- https://github.com/github/awesome-copilot
