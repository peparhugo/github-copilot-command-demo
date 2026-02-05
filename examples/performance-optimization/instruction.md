# Performance Optimization - Instructions

## Overview
Use GitHub Copilot to identify performance bottlenecks and optimize code for better performance.

## GitHub Copilot Instructions

### Instruction 1: Optimize Database Queries (N+1 Problem)

**Prompt:**
```
Fix the N+1 query problem in this code:
```

**Inefficient Code:**
```typescript
async function getUsersWithPosts() {
  const users = await User.findAll();
  
  const usersWithPosts = await Promise.all(
    users.map(async (user) => ({
      ...user,
      posts: await Post.findAll({ where: { userId: user.id } })
    }))
  );
  
  return usersWithPosts;
}
```

**Optimized Code:**
```typescript
/**
 * PROBLEM: N+1 Query
 * - 1 query to fetch all users
 * - N queries to fetch posts for each user
 * - Total: 1 + N queries
 * 
 * SOLUTION: Use eager loading with includes/joins
 */

// Using Sequelize ORM
async function getUsersWithPosts() {
  const users = await User.findAll({
    include: [{
      model: Post,
      as: 'posts'
    }]
  });
  
  return users;
}

// Using TypeORM
async function getUsersWithPostsTypeORM() {
  return await User.find({
    relations: ['posts']
  });
}

// Using raw SQL with JOIN
async function getUsersWithPostsRaw() {
  const query = `
    SELECT 
      u.id as user_id,
      u.name as user_name,
      u.email,
      p.id as post_id,
      p.title,
      p.content,
      p.created_at
    FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    ORDER BY u.id, p.created_at DESC
  `;
  
  const results = await db.query(query);
  
  // Group posts by user
  const usersMap = new Map();
  
  for (const row of results) {
    if (!usersMap.has(row.user_id)) {
      usersMap.set(row.user_id, {
        id: row.user_id,
        name: row.user_name,
        email: row.email,
        posts: []
      });
    }
    
    if (row.post_id) {
      usersMap.get(row.user_id).posts.push({
        id: row.post_id,
        title: row.title,
        content: row.content,
        createdAt: row.created_at
      });
    }
  }
  
  return Array.from(usersMap.values());
}

/**
 * PERFORMANCE IMPROVEMENT:
 * Before: O(1 + N) queries
 * After: O(1) query
 * 
 * For 100 users:
 * Before: 101 queries
 * After: 1 query
 * 
 * Estimated speedup: 10-100x depending on network latency
 */
```

### Instruction 2: Optimize React Component Rendering

**Prompt:**
```
Optimize this React component to prevent unnecessary re-renders:
```

**Inefficient Code:**
```typescript
function UserList({ users, onUserClick }) {
  const [searchTerm, setSearchTerm] = useState('');
  
  const filteredUsers = users.filter(user => 
    user.name.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  return (
    <div>
      <input 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      {filteredUsers.map(user => (
        <UserCard 
          key={user.id} 
          user={user} 
          onClick={() => onUserClick(user.id)} 
        />
      ))}
    </div>
  );
}

function UserCard({ user, onClick }) {
  console.log('Rendering UserCard:', user.name);
  return (
    <div onClick={onClick}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}
```

