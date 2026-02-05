// Minimal Express server to serve prompt files and a tiny UI
const express = require('express');
const path = require('path');
const fs = require('fs').promises;

const app = express();
const PORT = process.env.PORT || 3000;

const PROMPTS_DIR = path.join(__dirname, '..', '.github', 'prompts');

app.use('/static', express.static(path.join(__dirname, 'static')));

app.get('/api/prompts', async (req, res) => {
  try {
    const files = await fs.readdir(PROMPTS_DIR);
    const promptFiles = files.filter(f => f.endsWith('.prompt.md'));
    const results = [];
    for (const f of promptFiles) {
      const content = await fs.readFile(path.join(PROMPTS_DIR, f), 'utf8');
      results.push({ name: f, content });
    }
    res.json(results);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'static', 'index.html'));
});

app.listen(PORT, () => console.log(`Playground running on http://localhost:${PORT}`));
