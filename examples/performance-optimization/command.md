# Performance Optimization - Commands

## Overview
Use GitHub Copilot to identify and fix performance bottlenecks in code.

## Slash Commands

### /optimize - Improve Performance

**Usage:**
```
Select slow code and use:
/optimize Improve the performance of this code
```

### Inline Chat - Performance Review

**Press Ctrl+I:**
```
What are the performance bottlenecks in this code and how can I fix them?
```

## Demo Workflow (8 minutes)

### Minute 1-2: Fix N+1 Queries
```
1. Show code with N+1 query problem
2. Use: /optimize Fix the N+1 query problem using eager loading
3. Compare query counts before/after
```

### Minute 2-3: Optimize React Rendering
```
1. Show component that re-renders unnecessarily
2. Use: /fix Prevent unnecessary re-renders using React.memo and useMemo
3. Show React DevTools Profiler
```

### Minute 4-5: Algorithm Optimization
```
1. Show O(n²) or O(n³) algorithm
2. Use: /optimize Reduce the time complexity of this algorithm
3. Benchmark before/after
```

### Minute 6-7: Bundle Size Reduction
```
@workspace Find large dependencies and suggest lighter alternatives
```

### Minute 8: Caching Strategy
```
/new Implement a caching layer with Redis for this API endpoint
```

## Advanced Performance Commands

### Database Query Analysis
```
@workspace Analyze all database queries and suggest optimizations including indexes
```

### Memory Leak Detection
```
Review this code for potential memory leaks
```

### Bundle Analysis
```
Analyze package.json and suggest ways to reduce bundle size by 50%
```

### API Response Time
```
/optimize This API endpoint takes 2 seconds to respond. Reduce it to under 200ms using:
1. Parallel queries
2. Caching
3. Pagination
4. Field selection
```

## Performance Benchmarking

Use this prompt for benchmarking:
```
Create performance benchmarks for this function that:
1. Measures execution time
2. Tracks memory usage
3. Compares against baseline
4. Generates performance report
```

## Quick Wins Checklist

Ask Copilot to check for these common issues:
```
Review code for these performance issues:
- [ ] N+1 query problems
- [ ] Missing database indexes
- [ ] Unnecessary re-renders in React
- [ ] Large bundle sizes
- [ ] Blocking operations on main thread
- [ ] Missing caching
- [ ] Inefficient algorithms (O(n²) or worse)
- [ ] Large payload sizes
- [ ] Unoptimized images
- [ ] Memory leaks
```
