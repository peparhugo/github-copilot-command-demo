<!-- Based on: https://github.com/github/awesome-copilot/blob/main/prompts/create-implementation-plan.prompt.md -->
---
agent: 'agent'
description: 'Create a deterministic implementation plan with atomic phases and executable tasks.'
---

Create a new implementation plan for `${input:PlanPurpose}`.

Requirements:
- Save the plan in `/plan/`.
- Naming convention: `[purpose]-[component]-[version].md`.
- Use atomic, trackable tasks with explicit success criteria.
- Organize by phases with clear dependencies.
- Include testing, risks, assumptions, and affected files.

Plan sections:
1. Requirements & Constraints
2. Implementation Phases and Tasks
3. Alternatives
4. Dependencies
5. Files
6. Testing
7. Risks & Assumptions
