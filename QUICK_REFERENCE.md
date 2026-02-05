# GitHub Copilot Command Quick Reference

A quick reference card for all GitHub Copilot commands and shortcuts used in this demo.

## 🔥 Essential Commands

### Slash Commands (in Chat)

| Command | Purpose | Example |
|---------|---------|---------|
| `/explain` | Understand code or concepts | `/explain How does this SQL query work?` |
| `/fix` | Fix bugs or issues | `/fix Security vulnerabilities in this code` |
| `/doc` | Generate documentation | `/doc Create JSDoc comments for this function` |
| `/tests` | Generate test cases | `/tests Create unit tests with edge cases` |
| `/new` | Create new code | `/new Create API client from OpenAPI spec` |
| `/simplify` | Reduce complexity | `/simplify Break this into smaller functions` |
| `/optimize` | Improve performance | `/optimize Reduce time complexity` |

### Keyboard Shortcuts

| Shortcut | Platform | Action |
|----------|----------|--------|
| `Ctrl + I` | Windows/Linux | Open inline chat |
| `Cmd + I` | Mac | Open inline chat |
| `Ctrl + Shift + I` | Windows/Linux | Open chat panel |
| `Cmd + Shift + I` | Mac | Open chat panel |
| `Tab` | All | Accept suggestion |
| `Esc` | All | Dismiss suggestion |
| `Alt + ]` | Windows/Linux | Next suggestion |
| `Alt + [` | Windows/Linux | Previous suggestion |
| `Option + ]` | Mac | Next suggestion |
| `Option + [` | Mac | Previous suggestion |

## 🎯 Context Commands

### Workspace Agent

Use `@workspace` to analyze the entire repository:

```
@workspace Find all SQL queries in this project
@workspace Scan for security vulnerabilities  
@workspace List all API endpoints
@workspace Find files with TODO comments
@workspace Suggest performance optimizations
```

### File References

Reference specific files in your prompts:

```
Using the patterns in #file:UserRepository.ts, create OrderRepository.ts
Convert the SQL query in #file:queries.sql to Elasticsearch
Based on #file:types.ts, generate API client
```

### Terminal Commands

Use `#terminal` to reference terminal output:

```
Fix the error shown in #terminal
Explain what #terminal output means
Debug the test failure in #terminal
```

## 📋 Common Patterns

### SQL to Elasticsearch

```plaintext
Pattern: "Convert this SQL to Elasticsearch Query DSL"
Works for:
- SELECT statements
- WHERE clauses  
- JOINs
- Aggregations (GROUP BY, COUNT, AVG, SUM)
- ORDER BY and LIMIT
```

### Security Fixes

```plaintext
Pattern: "/fix Security vulnerabilities including SQL injection, XSS, and CSRF"
Detects:
- SQL Injection
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Insecure authentication
- Sensitive data exposure
```

### Test Generation

```plaintext
Pattern: "/tests Generate comprehensive unit tests with edge cases"
Generates:
- Happy path tests
- Edge cases
- Error scenarios
- Mocked dependencies
- Assertions
```

### API Client Generation

```plaintext
Pattern: "/new Create TypeScript API client from this OpenAPI spec"
Includes:
- Type-safe interfaces
- Error handling
- Retry logic
- Authentication
- Request/response interceptors
```

### Performance Optimization

```plaintext
Pattern: "/optimize Improve performance of this code"
Fixes:
- N+1 query problems
- Inefficient algorithms
- Unnecessary re-renders
- Large bundle sizes
- Missing caching
```

### Documentation

```plaintext
Pattern: "/doc Generate comprehensive documentation with examples"
Creates:
- JSDoc/TSDoc comments
- README files
- API documentation
- Usage examples
- OpenAPI specs
```

### Code Refactoring

```plaintext
Pattern: "/fix Refactor to use [pattern name] pattern"
Patterns:
- Repository
- MVC
- Observer
- Factory
- Strategy
- Dependency Injection
```

## 💡 Pro Tips

### 1. Be Specific

❌ Bad: "Fix this"
✅ Good: "Fix SQL injection vulnerability using parameterized queries"

