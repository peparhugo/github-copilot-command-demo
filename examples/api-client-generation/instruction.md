# API Client Generation from OpenAPI Spec - Instructions

## Overview
Automatically generate type-safe API client code from OpenAPI/Swagger specifications using GitHub Copilot.

## GitHub Copilot Instructions

### Instruction 1: Generate TypeScript Client from OpenAPI

**Prompt:**
```
Create a TypeScript API client with type-safe methods based on this OpenAPI specification:
```

**OpenAPI Spec:**
```yaml
openapi: 3.0.0
info:
  title: User Management API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List all users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
        - name: limit
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  users:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
    post:
      summary: Create a user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
  /users/{userId}:
    get:
      summary: Get user by ID
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        email:
          type: string
        createdAt:
          type: string
          format: date-time
    CreateUserRequest:
      type: object
      required:
        - name
        - email
      properties:
        name:
          type: string
        email:
          type: string
```

**Expected Output:**
```typescript
// Auto-generated types from OpenAPI spec
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: string;
}

interface CreateUserRequest {
  name: string;
  email: string;
}

interface ListUsersParams {
  page?: number;
  limit?: number;
}

interface ListUsersResponse {
  users: User[];
}

// API Client class
class UserManagementClient {
  constructor(private baseURL: string, private apiKey?: string) {}

  private async request<T>(
    endpoint: string,
    options?: RequestInit
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
      ...(this.apiKey && { 'Authorization': `Bearer ${this.apiKey}` }),
      ...options?.headers,
    };

    const response = await fetch(url, { ...options, headers });
    
    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  async listUsers(params?: ListUsersParams): Promise<ListUsersResponse> {
    const queryParams = new URLSearchParams();
    if (params?.page) queryParams.append('page', params.page.toString());
    if (params?.limit) queryParams.append('limit', params.limit.toString());
    
    const query = queryParams.toString();
    const endpoint = `/users${query ? `?${query}` : ''}`;
    
    return this.request<ListUsersResponse>(endpoint);
  }

  async createUser(data: CreateUserRequest): Promise<User> {
    return this.request<User>('/users', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async getUser(userId: string): Promise<User> {
    return this.request<User>(`/users/${userId}`);
  }
}

// Usage example
const client = new UserManagementClient('https://api.example.com', 'your-api-key');

// Type-safe API calls
const users = await client.listUsers({ page: 1, limit: 10 });
const newUser = await client.createUser({ name: 'John Doe', email: 'john@example.com' });
const user = await client.getUser('user-123');
```

### Instruction 2: Generate Python Client with Retry Logic

**Prompt:**
```
Generate a Python API client with automatic retry logic, rate limiting, and error handling for this API:
- Base URL: https://api.example.com
- Endpoints: /products (GET, POST), /products/{id} (GET, PUT, DELETE)
- Include exponential backoff for retries
- Add request/response logging
```

**Expected Output:**
```python
import requests
import time
import logging
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from enum import Enum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

@dataclass
class Product:
    id: str
    name: str
    price: float
    description: Optional[str] = None

class APIClient:
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        max_retries: int = 3,
        timeout: int = 30
    ):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.max_retries = max_retries
        self.timeout = timeout
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def _retry_with_backoff(self, func, *args, **kwargs):
        """Execute function with exponential backoff retry logic."""
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise
                
                wait_time = 2 ** attempt
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
    
    def _request(
        self,
        method: HTTPMethod,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make HTTP request with error handling."""
        url = f"{self.base_url}{endpoint}"
        
        logger.info(f"{method.value} {url}")
        
        def make_request():
            response = self.session.request(
                method=method.value,
                url=url,
                json=data,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json() if response.content else {}
        
        return self._retry_with_backoff(make_request)

class ProductClient(APIClient):
    def list_products(self, page: int = 1, limit: int = 10) -> List[Product]:
        """List all products with pagination."""
        response = self._request(
            HTTPMethod.GET,
            '/products',
            params={'page': page, 'limit': limit}
        )
        return [Product(**item) for item in response.get('products', [])]
    
    def get_product(self, product_id: str) -> Product:
        """Get a single product by ID."""
        response = self._request(HTTPMethod.GET, f'/products/{product_id}')
        return Product(**response)
    
    def create_product(self, name: str, price: float, description: Optional[str] = None) -> Product:
        """Create a new product."""
        data = {'name': name, 'price': price}
        if description:
            data['description'] = description
        
        response = self._request(HTTPMethod.POST, '/products', data=data)
        return Product(**response)
    
    def update_product(self, product_id: str, **kwargs) -> Product:
        """Update an existing product."""
        response = self._request(HTTPMethod.PUT, f'/products/{product_id}', data=kwargs)
        return Product(**response)
    
    def delete_product(self, product_id: str) -> None:
        """Delete a product."""
        self._request(HTTPMethod.DELETE, f'/products/{product_id}')

# Usage
client = ProductClient('https://api.example.com', api_key='your-key')
products = client.list_products(page=1, limit=10)
product = client.get_product('prod-123')
new_product = client.create_product('Laptop', 999.99, 'High-performance laptop')
```

### Instruction 3: Generate REST Client with GraphQL Alternative

**Prompt:**
```
Create both REST and GraphQL clients for the same API, showing how to achieve the same results with both approaches.
API: Blog platform with posts, comments, and authors
```

## Tips for API Client Generation

1. **Start with OpenAPI/Swagger**: If available, use the spec as the source of truth
2. **Type Safety**: Always generate TypeScript interfaces or Python dataclasses
3. **Error Handling**: Include comprehensive error handling and retries
4. **Authentication**: Support multiple auth methods (API key, OAuth, JWT)
5. **Testing**: Generate test mocks and fixtures alongside the client
6. **Documentation**: Auto-generate usage examples and method documentation

## Advanced Patterns

### Rate Limiting
```
Instruction: "Add rate limiting to this API client that respects HTTP 429 responses and Retry-After headers"
```

### Caching
```
Instruction: "Implement request caching with TTL for GET requests in this API client"
```

### Request/Response Interceptors
```
Instruction: "Add middleware pattern for request/response transformation and logging"
```

### WebSocket Support
```
Instruction: "Extend this REST client to also support WebSocket connections for real-time updates"
```
