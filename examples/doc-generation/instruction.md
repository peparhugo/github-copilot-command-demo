# Documentation Generation from Code - Instructions

## Overview
Automatically generate comprehensive documentation from code using GitHub Copilot.

## GitHub Copilot Instructions

### Instruction 1: Generate API Documentation

**Prompt:**
```
Generate OpenAPI/Swagger documentation for these Express.js API endpoints:
```

**Code:**
```typescript
router.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

router.post('/users', async (req, res) => {
  const user = await User.create(req.body);
  res.status(201).json(user);
});

router.put('/users/:id', async (req, res) => {
  const user = await User.update(req.params.id, req.body);
  res.json(user);
});

router.delete('/users/:id', async (req, res) => {
  await User.delete(req.params.id);
  res.status(204).send();
});
```

**Expected Output:**
```yaml
openapi: 3.0.0
info:
  title: User Management API
  version: 1.0.0
  description: API for managing user resources

paths:
  /users/{id}:
    get:
      summary: Get user by ID
      description: Retrieves a single user by their unique identifier
      parameters:
        - name: id
          in: path
          required: true
          description: Unique user identifier
          schema:
            type: string
      responses:
        '200':
          description: User found successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      tags:
        - Users
    
    put:
      summary: Update user
      description: Updates an existing user's information
      parameters:
        - name: id
          in: path
          required: true
          description: Unique user identifier
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserUpdate'
      responses:
        '200':
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
      tags:
        - Users
    
    delete:
      summary: Delete user
      description: Removes a user from the system
      parameters:
        - name: id
          in: path
          required: true
          description: Unique user identifier
          schema:
            type: string
      responses:
        '204':
          description: User deleted successfully
        '404':
          description: User not found
      tags:
        - Users

  /users:
    post:
      summary: Create new user
      description: Creates a new user in the system
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserCreate'
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          description: Invalid input
      tags:
        - Users

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          description: Unique user identifier
        name:
          type: string
          description: User's full name
        email:
          type: string
          format: email
          description: User's email address
        createdAt:
          type: string
          format: date-time
          description: Timestamp when user was created
        updatedAt:
          type: string
          format: date-time
          description: Timestamp when user was last updated
      required:
        - id
        - name
        - email

    UserCreate:
      type: object
      properties:
        name:
          type: string
          description: User's full name
        email:
          type: string
          format: email
          description: User's email address
      required:
        - name
        - email

    UserUpdate:
      type: object
      properties:
        name:
          type: string
          description: User's full name
        email:
          type: string
          format: email
          description: User's email address

    Error:
      type: object
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Error code
```

### Instruction 2: Generate JSDoc Comments

**Prompt:**
```
Add comprehensive JSDoc comments to this TypeScript function:
```

**Code:**
```typescript
function calculateShippingCost(
  weight: number,
  distance: number,
  express: boolean = false,
  insurance: boolean = false
): number {
  let baseCost = weight * 0.5 + distance * 0.1;
  
  if (express) {
    baseCost *= 1.5;
  }
  
  if (insurance) {
    baseCost += weight * 0.02;
  }
  
  return Math.round(baseCost * 100) / 100;
}
```

**Expected Output:**
```typescript
/**
 * Calculates the shipping cost based on package weight, distance, and additional services.
 * 
 * The base cost is calculated using the formula: (weight * 0.5) + (distance * 0.1)
 * Additional charges apply for express shipping and insurance.
 * 
 * @param {number} weight - Package weight in kilograms. Must be a positive number.
 * @param {number} distance - Shipping distance in kilometers. Must be a positive number.
 * @param {boolean} [express=false] - Whether to use express shipping. Adds 50% to base cost.
 * @param {boolean} [insurance=false] - Whether to include insurance. Adds 2% of weight value.
 * 
 * @returns {number} The total shipping cost in dollars, rounded to 2 decimal places.
 * 
 * @example
 * // Regular shipping
 * calculateShippingCost(10, 100);
 * // Returns: 11.00
 * 
 * @example
 * // Express shipping with insurance
 * calculateShippingCost(10, 100, true, true);
 * // Returns: 16.70
 * 
 * @throws {Error} Throws an error if weight or distance is negative.
 */
function calculateShippingCost(
  weight: number,
  distance: number,
  express: boolean = false,
  insurance: boolean = false
): number {
  if (weight < 0 || distance < 0) {
    throw new Error('Weight and distance must be positive numbers');
  }

  let baseCost = weight * 0.5 + distance * 0.1;
  
  if (express) {
    baseCost *= 1.5;
  }
  
  if (insurance) {
    baseCost += weight * 0.02;
  }
  
  return Math.round(baseCost * 100) / 100;
}
```

