# Code Refactoring with Architecture Patterns - Instructions

## Overview
Use GitHub Copilot to refactor code to follow established architecture patterns and best practices.

## GitHub Copilot Instructions

### Instruction 1: Refactor to Repository Pattern

**Prompt:**
```
Refactor this data access code to use the Repository pattern with dependency injection:
```

**Before:**
```typescript
// user-service.ts
import { db } from './database';

class UserService {
  async getUser(id: string) {
    const result = await db.query('SELECT * FROM users WHERE id = ?', [id]);
    return result[0];
  }

  async createUser(name: string, email: string) {
    const result = await db.query(
      'INSERT INTO users (name, email) VALUES (?, ?)',
      [name, email]
    );
    return result.insertId;
  }

  async updateUser(id: string, data: any) {
    await db.query('UPDATE users SET ? WHERE id = ?', [data, id]);
  }

  async deleteUser(id: string) {
    await db.query('DELETE FROM users WHERE id = ?', [id]);
  }
}
```

**Expected Output:**
```typescript
// entities/User.ts
export interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
  updatedAt: Date;
}

// repositories/IUserRepository.ts
export interface IUserRepository {
  findById(id: string): Promise<User | null>;
  findAll(): Promise<User[]>;
  create(user: Omit<User, 'id' | 'createdAt' | 'updatedAt'>): Promise<User>;
  update(id: string, user: Partial<User>): Promise<User>;
  delete(id: string): Promise<void>;
}

// repositories/UserRepository.ts
import { IUserRepository } from './IUserRepository';
import { User } from '../entities/User';
import { Database } from '../infrastructure/Database';

export class UserRepository implements IUserRepository {
  constructor(private db: Database) {}

  async findById(id: string): Promise<User | null> {
    const result = await this.db.query<User>(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );
    return result[0] || null;
  }

  async findAll(): Promise<User[]> {
    return this.db.query<User>('SELECT * FROM users');
  }

  async create(userData: Omit<User, 'id' | 'createdAt' | 'updatedAt'>): Promise<User> {
    const now = new Date();
    const result = await this.db.query(
      'INSERT INTO users (name, email, created_at, updated_at) VALUES (?, ?, ?, ?)',
      [userData.name, userData.email, now, now]
    );
    
    return {
      ...userData,
      id: result.insertId,
      createdAt: now,
      updatedAt: now
    };
  }

  async update(id: string, userData: Partial<User>): Promise<User> {
    const updateData = { ...userData, updatedAt: new Date() };
    await this.db.query('UPDATE users SET ? WHERE id = ?', [updateData, id]);
    
    const updated = await this.findById(id);
    if (!updated) throw new Error('User not found after update');
    return updated;
  }

  async delete(id: string): Promise<void> {
    await this.db.query('DELETE FROM users WHERE id = ?', [id]);
  }
}

// services/UserService.ts
import { IUserRepository } from '../repositories/IUserRepository';
import { User } from '../entities/User';

export class UserService {
  constructor(private userRepository: IUserRepository) {}

  async getUser(id: string): Promise<User | null> {
    return this.userRepository.findById(id);
  }

  async getAllUsers(): Promise<User[]> {
    return this.userRepository.findAll();
  }

  async createUser(name: string, email: string): Promise<User> {
    // Add business logic validation here
    if (!this.isValidEmail(email)) {
      throw new Error('Invalid email format');
    }

    return this.userRepository.create({ name, email });
  }

  async updateUser(id: string, data: Partial<User>): Promise<User> {
    // Add business logic here
    return this.userRepository.update(id, data);
  }

  async deleteUser(id: string): Promise<void> {
    await this.userRepository.delete(id);
  }

  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}

// dependency-injection/container.ts
import { Database } from '../infrastructure/Database';
import { UserRepository } from '../repositories/UserRepository';
import { UserService } from '../services/UserService';

export class Container {
  private static instance: Container;
  private services: Map<string, any> = new Map();

  private constructor() {
    this.registerServices();
  }

  static getInstance(): Container {
    if (!Container.instance) {
      Container.instance = new Container();
    }
    return Container.instance;
  }

  private registerServices(): void {
    // Register database
    const database = new Database({
      host: process.env.DB_HOST,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD
    });
    this.services.set('Database', database);

    // Register repository
    const userRepository = new UserRepository(database);
    this.services.set('UserRepository', userRepository);

    // Register service
    const userService = new UserService(userRepository);
    this.services.set('UserService', userService);
  }

  get<T>(serviceName: string): T {
    const service = this.services.get(serviceName);
    if (!service) {
      throw new Error(`Service ${serviceName} not found`);
    }
    return service;
  }
}

// Usage
const container = Container.getInstance();
const userService = container.get<UserService>('UserService');
const user = await userService.getUser('123');
```

### Instruction 2: Refactor to MVC Pattern

**Prompt:**
```
Refactor this monolithic Express route handler to follow MVC (Model-View-Controller) pattern:
```

