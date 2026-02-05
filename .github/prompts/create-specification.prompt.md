<!-- Based on: https://github.com/github/awesome-copilot/blob/main/prompts/create-specification.prompt.md -->
---
agent: 'agent'
description: 'Create a specification file optimized for AI and human implementation.'
---

Create a new specification file for `${input:SpecPurpose}`.

Requirements:
- Save file in `/spec/`.
- Naming convention: `spec-[a-z0-9-]+.md`.
- Use explicit, unambiguous language.
- Include requirements, constraints, interfaces, risks, and test/validation criteria.
- Make the document self-contained.

Use this structure:
1. Purpose & Scope
2. Definitions
3. Requirements, Constraints & Guidelines
4. Interfaces & Data Contracts
5. Validation & Acceptance Criteria
6. Risks & Assumptions
7. Related Specifications / References
