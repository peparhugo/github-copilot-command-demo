# SQL to Elasticsearch Query Conversion - Commands

## Overview
This file demonstrates GitHub Copilot slash commands for converting SQL queries to Elasticsearch Query DSL.

## GitHub Copilot Slash Commands

### Command 1: /explain - Understand SQL to ES Conversion

**Usage:**
```
Select a SQL query, then use:
/explain Convert this SQL query to Elasticsearch Query DSL
```

**Example:**
```sql
-- Select this query
SELECT * FROM users WHERE email LIKE '%@gmail.com' AND created_at > '2024-01-01'
```

**Command:**
```
/explain How would you convert this SQL query to Elasticsearch? What are the key differences?
```

**Expected Explanation:**
- WHERE clause becomes bool query with must conditions
- LIKE becomes wildcard or match query
- Date comparison becomes range query
- Field selection maps to _source filtering

### Command 2: /fix - Fix Elasticsearch Query Issues

**Usage:**
```
Select an incorrect Elasticsearch query and use:
/fix This Elasticsearch query should match the SQL query above
```

**Example:**
```json
// Incorrect ES query
{
  "query": {
    "match": {
      "age": "25"  // Should be a range query
    }
  }
}

// SQL: SELECT * FROM users WHERE age > 25
```

**Command:**
```
/fix This query should find users with age greater than 25, not equal to 25
```

### Command 3: /doc - Generate Documentation

**Usage:**
```
/doc Explain this Elasticsearch query and its SQL equivalent
```

**Example:**
```json
{
  "query": {
    "bool": {
      "must": [
        { "range": { "price": { "gte": 10, "lte": 100 } } }
      ],
      "should": [
        { "match": { "category": "electronics" } },
        { "match": { "category": "computers" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

**Command:**
```
/doc Create documentation explaining this query and its SQL equivalent
```

### Command 4: /tests - Generate Test Cases

**Usage:**
```
/tests Generate test cases for SQL to Elasticsearch conversion
```

**Example:**
Create a test file and use:
```
/tests Create unit tests that verify SQL queries are correctly converted to Elasticsearch queries
```

**Expected Output:**
```javascript
describe('SQL to Elasticsearch Converter', () => {
  test('converts simple WHERE clause', () => {
    const sql = 'SELECT * FROM users WHERE age > 25';
    const esQuery = convertSqlToEs(sql);
    expect(esQuery.query.range.age.gt).toBe(25);
  });

  test('converts AND conditions to bool must', () => {
    const sql = 'SELECT * FROM users WHERE age > 25 AND status = "active"';
    const esQuery = convertSqlToEs(sql);
    expect(esQuery.query.bool.must).toHaveLength(2);
  });

  test('converts OR conditions to bool should', () => {
    const sql = 'SELECT * FROM users WHERE role = "admin" OR role = "moderator"';
    const esQuery = convertSqlToEs(sql);
    expect(esQuery.query.bool.should).toHaveLength(2);
  });
});
```

### Command 5: /new - Create New Conversion Function

**Usage:**
```
/new Create a new function to convert SQL aggregations to Elasticsearch aggregations
```

**Example:**
```
/new Create a TypeScript function that converts SQL GROUP BY with COUNT, AVG, SUM to Elasticsearch aggregations
```

**Expected Output:**
```typescript
interface SqlAggregation {
  groupBy: string[];
  aggregates: {
    function: 'COUNT' | 'AVG' | 'SUM' | 'MIN' | 'MAX';
    field: string;
    alias?: string;
  }[];
}

function convertSqlAggregationToEs(sqlAgg: SqlAggregation): any {
  const esQuery: any = {
    size: 0,
    aggs: {}
  };

  // Create terms aggregation for GROUP BY
  const groupByField = sqlAgg.groupBy[0]; // Simplified for single field
  esQuery.aggs[groupByField] = {
    terms: {
      field: groupByField
    },
    aggs: {}
  };

  // Add metric aggregations
  sqlAgg.aggregates.forEach(agg => {
    const aggName = agg.alias || `${agg.function.toLowerCase()}_${agg.field}`;
    const esAggType = agg.function.toLowerCase();
    
    esQuery.aggs[groupByField].aggs[aggName] = {
      [esAggType]: {
        field: agg.field
      }
    };
  });

  return esQuery;
}
```

### Command 6: /simplify - Simplify Complex Queries

**Usage:**
```
/simplify Break this complex Elasticsearch query into simpler parts
```

**Example:**
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              { "range": { "price": { "gte": 100, "lte": 200 } } },
              { "range": { "price": { "gte": 500, "lte": 600 } } }
            ]
          }
        },
        {
          "terms": { "category": ["electronics", "computers", "phones"] }
        }
      ]
    }
  }
}
```