**Before:**
```typescript
app.post('/products', async (req, res) => {
  const { name, price, category } = req.body;
  
  if (!name || !price) {
    return res.status(400).json({ error: 'Missing required fields' });
  }
  
  const product = await db.query(
    'INSERT INTO products (name, price, category) VALUES (?, ?, ?)',
    [name, price, category || 'general']
  );
  
  res.status(201).json({ id: product.insertId, name, price, category });
});
```

**Expected Output:**
```typescript
// models/Product.ts
export class Product {
  constructor(
    public id: string,
    public name: string,
    public price: number,
    public category: string
  ) {}

  static async create(data: { name: string; price: number; category?: string }): Promise<Product> {
    const category = data.category || 'general';
    const result = await db.query(
      'INSERT INTO products (name, price, category) VALUES (?, ?, ?)',
      [data.name, data.price, category]
    );
    
    return new Product(result.insertId, data.name, data.price, category);
  }

  static async findById(id: string): Promise<Product | null> {
    const results = await db.query('SELECT * FROM products WHERE id = ?', [id]);
    if (results.length === 0) return null;
    
    const row = results[0];
    return new Product(row.id, row.name, row.price, row.category);
  }

  static async findAll(): Promise<Product[]> {
    const results = await db.query('SELECT * FROM products');
    return results.map(row => new Product(row.id, row.name, row.price, row.category));
  }

  async update(data: Partial<{ name: string; price: number; category: string }>): Promise<void> {
    await db.query('UPDATE products SET ? WHERE id = ?', [data, this.id]);
    Object.assign(this, data);
  }

  async delete(): Promise<void> {
    await db.query('DELETE FROM products WHERE id = ?', [this.id]);
  }
}

// controllers/ProductController.ts
import { Request, Response } from 'express';
import { Product } from '../models/Product';
import { ProductValidator } from '../validators/ProductValidator';

export class ProductController {
  async create(req: Request, res: Response): Promise<void> {
    try {
      // Validate input
      const validation = ProductValidator.validateCreate(req.body);
      if (!validation.isValid) {
        res.status(400).json({ error: validation.error });
        return;
      }

      // Create product
      const product = await Product.create(req.body);

      // Send response
      res.status(201).json(product);
    } catch (error) {
      console.error('Error creating product:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  async getById(req: Request, res: Response): Promise<void> {
    try {
      const product = await Product.findById(req.params.id);
      
      if (!product) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }

      res.json(product);
    } catch (error) {
      console.error('Error fetching product:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  async getAll(req: Request, res: Response): Promise<void> {
    try {
      const products = await Product.findAll();
      res.json(products);
    } catch (error) {
      console.error('Error fetching products:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  async update(req: Request, res: Response): Promise<void> {
    try {
      const product = await Product.findById(req.params.id);
      
      if (!product) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }

      const validation = ProductValidator.validateUpdate(req.body);
      if (!validation.isValid) {
        res.status(400).json({ error: validation.error });
        return;
      }

      await product.update(req.body);
      res.json(product);
    } catch (error) {
      console.error('Error updating product:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  async delete(req: Request, res: Response): Promise<void> {
    try {
      const product = await Product.findById(req.params.id);
      
      if (!product) {
        res.status(404).json({ error: 'Product not found' });
        return;
      }

      await product.delete();
      res.status(204).send();
    } catch (error) {
      console.error('Error deleting product:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }
}

// validators/ProductValidator.ts
export class ProductValidator {
  static validateCreate(data: any): { isValid: boolean; error?: string } {
    if (!data.name || typeof data.name !== 'string') {
      return { isValid: false, error: 'Name is required and must be a string' };
    }

    if (!data.price || typeof data.price !== 'number' || data.price <= 0) {
      return { isValid: false, error: 'Price is required and must be a positive number' };
    }

    if (data.category && typeof data.category !== 'string') {
      return { isValid: false, error: 'Category must be a string' };
    }

    return { isValid: true };
  }

  static validateUpdate(data: any): { isValid: boolean; error?: string } {
    if (data.name && typeof data.name !== 'string') {
      return { isValid: false, error: 'Name must be a string' };
    }

    if (data.price && (typeof data.price !== 'number' || data.price <= 0)) {
      return { isValid: false, error: 'Price must be a positive number' };
    }

    if (data.category && typeof data.category !== 'string') {
      return { isValid: false, error: 'Category must be a string' };
    }

    return { isValid: true };
  }
}

// routes/productRoutes.ts
import { Router } from 'express';
import { ProductController } from '../controllers/ProductController';

const router = Router();
const productController = new ProductController();

router.post('/products', (req, res) => productController.create(req, res));
router.get('/products', (req, res) => productController.getAll(req, res));
router.get('/products/:id', (req, res) => productController.getById(req, res));
router.put('/products/:id', (req, res) => productController.update(req, res));
router.delete('/products/:id', (req, res) => productController.delete(req, res));

export default router;

// app.ts
import express from 'express';
import productRoutes from './routes/productRoutes';

const app = express();
app.use(express.json());
app.use('/api', productRoutes);

export default app;
```

