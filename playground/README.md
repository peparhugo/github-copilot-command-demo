# Copilot Prompt Playground

A minimal local playground to browse the repository's Copilot prompt files and render them with optional input.

Why: Quickly inspect and test `.github/prompts/*.prompt.md` files without JetBrains.

Requirements:
- Node.js 16+ (or compatible LTS)

Quick start:

```powershell
cd playground
npm install
npm start
# then open http://localhost:3000 in your browser
```

Notes:
- The server reads prompts from `.github/prompts/` relative to the repo root.
- This is intentionally minimal and safe: it does not execute prompts or contact any external service.
- Accessibility: a skip-to-main link and keyboard focus styles are included.

Security & privacy:
- This tool runs locally and does not send data anywhere.
- Do not run in production or expose to untrusted networks.
