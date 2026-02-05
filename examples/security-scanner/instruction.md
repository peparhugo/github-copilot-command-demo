# Security Vulnerability Scanner - Instructions

## Overview
Use GitHub Copilot to identify and fix security vulnerabilities in code.

## GitHub Copilot Instructions

### Instruction 1: Identify SQL Injection Vulnerabilities

**Prompt:**
```
Review this code for SQL injection vulnerabilities and suggest fixes:
```

**Vulnerable Code:**
```typescript
app.get('/users', (req, res) => {
  const searchQuery = req.query.search;
  const sql = `SELECT * FROM users WHERE name LIKE '%${searchQuery}%'`;
  db.query(sql, (err, results) => {
    res.json(results);
  });
});
```

**Expected Analysis and Fix:**
```typescript
/**
 * VULNERABILITY IDENTIFIED: SQL Injection
 * 
 * Problem: User input is directly concatenated into SQL query
 * Risk Level: CRITICAL
 * Attack Vector: Malicious user could inject SQL commands
 * 
 * Example Attack:
 * GET /users?search='; DROP TABLE users; --
 * 
 * This would execute: SELECT * FROM users WHERE name LIKE '%'; DROP TABLE users; --%'
 */

// FIXED VERSION - Using Parameterized Queries
app.get('/users', (req, res) => {
  const searchQuery = req.query.search;
  
  // Input validation
  if (!searchQuery || typeof searchQuery !== 'string') {
    return res.status(400).json({ error: 'Invalid search parameter' });
  }
  
  // Parameterized query prevents SQL injection
  const sql = 'SELECT * FROM users WHERE name LIKE ?';
  const params = [`%${searchQuery}%`];
  
  db.query(sql, params, (err, results) => {
    if (err) {
      console.error('Database error:', err);
      return res.status(500).json({ error: 'Internal server error' });
    }
    res.json(results);
  });
});

// EVEN BETTER - Using an ORM like TypeORM
app.get('/users', async (req, res) => {
  try {
    const searchQuery = req.query.search;
    
    if (!searchQuery || typeof searchQuery !== 'string') {
      return res.status(400).json({ error: 'Invalid search parameter' });
    }
    
    const users = await User.find({
      where: {
        name: Like(`%${searchQuery}%`)
      }
    });
    
    res.json(users);
  } catch (err) {
    console.error('Error fetching users:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

### Instruction 2: Fix XSS (Cross-Site Scripting) Vulnerabilities

**Prompt:**
```
Identify and fix XSS vulnerabilities in this React component:
```

**Vulnerable Code:**
```typescript
function UserProfile({ user }) {
  return (
    <div>
      <h1>{user.name}</h1>
      <div dangerouslySetInnerHTML={{ __html: user.bio }} />
      <a href={user.website}>Website</a>
    </div>
  );
}
```

**Expected Analysis and Fix:**
```typescript
/**
 * VULNERABILITIES IDENTIFIED:
 * 
 * 1. XSS via dangerouslySetInnerHTML
 *    - User bio is rendered as raw HTML without sanitization
 *    - Attacker could inject malicious scripts
 * 
 * 2. Open Redirect via href
 *    - Website URL is not validated
 *    - Could redirect to malicious sites
 * 
 * Risk Level: HIGH
 */

import DOMPurify from 'dompurify';
import { useMemo } from 'react';

function UserProfile({ user }) {
  // Sanitize HTML content to prevent XSS
  const sanitizedBio = useMemo(() => {
    return DOMPurify.sanitize(user.bio, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p', 'br'],
      ALLOWED_ATTR: ['href']
    });
  }, [user.bio]);
  
  // Validate URL to prevent open redirect
  const isValidUrl = (url: string): boolean => {
    try {
      const parsedUrl = new URL(url);
      // Only allow http and https protocols
      return ['http:', 'https:'].includes(parsedUrl.protocol);
    } catch {
      return false;
    }
  };
  
  const safeWebsite = isValidUrl(user.website) ? user.website : '#';
  
  return (
    <div>
      {/* User name is automatically escaped by React */}
      <h1>{user.name}</h1>
      
      {/* Sanitized HTML */}
      <div dangerouslySetInnerHTML={{ __html: sanitizedBio }} />
      
      {/* Validated URL with additional security attributes */}
      {safeWebsite !== '#' && (
        <a 
          href={safeWebsite} 
          target="_blank" 
          rel="noopener noreferrer"
        >
          Website
        </a>
      )}
    </div>
  );
}