**Optimized Code:**
```typescript
import { useState, useMemo, useCallback, memo } from 'react';

/**
 * OPTIMIZATIONS APPLIED:
 * 1. useMemo for expensive filtering operation
 * 2. useCallback for stable function references
 * 3. React.memo to prevent unnecessary re-renders
 * 4. Virtualization for large lists
 */

function UserList({ users, onUserClick }) {
  const [searchTerm, setSearchTerm] = useState('');
  
  // Memoize filtered users - only recalculate when users or searchTerm changes
  const filteredUsers = useMemo(() => {
    return users.filter(user => 
      user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [users, searchTerm]);
  
  // Memoize callback to prevent new function on every render
  const handleUserClick = useCallback((userId: string) => {
    onUserClick(userId);
  }, [onUserClick]);
  
  return (
    <div>
      <input 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search users..."
      />
      {filteredUsers.map(user => (
        <UserCard 
          key={user.id} 
          user={user} 
          onClick={handleUserClick}
        />
      ))}
    </div>
  );
}

// Memoized component - only re-renders if props change
const UserCard = memo(function UserCard({ user, onClick }: UserCardProps) {
  console.log('Rendering UserCard:', user.name);
  
  const handleClick = useCallback(() => {
    onClick(user.id);
  }, [user.id, onClick]);
  
  return (
    <div onClick={handleClick}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function
  return prevProps.user.id === nextProps.user.id && 
         prevProps.onClick === nextProps.onClick;
});

// For very large lists (1000+ items), use virtualization
import { FixedSizeList as List } from 'react-window';

function VirtualizedUserList({ users, onUserClick }) {
  const [searchTerm, setSearchTerm] = useState('');
  
  const filteredUsers = useMemo(() => {
    return users.filter(user => 
      user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [users, searchTerm]);
  
  const Row = useCallback(({ index, style }) => {
    const user = filteredUsers[index];
    return (
      <div style={style}>
        <UserCard user={user} onClick={onUserClick} />
      </div>
    );
  }, [filteredUsers, onUserClick]);
  
  return (
    <div>
      <input 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <List
        height={600}
        itemCount={filteredUsers.length}
        itemSize={80}
        width="100%"
      >
        {Row}
      </List>
    </div>
  );
}

/**
 * PERFORMANCE IMPROVEMENT:
 * - Without optimization: Re-renders all components on every state change
 * - With useMemo: Filter operation runs only when needed
 * - With memo: UserCard only re-renders when its props change
 * - With virtualization: Only visible rows are rendered
 * 
 * For 1000 users:
 * Before: 1000 DOM updates on search
 * After: ~10-20 DOM updates (only visible items)
 * 
 * Estimated speedup: 50-100x for large lists
 */
```

### Instruction 3: Optimize API Response Time

**Prompt:**
```
Optimize this API endpoint to reduce response time:
```

**Inefficient Code:**
```typescript
app.get('/api/dashboard', async (req, res) => {
  const user = await User.findById(req.user.id);
  const posts = await Post.findAll({ userId: req.user.id });
  const comments = await Comment.findAll({ userId: req.user.id });
  const notifications = await Notification.findAll({ userId: req.user.id });
  const stats = await calculateUserStats(req.user.id);
  
  res.json({
    user,
    posts,
    comments,
    notifications,
    stats
  });
});
```

**Optimized Code:**
```typescript
/**
 * OPTIMIZATIONS:
 * 1. Parallel queries instead of sequential
 * 2. Response caching with Redis
 * 3. Pagination for large datasets
 * 4. Field selection to reduce payload size
 */

import Redis from 'ioredis';
const redis = new Redis();

app.get('/api/dashboard', async (req, res) => {
  const userId = req.user.id;
  const cacheKey = `dashboard:${userId}`;
  
  // 1. Check cache first
  const cached = await redis.get(cacheKey);
  if (cached) {
    return res.json(JSON.parse(cached));
  }
  
  // 2. Execute queries in parallel
  const [user, posts, comments, notifications, stats] = await Promise.all([
    // Select only needed fields
    User.findById(userId, {
      attributes: ['id', 'name', 'email', 'avatar']
    }),
    
    // Limit and paginate
    Post.findAll({
      where: { userId },
      limit: 10,
      order: [['createdAt', 'DESC']],
      attributes: ['id', 'title', 'createdAt']
    }),
    
    Comment.findAll({
      where: { userId },
      limit: 10,
      order: [['createdAt', 'DESC']],
      attributes: ['id', 'content', 'postId', 'createdAt']
    }),
    
    Notification.findAll({
      where: { userId, read: false },
      limit: 5,
      order: [['createdAt', 'DESC']],
      attributes: ['id', 'type', 'message', 'createdAt']
    }),
    
    // Pre-calculated stats stored in separate table
    UserStats.findOne({
      where: { userId },
      attributes: ['totalPosts', 'totalComments', 'totalLikes']
    })
  ]);
  
  const response = {
    user,
    posts,
    comments,
    notifications,
    stats
  };
  
  // 3. Cache the response (5 minutes TTL)
  await redis.setex(cacheKey, 300, JSON.stringify(response));
  
  res.json(response);
});

/**
 * PERFORMANCE IMPROVEMENT:
 * Before: 5 sequential queries = 5 * 50ms = 250ms
 * After (parallel): max(50ms) = 50ms
 * After (cached): < 5ms
 * 
 * Estimated speedup:
 * - First request: 5x faster
 * - Cached requests: 50x faster
 */

// Background job to pre-warm cache
async function prewarmDashboardCache(userId: string) {
  // Warm cache during off-peak hours
  // This ensures users get instant responses
}

// Invalidate cache when data changes
async function invalidateDashboardCache(userId: string) {
  await redis.del(`dashboard:${userId}`);
}
```

