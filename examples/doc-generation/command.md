# Documentation Generation - Commands

## Overview
Use GitHub Copilot to automatically generate documentation from code.

## Slash Commands

### /doc - Generate Documentation

**Usage:**
```
Select code and use:
/doc Create comprehensive documentation with examples
```

**Example:**
```typescript
// Select this class
class UserService {
  async createUser(data: UserData): Promise<User> {
    // implementation
  }
}

// Use: /doc Generate JSDoc comments for this class
```

### Inline Chat - Quick Comments

**Press Ctrl+I:**
```
Add JSDoc comments explaining parameters and return values
```

## Demo Workflow

### Step 1: Generate API Docs (2 minutes)
```
1. Select all API route handlers
2. Use: /doc Create OpenAPI specification
3. Save to openapi.yaml
```

### Step 2: Add Inline Comments (2 minutes)
```
1. Select complex function
2. Use inline chat: "Add explanatory comments for each step"
3. Review and refine
```

### Step 3: Generate README (2 minutes)
```
@workspace Analyze this project and create a comprehensive README.md with:
- Project description
- Installation steps
- Usage examples
- API documentation
- Contributing guidelines
```

### Step 4: Class Documentation (1 minute)
```
1. Select a class
2. /doc Generate complete JSDoc/TSDoc comments for this class
```

### Step 5: Generate Changelog (1 minute)
```
@workspace Review git commits and generate a CHANGELOG.md following keep a changelog format
```

## Advanced Documentation

### Architecture Diagrams
```
Create a mermaid diagram showing the architecture of this application
```

### Type Documentation
```
Generate comprehensive type documentation for all TypeScript interfaces
```

### Migration Guides
```
Create a migration guide for upgrading from v1 to v2 based on the code changes
```