// ALTERNATIVE: Avoid HTML rendering entirely
function UserProfileSafe({ user }) {
  return (
    <div>
      <h1>{user.name}</h1>
      {/* Render bio as plain text - safest approach */}
      <p className="bio">{user.bio}</p>
      {user.website && isValidUrl(user.website) && (
        <a 
          href={user.website} 
          target="_blank" 
          rel="noopener noreferrer"
        >
          Website
        </a>
      )}
    </div>
  );
}
```

### Instruction 3: Fix Authentication and Authorization Issues

**Prompt:**
```
Review this authentication middleware for security issues:
```

**Vulnerable Code:**
```typescript
function authMiddleware(req, res, next) {
  const token = req.headers.authorization;
  
  if (token) {
    const decoded = jwt.decode(token);
    req.user = decoded;
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

app.delete('/users/:id', authMiddleware, (req, res) => {
  User.delete(req.params.id);
  res.json({ success: true });
});
```

**Expected Analysis and Fix:**
```typescript
/**
 * VULNERABILITIES IDENTIFIED:
 * 
 * 1. JWT Token Not Verified
 *    - Using jwt.decode() instead of jwt.verify()
 *    - Anyone can create a fake token
 * 
 * 2. No Token Signature Validation
 *    - Token is not verified against secret key
 * 
 * 3. Insecure Direct Object Reference (IDOR)
 *    - No authorization check
 *    - Any authenticated user can delete any user
 * 
 * 4. Bearer Prefix Not Required
 *    - Should enforce "Bearer " prefix
 * 
 * Risk Level: CRITICAL
 */

import jwt from 'jsonwebtoken';

interface JWTPayload {
  userId: string;
  role: string;
  iat: number;
  exp: number;
}

// FIXED Authentication Middleware
function authMiddleware(req, res, next) {
  try {
    const authHeader = req.headers.authorization;
    
    // Check for Authorization header
    if (!authHeader) {
      return res.status(401).json({ error: 'No authorization token provided' });
    }
    
    // Validate Bearer prefix
    if (!authHeader.startsWith('Bearer ')) {
      return res.status(401).json({ error: 'Invalid authorization format' });
    }
    
    // Extract token
    const token = authHeader.substring(7);
    
    // Verify token signature and expiration
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as JWTPayload;
    
    // Additional validation
    if (!decoded.userId || !decoded.role) {
      return res.status(401).json({ error: 'Invalid token payload' });
    }
    
    // Check token expiration explicitly
    if (decoded.exp && Date.now() >= decoded.exp * 1000) {
      return res.status(401).json({ error: 'Token expired' });
    }
    
    // Attach user to request
    req.user = decoded;
    next();
  } catch (err) {
    if (err.name === 'JsonWebTokenError') {
      return res.status(401).json({ error: 'Invalid token' });
    }
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(500).json({ error: 'Authentication error' });
  }
}

// Authorization Middleware
function requireRole(allowedRoles: string[]) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Forbidden: Insufficient permissions' });
    }
    
    next();
  };
}