### 2. Provide Context

❌ Bad: "Create tests"
✅ Good: "Create Jest tests for this Express.js controller with mocked database"

### 3. Iterate

1. Start with simple prompt
2. Review output
3. Refine with more specific requirements
4. Get better results

### 4. Use Multiple Commands

```
Step 1: /explain What security issues exist here?
Step 2: /fix Address the SQL injection vulnerability
Step 3: /tests Create tests to verify the fix
Step 4: /doc Document the security improvement
```

### 5. Combine Features

```
Select code → /explain → /fix → /tests → /doc
```

## 🔍 Advanced Techniques

### Multi-step Workflows

```
1. @workspace Find all database queries
2. /optimize Convert N+1 queries to eager loading
3. /tests Generate tests for optimized queries
4. /doc Document performance improvements
```

### Custom Instructions in Comments

```typescript
// @copilot Convert the following SQL to Elasticsearch
// Requirements:
// - Use filter context for better performance
// - Add fuzzy matching for text fields
// - Include proper error handling
const sql = "SELECT * FROM users WHERE name LIKE '%John%'";
```

### Iterative Refinement

```
First attempt: "Create API client"
→ Review output
Second attempt: "Add retry logic with exponential backoff"
→ Review output
Third attempt: "Add request/response logging"
→ Production ready!
```

### Natural Language Prompts

Instead of:
```
/new function convert SQL
```

Use:
```
/new Create a robust TypeScript function that converts SQL WHERE clauses to Elasticsearch bool queries, supporting AND, OR, NOT, and nested conditions with full error handling
```

## 📊 Best Practices

### Do's ✅
- Be specific about requirements
- Provide example inputs/outputs
- Specify the programming language
- Mention framework/library versions
- Include error handling requirements
- Request tests alongside code

### Don'ts ❌
- Don't use vague prompts
- Don't skip code review
- Don't blindly accept suggestions
- Don't forget edge cases
- Don't ignore errors
- Don't commit without testing

## 🎬 Demo Shortcuts

Quick commands for impressive demos:

### 1-Minute Demos
```
SQL → Elasticsearch: "Convert this SQL to Elasticsearch Query DSL"
Security Fix: "/fix SQL injection vulnerability"
Test Generation: "/tests with edge cases"
```

### 2-Minute Demos
```
API Client: "/new TypeScript API client from OpenAPI spec"
Performance: "/optimize Fix N+1 query problem"
Refactoring: "/fix Refactor to Repository pattern"
```

### 5-Minute Demos
```
Complete workflow:
1. Show problem code
2. @workspace analyze issues
3. /fix address issues
4. /tests verify fixes
5. /doc document changes
```

## 📚 Example Prompts by Use Case

### Web Development
```
"Create React component with TypeScript, props validation, and tests"
"Generate Express.js REST API with error handling and validation"
"Build Next.js page with SSR and proper SEO"
```

### Backend Development
```
"Create database migration for this schema change"
"Generate GraphQL resolvers from this schema"
"Build authentication middleware with JWT"
```

### Testing
```
"Generate Playwright E2E tests for this user flow"
"Create integration tests with mocked external services"
"Write property-based tests for this algorithm"
```

### DevOps
```
"Create Dockerfile with multi-stage build"
"Generate GitHub Actions workflow for CI/CD"
"Build Terraform configuration for AWS infrastructure"
```

### Data Engineering
```
"Convert this Pandas code to PySpark"
"Generate SQL query from this business requirement"
"Create data validation schema with Pydantic"
```

## 🚨 Troubleshooting

### Copilot Not Responding
1. Check internet connection
2. Reload VS Code window
3. Check Copilot status in bottom bar
4. Try `/clear` to clear context

### Poor Suggestions
1. Add more context in prompt
2. Reference similar code files
3. Be more specific about requirements
4. Use `/explain` first to establish context

### Wrong Programming Language
```
Specify explicitly: "Create a Python function..."
Reference file extension: "In TypeScript..."
Use language-specific terms: "async/await", "List comprehension"
```

## 📖 Learning Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [Copilot Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

---

**Print this page** for quick reference during demos and development! 🖨️
