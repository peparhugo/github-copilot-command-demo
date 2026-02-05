# Test Generation - Commands

## Overview
Automatically generate comprehensive tests using GitHub Copilot commands.

## Slash Commands

### /tests - Generate Unit Tests

**Usage:**
```
Select a function or class, then:
/tests Generate comprehensive unit tests with edge cases and error scenarios
```

**Example:**
```typescript
// Select this function
function divide(a: number, b: number): number {
  if (b === 0) throw new Error('Division by zero');
  return a / b;
}

// Use: /tests
```

**Expected Output:**
```typescript
describe('divide', () => {
  test('divides positive numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  test('divides negative numbers', () => {
    expect(divide(-10, 2)).toBe(-5);
  });

  test('throws error for division by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });

  test('handles decimal results', () => {
    expect(divide(5, 2)).toBe(2.5);
  });
});
```

### /fix - Fix Failing Tests

**Usage:**
```
Select a failing test and use:
/fix Make this test pass
```

### Inline Chat - Quick Test Generation

**Press Ctrl+I (Cmd+I on Mac):**
```
Generate test cases for happy path and error cases
```

## Demo Workflow (8 minutes)

### Minute 1-2: Unit Test Generation
```
1. Open a function you want to test
2. Select the entire function
3. Use /tests command
4. Review and run generated tests
```

### Minute 3-4: Mock Complex Dependencies
```
1. Select a function with external dependencies
2. Use: /tests Generate tests with mocked dependencies
3. Verify mocks are properly configured
```

### Minute 5-6: Integration Tests
```
1. Select an API endpoint handler
2. Use: /tests Create integration tests with supertest
3. Run tests against test database
```

### Minute 7-8: E2E Tests
```
1. Document a user flow in comments
2. Use: /new Create Playwright test for this user flow
3. Run E2E test in browser
```

## Advanced Techniques

### Test Coverage Analysis
```
@workspace Analyze test coverage and suggest tests for uncovered code paths
```

### Mutation Testing
```
Generate tests that would fail if I remove this null check
```

### Performance Testing
```
/tests Create performance benchmarks for this function that verify it completes in under 100ms
```