### Instruction 3: Refactor to Observer Pattern

**Prompt:**
```
Refactor this event handling code to use the Observer pattern for better decoupling:
```

**Before:**
```typescript
class OrderProcessor {
  processOrder(order: Order) {
    // Process the order
    this.validateOrder(order);
    this.chargePayment(order);
    this.updateInventory(order);
    
    // Send notifications
    this.sendEmailToCustomer(order);
    this.sendSmsToCustomer(order);
    this.notifyWarehouse(order);
    this.updateAnalytics(order);
  }
}
```

**Expected Output:**
```typescript
// Observer pattern implementation
interface Observer {
  update(event: OrderEvent): void;
}

interface Subject {
  attach(observer: Observer): void;
  detach(observer: Observer): void;
  notify(event: OrderEvent): void;
}

type OrderEvent = {
  type: 'ORDER_CREATED' | 'ORDER_PROCESSED' | 'ORDER_SHIPPED' | 'ORDER_CANCELLED';
  order: Order;
  timestamp: Date;
};

// Subject
class OrderProcessor implements Subject {
  private observers: Observer[] = [];

  attach(observer: Observer): void {
    const exists = this.observers.includes(observer);
    if (!exists) {
      this.observers.push(observer);
    }
  }

  detach(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index !== -1) {
      this.observers.splice(index, 1);
    }
  }

  notify(event: OrderEvent): void {
    for (const observer of this.observers) {
      observer.update(event);
    }
  }

  async processOrder(order: Order): Promise<void> {
    try {
      await this.validateOrder(order);
      await this.chargePayment(order);
      await this.updateInventory(order);
      
      // Notify all observers
      this.notify({
        type: 'ORDER_PROCESSED',
        order,
        timestamp: new Date()
      });
    } catch (error) {
      this.notify({
        type: 'ORDER_CANCELLED',
        order,
        timestamp: new Date()
      });
      throw error;
    }
  }

  private async validateOrder(order: Order): Promise<void> {
    // Validation logic
  }

  private async chargePayment(order: Order): Promise<void> {
    // Payment logic
  }

  private async updateInventory(order: Order): Promise<void> {
    // Inventory logic
  }
}

// Concrete Observers
class EmailNotificationObserver implements Observer {
  update(event: OrderEvent): void {
    if (event.type === 'ORDER_PROCESSED') {
      this.sendOrderConfirmation(event.order);
    } else if (event.type === 'ORDER_CANCELLED') {
      this.sendCancellationEmail(event.order);
    }
  }

  private sendOrderConfirmation(order: Order): void {
    console.log(`Sending confirmation email to ${order.customerEmail}`);
    // Email sending logic
  }

  private sendCancellationEmail(order: Order): void {
    console.log(`Sending cancellation email to ${order.customerEmail}`);
    // Email sending logic
  }
}

class SmsNotificationObserver implements Observer {
  update(event: OrderEvent): void {
    if (event.type === 'ORDER_PROCESSED') {
      this.sendOrderSms(event.order);
    }
  }

  private sendOrderSms(order: Order): void {
    console.log(`Sending SMS to ${order.customerPhone}`);
    // SMS sending logic
  }
}

class WarehouseNotificationObserver implements Observer {
  update(event: OrderEvent): void {
    if (event.type === 'ORDER_PROCESSED') {
      this.notifyWarehouse(event.order);
    }
  }

  private notifyWarehouse(order: Order): void {
    console.log(`Notifying warehouse about order ${order.id}`);
    // Warehouse notification logic
  }
}

class AnalyticsObserver implements Observer {
  update(event: OrderEvent): void {
    this.trackEvent(event);
  }

  private trackEvent(event: OrderEvent): void {
    console.log(`Analytics: ${event.type} at ${event.timestamp}`);
    // Analytics tracking logic
  }
}

// Usage
const orderProcessor = new OrderProcessor();

// Attach observers
orderProcessor.attach(new EmailNotificationObserver());
orderProcessor.attach(new SmsNotificationObserver());
orderProcessor.attach(new WarehouseNotificationObserver());
orderProcessor.attach(new AnalyticsObserver());

// Process order - all observers will be notified automatically
await orderProcessor.processOrder(order);
```

## Refactoring Best Practices

1. **Start Small**: Refactor one pattern at a time
2. **Maintain Tests**: Ensure tests pass before and after refactoring
3. **Incremental Changes**: Make small, verifiable changes
4. **Document Patterns**: Add comments explaining the pattern used
5. **Review Dependencies**: Update dependency injection as needed

## Common Architecture Patterns

- Repository Pattern
- MVC (Model-View-Controller)
- MVVM (Model-View-ViewModel)
- Observer Pattern
- Factory Pattern
- Strategy Pattern
- Dependency Injection
- Clean Architecture
- Hexagonal Architecture
- CQRS (Command Query Responsibility Segregation)