// FIXED Endpoint with Proper Authorization
app.delete('/users/:id', 
  authMiddleware,
  requireRole(['admin']),
  async (req, res) => {
    try {
      const targetUserId = req.params.id;
      const currentUserId = req.user.userId;
      
      // Additional check: Users can only delete themselves unless they're admin
      if (req.user.role !== 'admin' && targetUserId !== currentUserId) {
        return res.status(403).json({ 
          error: 'Forbidden: You can only delete your own account' 
        });
      }
      
      // Validate user exists before deleting
      const user = await User.findById(targetUserId);
      if (!user) {
        return res.status(404).json({ error: 'User not found' });
      }
      
      // Prevent self-deletion for admins if they're the last admin
      if (req.user.role === 'admin') {
        const adminCount = await User.count({ role: 'admin' });
        if (adminCount === 1 && targetUserId === currentUserId) {
          return res.status(400).json({ 
            error: 'Cannot delete the last admin account' 
          });
        }
      }
      
      await User.delete(targetUserId);
      
      // Log the deletion for audit trail
      await AuditLog.create({
        action: 'USER_DELETED',
        performedBy: currentUserId,
        targetUser: targetUserId,
        timestamp: new Date()
      });
      
      res.json({ success: true });
    } catch (err) {
      console.error('Error deleting user:', err);
      res.status(500).json({ error: 'Internal server error' });
    }
  }
);
```

### Instruction 4: Fix Sensitive Data Exposure

**Prompt:**
```
Review this user API response for sensitive data exposure:
```

**Vulnerable Code:**
```typescript
app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});
```

**Expected Analysis and Fix:**
```typescript
/**
 * VULNERABILITY: Sensitive Data Exposure
 * 
 * Problem: Entire user object is sent, including sensitive fields
 * Risk: Password hash, email verification tokens, etc. exposed
 * 
 * Risk Level: HIGH
 */

// Define DTOs (Data Transfer Objects) for API responses
interface PublicUserDTO {
  id: string;
  name: string;
  username: string;
  avatarUrl?: string;
  createdAt: Date;
}

interface PrivateUserDTO extends PublicUserDTO {
  email: string;
  emailVerified: boolean;
  lastLogin: Date;
}

// User entity (DO NOT expose directly)
interface UserEntity {
  id: string;
  name: string;
  username: string;
  email: string;
  passwordHash: string;  // NEVER expose this!
  resetToken?: string;   // NEVER expose this!
  emailVerificationToken?: string;  // NEVER expose this!
  emailVerified: boolean;
  avatarUrl?: string;
  createdAt: Date;
  lastLogin: Date;
}

// FIXED Version
app.get('/users/:id', 
  authMiddleware, 
  async (req, res) => {
    try {
      const user = await User.findById(req.params.id);
      
      if (!user) {
        return res.status(404).json({ error: 'User not found' });
      }
      
      // Determine what data to return based on who's requesting
      const isOwnProfile = req.user.userId === req.params.id;
      const isAdmin = req.user.role === 'admin';
      
      let responseData: PublicUserDTO | PrivateUserDTO;
      
      if (isOwnProfile || isAdmin) {
        // Return private data for own profile or admin
        responseData = {
          id: user.id,
          name: user.name,
          username: user.username,
          email: user.email,
          emailVerified: user.emailVerified,
          avatarUrl: user.avatarUrl,
          createdAt: user.createdAt,
          lastLogin: user.lastLogin
        };
      } else {
        // Return only public data for other users
        responseData = {
          id: user.id,
          name: user.name,
          username: user.username,
          avatarUrl: user.avatarUrl,
          createdAt: user.createdAt
        };
      }
      
      res.json(responseData);
    } catch (err) {
      console.error('Error fetching user:', err);
      res.status(500).json({ error: 'Internal server error' });
    }
  }
);
```

## Security Scanning Best Practices

1. **Regular Audits**: Scan code regularly for vulnerabilities
2. **Input Validation**: Always validate and sanitize user input
3. **Output Encoding**: Encode data before rendering
4. **Least Privilege**: Grant minimum necessary permissions
5. **Security Headers**: Use helmet.js for Express apps
6. **Dependencies**: Keep dependencies updated
7. **Secrets Management**: Never commit secrets to code

## Common Vulnerability Categories (OWASP Top 10)

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)
