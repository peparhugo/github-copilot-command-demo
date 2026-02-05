// ...existing code...
const axios = require('axios');

class JiraClient {
  constructor({ baseUrl, email, apiToken }) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.auth = {
      username: email,
      password: apiToken
    };
    this.http = axios.create({
      baseURL: `${this.baseUrl}/rest/api/3`,
      auth: this.auth,
      headers: { 'Accept': 'application/json' }
    });
  }

  async createIssue({ projectKey, summary, description, issuetype = 'Task' }) {
    const payload = {
      fields: {
        project: { key: projectKey },
        summary,
        description,
        issuetype: { name: issuetype }
      }
    };
    const res = await this.http.post('/issue', payload);
    return res.data;
  }

  async updateIssue({ issueKey, fields }) {
    const res = await this.http.put(`/issue/${encodeURIComponent(issueKey)}`, { fields });
    return res.status === 204 ? { ok: true } : res.data;
  }

  async getIssue({ issueKey }) {
    const res = await this.http.get(`/issue/${encodeURIComponent(issueKey)}`);
    return res.data;
  }

  async search({ jql, maxResults = 50 }) {
    const res = await this.http.post('/search', { jql, maxResults });
    return res.data;
  }
}

module.exports = JiraClient;