### Instruction 4: Optimize Algorithm Complexity

**Prompt:**
```
Optimize this algorithm to reduce time complexity:
```

**Inefficient Code:**
```typescript
// Find duplicate numbers in an array
function findDuplicates(nums: number[]): number[] {
  const duplicates: number[] = [];
  
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] === nums[j] && !duplicates.includes(nums[i])) {
        duplicates.push(nums[i]);
      }
    }
  }
  
  return duplicates;
}

// Time Complexity: O(n³)
// Space Complexity: O(n)
```

**Optimized Code:**
```typescript
/**
 * OPTIMIZATION: Use Set/Map for O(1) lookups
 * 
 * Time Complexity: O(n³) → O(n)
 * Space Complexity: O(n) → O(n)
 */

function findDuplicates(nums: number[]): number[] {
  const seen = new Set<number>();
  const duplicates = new Set<number>();
  
  for (const num of nums) {
    if (seen.has(num)) {
      duplicates.add(num);
    } else {
      seen.add(num);
    }
  }
  
  return Array.from(duplicates);
}

/**
 * PERFORMANCE COMPARISON:
 * 
 * For n = 10,000:
 * Before: ~10,000³ = 1,000,000,000,000 operations
 * After: ~10,000 operations
 * 
 * Speedup: 100,000,000x
 */

// Alternative using Map to track counts
function findDuplicatesWithCount(nums: number[]): Map<number, number> {
  const counts = new Map<number, number>();
  
  for (const num of nums) {
    counts.set(num, (counts.get(num) || 0) + 1);
  }
  
  // Filter to only duplicates
  const duplicates = new Map<number, number>();
  for (const [num, count] of counts) {
    if (count > 1) {
      duplicates.set(num, count);
    }
  }
  
  return duplicates;
}
```

### Instruction 5: Optimize Bundle Size

**Prompt:**
```
Reduce the bundle size of this Next.js application:
```

**Before:**
```typescript
import _ from 'lodash';
import moment from 'moment';
import { Button, Card, Modal, Dropdown, ... } from 'antd';

function MyComponent() {
  const formatted = moment().format('YYYY-MM-DD');
  const sorted = _.sortBy(items, 'name');
  
  return <Button>Click me</Button>;
}
```

**Optimized Code:**
```typescript
/**
 * OPTIMIZATIONS:
 * 1. Tree-shaking with named imports
 * 2. Replace heavy libraries with lighter alternatives
 * 3. Dynamic imports for code splitting
 * 4. Remove unused dependencies
 */

// Use tree-shakeable imports
import sortBy from 'lodash/sortBy';
import { format } from 'date-fns';  // Much lighter than moment
import { Button } from 'antd';  // Import only what you need
import dynamic from 'next/dynamic';

// Dynamic import for code splitting
const Modal = dynamic(() => import('antd').then(mod => mod.Modal), {
  loading: () => <p>Loading...</p>,
  ssr: false  // Don't render on server if not needed
});

function MyComponent() {
  const formatted = format(new Date(), 'yyyy-MM-dd');
  const sorted = sortBy(items, 'name');
  
  return <Button>Click me</Button>;
}

/**
 * BUNDLE SIZE REDUCTION:
 * 
 * Before:
 * - lodash: 72 KB
 * - moment: 67 KB
 * - antd (full): 300 KB
 * Total: ~440 KB
 * 
 * After:
 * - lodash/sortBy: 2 KB
 * - date-fns/format: 3 KB
 * - antd (Button only): 20 KB
 * Total: ~25 KB
 * 
 * Size reduction: 94% (440 KB → 25 KB)
 */

// next.config.js optimization
module.exports = {
  webpack: (config) => {
    config.optimization.splitChunks = {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: -10
        }
      }
    };
    return config;
  }
};
```

## Performance Optimization Best Practices

1. **Measure First**: Use profiling tools to identify bottlenecks
2. **Database Optimization**: Proper indexing, query optimization, connection pooling
3. **Caching Strategy**: Redis, CDN, browser cache
4. **Code Splitting**: Load only what's needed
5. **Lazy Loading**: Defer non-critical resources
6. **Compression**: Gzip/Brotli for responses
7. **Monitoring**: Track performance metrics over time

## Tools for Performance Analysis

- Chrome DevTools Performance tab
- React DevTools Profiler
- Lighthouse
- WebPageTest
- Bundle Analyzer
- Database query analyzers
