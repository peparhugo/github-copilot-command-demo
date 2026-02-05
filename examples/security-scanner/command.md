# Security Vulnerability Scanner - Commands

## Overview
Use GitHub Copilot to identify and fix security vulnerabilities in code.

## Slash Commands

### /fix - Fix Security Issues

**Usage:**
```
Select vulnerable code and use:
/fix Fix security vulnerabilities in this code including SQL injection, XSS, and CSRF
```

### Inline Chat - Security Review

**Press Ctrl+I:**
```
Review this code for security vulnerabilities and suggest fixes
```

## Demo Workflow (8 minutes)

### Minute 1-2: Identify SQL Injection
```
1. Show vulnerable SQL code
2. Use: /fix Prevent SQL injection by using parameterized queries
3. Demonstrate before/after
```

### Minute 2-3: Fix XSS Vulnerabilities
```
1. Show React component with dangerouslySetInnerHTML
2. Use: /fix Add input sanitization to prevent XSS attacks
3. Show DOMPurify implementation
```

### Minute 4-5: Authentication Review
```
1. Select authentication middleware
2. Use inline chat: "What security issues exist in this auth code?"
3. Apply suggested fixes
```

### Minute 6-7: Scan Entire Codebase
```
@workspace Scan all files for common security vulnerabilities:
- SQL injection
- XSS
- CSRF
- Insecure authentication
- Sensitive data exposure
```

### Minute 8: Generate Security Report
```
/doc Create a security audit report summarizing vulnerabilities found and fixes applied
```

## Advanced Security Commands

### OWASP Top 10 Check
```
@workspace Review code against OWASP Top 10 vulnerabilities
```

### Dependency Audit
```
Check package.json for known vulnerabilities and suggest secure alternatives
```

### Secrets Detection
```
@workspace Find hardcoded secrets, API keys, or passwords in the codebase
```

### Input Validation
```
/new Create a comprehensive input validation middleware for Express.js
```

## Security Checklist

Use this prompt to get a comprehensive security review:
```
Review this application for:
1. ✓ Input validation
2. ✓ Output encoding
3. ✓ Authentication security
4. ✓ Authorization checks
5. ✓ Sensitive data protection
6. ✓ HTTPS enforcement
7. ✓ Security headers
8. ✓ CSRF protection
9. ✓ Rate limiting
10. ✓ Error handling (no info leakage)
```
