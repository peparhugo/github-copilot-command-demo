# Test Generation from Existing Code - Instructions

## Overview
Automatically generate comprehensive test suites from existing code using GitHub Copilot.

## GitHub Copilot Instructions

### Instruction 1: Generate Unit Tests for a Function

**Prompt:**
```
Generate comprehensive unit tests for this function, including edge cases and error scenarios:
```

**Function:**
```typescript
function calculateDiscount(price: number, discountPercent: number, memberTier: 'bronze' | 'silver' | 'gold'): number {
  if (price < 0 || discountPercent < 0 || discountPercent > 100) {
    throw new Error('Invalid input parameters');
  }

  let baseDiscount = (price * discountPercent) / 100;
  
  // Apply tier multiplier
  const tierMultipliers = {
    bronze: 1.0,
    silver: 1.1,
    gold: 1.2
  };
  
  const finalDiscount = baseDiscount * tierMultipliers[memberTier];
  return Math.min(finalDiscount, price); // Discount cannot exceed price
}
```

**Expected Test Output:**
```typescript
import { describe, test, expect } from '@jest/globals';
import { calculateDiscount } from './discount';

describe('calculateDiscount', () => {
  describe('valid inputs', () => {
    test('calculates basic discount correctly', () => {
      const result = calculateDiscount(100, 10, 'bronze');
      expect(result).toBe(10);
    });

    test('applies silver tier multiplier', () => {
      const result = calculateDiscount(100, 10, 'silver');
      expect(result).toBe(11);
    });

    test('applies gold tier multiplier', () => {
      const result = calculateDiscount(100, 10, 'gold');
      expect(result).toBe(12);
    });

    test('handles zero discount', () => {
      const result = calculateDiscount(100, 0, 'bronze');
      expect(result).toBe(0);
    });

    test('handles 100% discount', () => {
      const result = calculateDiscount(100, 100, 'bronze');
      expect(result).toBe(100);
    });

    test('discount does not exceed price', () => {
      const result = calculateDiscount(50, 100, 'gold');
      expect(result).toBe(50); // Would be 60 with multiplier, but capped at 50
    });
  });

  describe('edge cases', () => {
    test('handles very small prices', () => {
      const result = calculateDiscount(0.01, 10, 'bronze');
      expect(result).toBe(0.001);
    });

    test('handles large prices', () => {
      const result = calculateDiscount(1000000, 5, 'gold');
      expect(result).toBe(60000);
    });

    test('handles decimal discount percentages', () => {
      const result = calculateDiscount(100, 10.5, 'bronze');
      expect(result).toBe(10.5);
    });
  });

  describe('error cases', () => {
    test('throws error for negative price', () => {
      expect(() => calculateDiscount(-10, 10, 'bronze'))
        .toThrow('Invalid input parameters');
    });

    test('throws error for negative discount', () => {
      expect(() => calculateDiscount(100, -5, 'bronze'))
        .toThrow('Invalid input parameters');
    });

    test('throws error for discount > 100', () => {
      expect(() => calculateDiscount(100, 150, 'bronze'))
        .toThrow('Invalid input parameters');
    });
  });
});
```

### Instruction 2: Generate Integration Tests for API Endpoints

**Prompt:**
```
Generate integration tests for this Express.js API endpoint with database mocking:
```

**API Code:**
```typescript
import express from 'express';
import { User } from './models/User';

const router = express.Router();

router.post('/users', async (req, res) => {
  try {
    const { name, email, role } = req.body;
    
    // Validation
    if (!name || !email) {
      return res.status(400).json({ error: 'Name and email are required' });
    }
    
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      return res.status(400).json({ error: 'Invalid email format' });
    }
    
    // Check if user already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(409).json({ error: 'User already exists' });
    }
    
    // Create user
    const user = await User.create({ name, email, role: role || 'user' });
    res.status(201).json(user);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

export default router;
```

