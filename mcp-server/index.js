// Simple MCP-style JSON-RPC over HTTP server
// Supports methods: create_issue, update_issue, get_issue, search_issues
const express = require('express');
const bodyParser = require('body-parser');
const JiraClient = require('./jira-client');
require('dotenv').config();

const app = express();
app.use(bodyParser.json());

const PORT = process.env.PORT || 8080;

function makeJira() {
  const jiraBase = process.env.JIRA_BASE_URL;
  const jiraEmail = process.env.JIRA_EMAIL;
  const jiraToken = process.env.JIRA_API_TOKEN;

  if (!jiraBase || !jiraEmail || !jiraToken) {
    throw new Error('JIRA_BASE_URL, JIRA_EMAIL and JIRA_API_TOKEN must be set in environment');
  }

  return new JiraClient({ baseUrl: jiraBase, email: jiraEmail, apiToken: jiraToken });
}

app.post('/rpc', async (req, res) => {
  const call = req.body;
  // Basic JSON-RPC 2.0 handling
  if (!call || !call.method) {
    return res.status(400).json({ error: 'Invalid JSON-RPC call' });
  }

  let jira;
  try {
    jira = makeJira();
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }

  try {
    switch (call.method) {
      case 'create_issue': {
        const params = call.params || {};
        const data = await jira.createIssue({
          projectKey: params.projectKey,
          summary: params.summary,
          description: params.description,
          issuetype: params.issuetype
        });
        return res.json({ jsonrpc: '2.0', result: data, id: call.id || null });
      }
      case 'update_issue': {
        const params = call.params || {};
        const data = await jira.updateIssue({ issueKey: params.issueKey, fields: params.fields });
        return res.json({ jsonrpc: '2.0', result: data, id: call.id || null });
      }
      case 'get_issue': {
        const params = call.params || {};
        const data = await jira.getIssue({ issueKey: params.issueKey });
        return res.json({ jsonrpc: '2.0', result: data, id: call.id || null });
      }
      case 'search_issues': {
        const params = call.params || {};
        const data = await jira.search({ jql: params.jql, maxResults: params.maxResults });
        return res.json({ jsonrpc: '2.0', result: data, id: call.id || null });
      }
      default:
        return res.status(400).json({ jsonrpc: '2.0', error: { code: -32601, message: 'Method not found' }, id: call.id || null });
    }
  } catch (err) {
    console.error('RPC error', err.message || err);
    return res.status(500).json({ jsonrpc: '2.0', error: { code: -32000, message: err.message || 'Server error' }, id: call.id || null });
  }
});

app.get('/', (req, res) => {
  res.send('MCP Jira JSON-RPC server running. POST JSON-RPC to /rpc');
});

app.listen(PORT, () => {
  console.log(`MCP Jira server listening on port ${PORT}`);
});