**Command:**
```
/simplify Explain this query step by step and suggest if it can be simplified
```

### Command 7: Workspace Agent - Full Conversion

**Usage in Chat:**
```
@workspace Convert all SQL queries in this project to Elasticsearch queries
```

**Example:**
```
@workspace Find all SQL queries in .sql files and create corresponding Elasticsearch query files
```

### Command 8: Inline Chat - Quick Conversion

**Usage:**
Press `Ctrl+I` (or `Cmd+I` on Mac) while editing, then:

```
Convert this SQL WHERE clause to Elasticsearch bool query:
status = 'active' AND (priority = 'high' OR priority = 'urgent') AND created_at > NOW() - INTERVAL '7 days'
```

### Command 9: /optimize - Performance Optimization

**Usage:**
```
/optimize Improve the performance of this Elasticsearch query
```

**Example:**
```json
{
  "query": {
    "bool": {
      "must": [
        { "wildcard": { "email": "*@gmail.com" } },  // Slow
        { "match": { "description": "the quick brown fox" } }  // Could use match_phrase
      ]
    }
  }
}
```

**Command:**
```
/optimize Suggest performance improvements for this query
```

**Expected Suggestions:**
- Use term query with proper analyzer instead of wildcard
- Consider using match_phrase for exact phrase matching
- Add filter context for non-scoring queries
- Use bool filter instead of must for better caching

### Command 10: Generate Complete Conversion Pipeline

**Usage:**
```
/new Create a complete SQL to Elasticsearch query converter with error handling
```

**Example:**
```
/new Create a robust converter that handles:
1. SELECT with field selection
2. WHERE with AND/OR/NOT
3. ORDER BY with multiple fields
4. LIMIT and OFFSET
5. Basic aggregations (GROUP BY, COUNT, AVG, SUM)
Include error handling and validation
```

## Best Practices for Using Commands

### 1. Context is Key
Always select the relevant code before using a command. Copilot works better with context.

### 2. Iterate and Refine
Start with `/new` or `/explain`, then use `/fix` to refine the output.

### 3. Use Workspace Agent for Large Tasks
For repository-wide changes, use `@workspace` in the chat interface.

### 4. Combine Commands
Use `/explain` to understand, then `/new` to create, then `/tests` to verify.

### 5. Verify Generated Code
Always review and test generated Elasticsearch queries with real data.

## Demo Sequence (5-10 minutes)

### Minute 1-2: Simple Conversion
1. Show basic SQL query
2. Use `/explain` to understand conversion
3. Use inline chat to convert

### Minute 3-4: Complex Query
1. Show SQL with JOINs and aggregations
2. Use `/new` to create converter function
3. Demonstrate the conversion

### Minute 5-6: Testing
1. Use `/tests` to generate test cases
2. Run tests to verify conversions
3. Use `/fix` to correct any issues

### Minute 7-8: Optimization
1. Show a slow Elasticsearch query
2. Use `/optimize` for suggestions
3. Apply optimizations

### Minute 9-10: Documentation
1. Use `/doc` to document the queries
2. Use `@workspace` to find all SQL files
3. Show complete conversion pipeline

## Advanced Techniques

### Custom Instructions in Comments
```javascript
// @copilot Convert the following SQL to Elasticsearch
// Consider: 
// - Use filter context for better performance
// - Add fuzzy matching for text fields
// - Include proper field mapping
const sql = "SELECT * FROM users WHERE name LIKE '%John%' AND age > 25";
```

### Chain Multiple Conversions
```
1. Select SQL query
2. /explain conversion approach
3. /new create converter function
4. /tests add test cases
5. /doc document the solution
```

### Use Natural Language
```
Instead of: /new function to convert SQL
Use: /new Create a TypeScript function with full error handling that converts SQL WHERE clauses to Elasticsearch bool queries, supporting AND, OR, NOT, and nested conditions
```