**Expected Test Output:**
```typescript
import request from 'supertest';
import express from 'express';
import { User } from './models/User';
import userRoutes from './routes/users';

// Mock the User model
jest.mock('./models/User');

const app = express();
app.use(express.json());
app.use('/api', userRoutes);

describe('POST /users', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('successful user creation', () => {
    test('creates user with valid data', async () => {
      const mockUser = {
        id: '123',
        name: 'John Doe',
        email: 'john@example.com',
        role: 'user'
      };

      (User.findOne as jest.Mock).mockResolvedValue(null);
      (User.create as jest.Mock).mockResolvedValue(mockUser);

      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John Doe', email: 'john@example.com' })
        .expect(201);

      expect(response.body).toEqual(mockUser);
      expect(User.create).toHaveBeenCalledWith({
        name: 'John Doe',
        email: 'john@example.com',
        role: 'user'
      });
    });

    test('creates user with custom role', async () => {
      const mockUser = {
        id: '123',
        name: 'Admin User',
        email: 'admin@example.com',
        role: 'admin'
      };

      (User.findOne as jest.Mock).mockResolvedValue(null);
      (User.create as jest.Mock).mockResolvedValue(mockUser);

      const response = await request(app)
        .post('/api/users')
        .send({ name: 'Admin User', email: 'admin@example.com', role: 'admin' })
        .expect(201);

      expect(response.body.role).toBe('admin');
    });
  });

  describe('validation errors', () => {
    test('returns 400 when name is missing', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ email: 'john@example.com' })
        .expect(400);

      expect(response.body.error).toBe('Name and email are required');
    });

    test('returns 400 when email is missing', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John Doe' })
        .expect(400);

      expect(response.body.error).toBe('Name and email are required');
    });

    test('returns 400 for invalid email format', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John Doe', email: 'invalid-email' })
        .expect(400);

      expect(response.body.error).toBe('Invalid email format');
    });
  });

  describe('duplicate user', () => {
    test('returns 409 when user already exists', async () => {
      (User.findOne as jest.Mock).mockResolvedValue({
        id: '123',
        email: 'john@example.com'
      });

      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John Doe', email: 'john@example.com' })
        .expect(409);

      expect(response.body.error).toBe('User already exists');
      expect(User.create).not.toHaveBeenCalled();
    });
  });

  describe('server errors', () => {
    test('returns 500 when database error occurs', async () => {
      (User.findOne as jest.Mock).mockRejectedValue(new Error('DB Error'));

      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John Doe', email: 'john@example.com' })
        .expect(500);

      expect(response.body.error).toBe('Internal server error');
    });
  });
});
```

### Instruction 3: Generate E2E Tests with Playwright

**Prompt:**
```
Generate end-to-end tests using Playwright for this user registration flow:
1. Navigate to /register
2. Fill in form fields
3. Submit form
4. Verify success message
5. Verify redirect to dashboard
```

**Expected Output:**
```typescript
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/register');
  });

  test('successfully registers new user', async ({ page }) => {
    // Fill in form
    await page.fill('input[name="name"]', 'John Doe');
    await page.fill('input[name="email"]', `user-${Date.now()}@example.com`);
    await page.fill('input[name="password"]', 'SecurePass123!');
    await page.fill('input[name="confirmPassword"]', 'SecurePass123!');
    
    // Submit form
    await page.click('button[type="submit"]');
    
    // Verify success message
    await expect(page.locator('.success-message')).toBeVisible();
    await expect(page.locator('.success-message')).toContainText('Registration successful');
    
    // Verify redirect
    await expect(page).toHaveURL('/dashboard');
    
    // Verify user is logged in
    await expect(page.locator('.user-menu')).toContainText('John Doe');
  });

  test('shows validation errors for invalid email', async ({ page }) => {
    await page.fill('input[name="name"]', 'John Doe');
    await page.fill('input[name="email"]', 'invalid-email');
    await page.fill('input[name="password"]', 'SecurePass123!');
    await page.fill('input[name="confirmPassword"]', 'SecurePass123!');
    
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error-message')).toContainText('Invalid email format');
    await expect(page).toHaveURL('/register'); // Should stay on same page
  });

  test('shows error when passwords do not match', async ({ page }) => {
    await page.fill('input[name="name"]', 'John Doe');
    await page.fill('input[name="email"]', 'john@example.com');
    await page.fill('input[name="password"]', 'SecurePass123!');
    await page.fill('input[name="confirmPassword"]', 'DifferentPass123!');
    
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error-message')).toContainText('Passwords do not match');
  });

  test('shows error for weak password', async ({ page }) => {
    await page.fill('input[name="name"]', 'John Doe');
    await page.fill('input[name="email"]', 'john@example.com');
    await page.fill('input[name="password"]', '123');
    await page.fill('input[name="confirmPassword"]', '123');
    
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error-message')).toContainText('Password must be at least 8 characters');
  });

  test('handles duplicate email error', async ({ page }) => {
    const existingEmail = 'existing@example.com';
    
    await page.fill('input[name="name"]', 'John Doe');
    await page.fill('input[name="email"]', existingEmail);
    await page.fill('input[name="password"]', 'SecurePass123!');
    await page.fill('input[name="confirmPassword"]', 'SecurePass123!');
    
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error-message')).toContainText('Email already registered');
  });
});
```

## Test Generation Best Practices

### 1. Coverage Goals
- Aim for 80%+ code coverage
- Cover all public methods
- Test edge cases and error paths
- Include integration tests for critical flows

### 2. Test Structure
- Use descriptive test names
- Group related tests in describe blocks
- Follow Arrange-Act-Assert pattern
- Keep tests independent

### 3. Mocking Strategy
- Mock external dependencies
- Use test doubles for databases
- Mock API calls
- Avoid over-mocking

### 4. Assertion Quality
- Use specific assertions
- Test behavior, not implementation
- Verify both positive and negative cases
- Check error messages and types

## Advanced Test Patterns

### Property-Based Testing
```
Instruction: "Generate property-based tests using fast-check for this sorting function"
```

### Snapshot Testing
```
Instruction: "Create snapshot tests for this React component's render output"
```

### Performance Testing
```
Instruction: "Generate performance tests that verify this function completes within 100ms"
```

### Mutation Testing
```
Instruction: "Create tests that would catch common mutations in this algorithm"
```
