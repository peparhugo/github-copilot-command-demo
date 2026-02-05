# Repository instructions for GitHub Copilot (JetBrains)

This repository is configured to use **GitHub Copilot repository instructions**, **prompt files**, **agents**, and **skills** so teams can run reusable command-style prompts from JetBrains and iterate on them collaboratively.

## Purpose
This file explains where to find Copilot assets in this repo and how to get the most value from them. It also contains a short checklist and recommended next steps to "super charge" the Copilot experience by improving discoverability, quality, and governance of prompts, agents and instructions.

## Where things live
- `.github/prompts/` — prompt files (`.prompt.md`) you can run directly from Copilot Chat.
- `.github/agents/` — agent blueprints that define agent behaviors and conversational policies.
- `.github/instructions/` — repository instructions (local policy and guidance) that Copilot will honor when generating code or suggestions.
- `.github/skills/` — skill collections and curated helper prompts.

## Quick start (in JetBrains Copilot Chat)
1. Open Copilot Chat in JetBrains.
2. Type `/` and pick a prompt from `.github/prompts/` (for example `/github-copilot-starter`).
3. Provide the optional input asked by the prompt.
4. Iterate: refine the prompt, run again, or open the matching agent for a longer session.

## Best practices to super charge the repo
- Keep prompts deterministic and short: prefer explicit instructions and examples so results are repeatable.
- Use front matter in prompts: include `description`, `scope`, and `input` fields so prompts are self-documenting.
- Tag prompts and agents by domain (e.g., `#security`, `#devops`, `#docs`) to make discovery easy.
- Add smoke tests for example outputs: include a short validation section in prompts that asserts expected structure (e.g., JSON schema) so you can run quick checks.
- Maintain `instructions/` files as living policy docs (accessibility, security, testing); reference them from prompts and agents.
- Version prompts/agents by adding a `version` field in front matter; update changelog entries when you modify behavior.

## Governance & Quality gates
- Pull request rule: update or add prompts/agents/instructions in the same PR that changes related code.
- Linting: run a markdown linter and a front-matter schema validator in CI to ensure prompt metadata is present.
- Review: require a tech reviewer for agent prompts that can modify code or run automation.

## Suggested super-charge checklist (start here)
- [ ] Add `description`, `author`, `post_date`, and `version` front matter to each prompt in `.github/prompts/`.
- [ ] Tag each prompt/agent with at least one domain tag (e.g., `#security`, `#testing`).
- [ ] Add a `README.md` in `.github/agents/` that explains agent naming and conventions.
- [ ] Add a `prompts/_index.md` or `prompts/README.md` that lists high-value prompts and examples.
- [ ] Add CI checks to validate prompt front matter and run simple smoke validations for critical prompts.
- [ ] Create a lightweight owner map (OWNERS or CODEOWNERS entries) for prompts and agents.

## Recommended prompt & agent authoring pattern
- Front matter with: `description`, `version`, `author`, `tags`, `applyTo` (if relevant)
- A short problem statement (1–2 lines)
- Input contract (what inputs the prompt expects)
- Desired output format (include an example / JSON schema when helpful)
- Safety & governance notes (references to instructions that should be applied)

## Example front matter (recommended)
```yaml
---
description: "Create a focused implementation plan for X feature"
version: "v1"
author: "team@example.com"
tags: [implementation, planning]
applyTo: "**/*.md"
---
```

## Next steps (practical)
1. Run an inventory of `.github/prompts/`, `.github/agents/`, `.github/instructions/` and `.github/skills/` and create `docs/copilot-inventory.md` summarizing high-value items and gaps.
2. Pick 3 high-value prompts and add front matter + an example output and smoke-test for each.
3. Add a `prompts/README.md` describing how to run and iterate on prompts locally and in JetBrains.
4. Add CI job (e.g., GitHub Actions) that runs `markdownlint` and a small script to validate front matter presence on PRs.

## Where to get help
- Use the `prompt-builder.agent.md` and `prompt-engineer.agent.md` agents (in `.github/agents/`) to improve prompts programmatically.
- For repository-specific policies, review `.github/instructions/` — there are files for accessibility, security, performance and more.

## Contributing
- When adding or modifying prompts/agents/instructions, follow the checklist above and include a changelog entry in `CHANGELOG.md`.
- Keep changes minimal and testable. Include expected output examples for reviewers.

---

This repo already contains a rich set of prompts, agents and instructions — see `.github/prompts/`, `.github/agents/` and `.github/instructions/` for many ready-to-use templates. The suggestions above will make them easier to discover, safer to run, and faster to iterate on.