### Instruction 3: Generate README from Codebase

**Prompt:**
```
Generate a comprehensive README.md for this project based on the code structure and package.json
```

**Expected Output:**
```markdown
# Project Name

![Build Status](https://img.shields.io/github/workflow/status/user/repo/CI)
![Coverage](https://img.shields.io/codecov/c/github/user/repo)
![License](https://img.shields.io/github/license/user/repo)

A brief description of what this project does and who it's for.

## Features

- ✨ Feature 1: User authentication and authorization
- 🚀 Feature 2: RESTful API with full CRUD operations
- 📊 Feature 3: Real-time data synchronization
- 🔒 Feature 4: End-to-end encryption
- 🎨 Feature 5: Modern responsive UI

## Installation

### Prerequisites

- Node.js >= 16.0.0
- npm >= 8.0.0
- PostgreSQL >= 13.0

### Setup

1. Clone the repository:
```bash
git clone https://github.com/user/repo.git
cd repo
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run database migrations:
```bash
npm run migrate
```

5. Start the development server:
```bash
npm run dev
```

## Usage

### Starting the Server

```bash
npm start
```

The server will start on `http://localhost:3000`

### API Endpoints

#### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user

#### Users
- `GET /api/users` - List all users
- `GET /api/users/:id` - Get user by ID
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

### Examples

#### Register a new user:
```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepass123"}'
```

#### Get user information:
```bash
curl http://localhost:3000/api/users/123 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Development

### Project Structure

```
.
├── src/
│   ├── controllers/    # Request handlers
│   ├── models/         # Database models
│   ├── routes/         # API routes
│   ├── services/       # Business logic
│   ├── middleware/     # Express middleware
│   └── utils/          # Utility functions
├── tests/              # Test files
├── docs/               # Documentation
└── scripts/            # Build and deployment scripts
```

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Linting and Formatting

```bash
# Run ESLint
npm run lint

# Fix linting issues
npm run lint:fix

# Format code with Prettier
npm run format
```

### Building for Production

```bash
npm run build
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | 3000 |
| `DATABASE_URL` | PostgreSQL connection string | - |
| `JWT_SECRET` | Secret key for JWT tokens | - |
| `NODE_ENV` | Environment (development/production) | development |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards

- Follow the ESLint configuration
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **John Doe** - *Initial work* - [johndoe](https://github.com/johndoe)

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
```

### Instruction 4: Generate Inline Code Comments

**Prompt:**
```
Add explanatory comments to this complex algorithm:
```

**Code:**
```typescript
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left: number[], right: number[]): number[] {
  const result: number[] = [];
  let i = 0, j = 0;
  
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i++]);
    } else {
      result.push(right[j++]);
    }
  }
  
  return result.concat(left.slice(i)).concat(right.slice(j));
}
```

**Expected Output:**
```typescript
/**
 * Sorts an array of numbers using the merge sort algorithm.
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 * 
 * @param arr - The array to be sorted
 * @returns A new sorted array
 */
function mergeSort(arr: number[]): number[] {
  // Base case: arrays with 0 or 1 element are already sorted
  if (arr.length <= 1) return arr;
  
  // Divide: find the middle point to divide the array into two halves
  const mid = Math.floor(arr.length / 2);
  
  // Split the array into left and right subarrays
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  
  // Recursively sort both halves and merge them
  // This is the "divide and conquer" approach
  return merge(mergeSort(left), mergeSort(right));
}

/**
 * Merges two sorted arrays into a single sorted array.
 * This is the "conquer" step of merge sort.
 * 
 * @param left - First sorted array
 * @param right - Second sorted array
 * @returns Merged sorted array
 */
function merge(left: number[], right: number[]): number[] {
  const result: number[] = [];
  let i = 0;  // Pointer for left array
  let j = 0;  // Pointer for right array
  
  // Compare elements from both arrays and add the smaller one to result
  // Continue until we reach the end of either array
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      // Left element is smaller, add it to result and move left pointer
      result.push(left[i++]);
    } else {
      // Right element is smaller or equal, add it to result and move right pointer
      result.push(right[j++]);
    }
  }
  
  // Add any remaining elements from left array (if any)
  // Then add any remaining elements from right array (if any)
  // At least one of these will be empty
  return result.concat(left.slice(i)).concat(right.slice(j));
}
```

## Documentation Best Practices

1. **Keep it Updated**: Regenerate docs when code changes
2. **Be Comprehensive**: Cover all public APIs
3. **Include Examples**: Show real-world usage
4. **Document Edge Cases**: Explain error conditions
5. **Add Diagrams**: Use mermaid or similar for architecture
6. **Version Documentation**: Track changes with versions
