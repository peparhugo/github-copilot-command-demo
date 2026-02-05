# MCP Jira Server

A small local MCP-style JSON-RPC server that exposes simple Jira operations: create_issue, update_issue, get_issue, search_issues.

This server is intended for local development and can be used as a tool by an MCP agent or other local automation to interact with Jira.

## Quick start

1. Copy `.env.example` to `.env` and fill in your Jira base URL, email and API token.

2. Install dependencies:

```powershell
cd mcp-server; npm install
```

3. Start server:

```powershell
npm start
```

4. POST JSON-RPC calls to `http://localhost:8080/rpc`.

Example create issue:

```json
{
  "jsonrpc": "2.0",
  "method": "create_issue",
  "params": {
    "projectKey": "PROJ",
    "summary": "Test from MCP",
    "description": "Created by local MCP server",
    "issuetype": "Task"
  },
  "id": 1
}
```

Example update issue:

```json
{
  "jsonrpc": "2.0",
  "method": "update_issue",
  "params": {
    "issueKey": "PROJ-123",
    "fields": { "summary": "Updated summary" }
  },
  "id": 2
}
```

## Security

This server uses basic auth (email + API token) to call the Jira REST API. Keep your `.env` out of source control and use proper secret management for production.

## MCP integration

Provide a `mcp-tools.json` descriptor (root) that lists the available operations and parameters so MCP-aware tools can discover them.

## Notes

- This is intentionally minimal. Add rate limiting, retries, and robust error handling for production use.
