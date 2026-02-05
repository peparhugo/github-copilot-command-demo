# API Client Generation - Commands

## Overview
Use GitHub Copilot commands to automatically generate API clients from specifications.

## Slash Commands

### /new - Generate Complete API Client

**Usage:**
```
/new Create a TypeScript API client from this OpenAPI spec with error handling, retries, and TypeScript types
```

### /doc - Generate API Documentation

**Usage:**
```
/doc Create comprehensive documentation for this API client including usage examples and error handling
```

### /tests - Generate API Client Tests

**Usage:**
```
/tests Generate unit tests for this API client with mocked responses
```

**Expected Output:**
```typescript
import { describe, test, expect, jest } from '@jest/globals';
import { UserManagementClient } from './client';

// Mock fetch
global.fetch = jest.fn();

describe('UserManagementClient', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('listUsers returns users array', async () => {
    const mockResponse = {
      users: [
        { id: '1', name: 'John', email: 'john@example.com', createdAt: '2024-01-01' }
      ]
    };

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    });

    const client = new UserManagementClient('https://api.test.com');
    const result = await client.listUsers({ page: 1, limit: 10 });

    expect(fetch).toHaveBeenCalledWith(
      'https://api.test.com/users?page=1&limit=10',
      expect.any(Object)
    );
    expect(result.users).toHaveLength(1);
  });

  test('handles API errors gracefully', async () => {
    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: false,
      status: 404,
      statusText: 'Not Found',
    });

    const client = new UserManagementClient('https://api.test.com');
    
    await expect(client.getUser('invalid-id'))
      .rejects.toThrow('API Error: 404 Not Found');
  });
});
```

### @workspace - Scan for API Specifications

**Usage in Chat:**
```
@workspace Find all OpenAPI/Swagger specifications in this project and generate TypeScript clients for each
```

## Demo Sequence

### Step 1: Find API Spec (1 minute)
```
@workspace Find OpenAPI or Swagger files in this repository
```

### Step 2: Generate Client (2 minutes)
```
/new Create a complete TypeScript API client from the OpenAPI spec in ./specs/api.yaml
Include:
- Type-safe interfaces
- Async/await methods
- Error handling with custom exceptions
- Request/response interceptors
```

### Step 3: Add Authentication (1 minute)
```
Add Bearer token authentication to this API client with automatic token refresh
```

### Step 4: Generate Tests (2 minutes)
```
/tests Create comprehensive tests for this API client with mocked fetch responses
```

### Step 5: Documentation (1 minute)
```
/doc Generate usage documentation with examples for each API method
```
