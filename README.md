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

## Local Prompt Playground (optional)

A minimal local playground is included at `playground/` to browse and render the repository's Copilot prompt files (`.github/prompts/*.prompt.md`) in your browser without JetBrains.

Why use it:

- Quickly inspect prompt front-matter and content.
- Render a prompt with optional input to preview what will be sent to Copilot Chat.
- Keep prompt testing local and safe — the playground does not execute prompts or contact external services.

Requirements

- Node.js 16+ installed locally.

Quick start (PowerShell):

```powershell
cd playground
npm install --no-audit --no-fund
npm start
# open http://localhost:3000
```

Notes

- The server reads prompt files from `.github/prompts/` relative to the repository root.
- The UI is intentionally minimal and accessible: skip-to-main link, keyboard focus styles, and clear labels.
- Do not expose the playground on untrusted networks; it's intended for local use only.

If you'd like, I can extend the playground (search, front-matter parsing, or a small CI lint) — tell me which feature to add next.

## Source

This setup is ported and adapted from patterns in:

- https://github.com/github/awesome-copilot
