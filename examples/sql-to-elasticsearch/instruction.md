# SQL to Elasticsearch Query Conversion - Instructions

## Overview
This instruction file demonstrates how to use GitHub Copilot to convert SQL queries into Elasticsearch Query DSL (Domain Specific Language).

## GitHub Copilot Instructions

### Instruction 1: Basic SQL SELECT to Elasticsearch Query

**Prompt:**
```
Convert the following SQL query to Elasticsearch Query DSL:
SELECT * FROM users WHERE age > 25 AND status = 'active' ORDER BY created_at DESC LIMIT 10
```

**Expected Output:**
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "age": {
              "gt": 25
            }
          }
        },
        {
          "term": {
            "status": "active"
          }
        }
      ]
    }
  },
  "sort": [
    {
      "created_at": {
        "order": "desc"
      }
    }
  ],
  "size": 10
}
```

### Instruction 2: SQL JOIN to Elasticsearch Nested Query

**Prompt:**
```
Convert this SQL query with JOIN to Elasticsearch nested query:
SELECT u.name, o.order_id, o.total 
FROM users u 
INNER JOIN orders o ON u.user_id = o.user_id 
WHERE o.total > 100 AND u.country = 'USA'
```

**Expected Output:**
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "country": "USA"
          }
        },
        {
          "nested": {
            "path": "orders",
            "query": {
              "range": {
                "orders.total": {
                  "gt": 100
                }
              }
            }
          }
        }
      ]
    }
  },
  "_source": ["name", "orders.order_id", "orders.total"]
}
```

### Instruction 3: SQL Aggregation to Elasticsearch Aggregation

**Prompt:**
```
Convert this SQL aggregation query to Elasticsearch aggregation:
SELECT category, COUNT(*) as count, AVG(price) as avg_price, MAX(price) as max_price
FROM products
WHERE in_stock = true
GROUP BY category
HAVING COUNT(*) > 5
ORDER BY avg_price DESC
```

**Expected Output:**
```json
{
  "query": {
    "term": {
      "in_stock": true
    }
  },
  "size": 0,
  "aggs": {
    "categories": {
      "terms": {
        "field": "category",
        "order": {
          "avg_price": "desc"
        },
        "min_doc_count": 6
      },
      "aggs": {
        "count": {
          "value_count": {
            "field": "category"
          }
        },
        "avg_price": {
          "avg": {
            "field": "price"
          }
        },
        "max_price": {
          "max": {
            "field": "price"
          }
        }
      }
    }
  }
}
```

### Instruction 4: SQL LIKE to Elasticsearch Wildcard/Match Query

**Prompt:**
```
Convert this SQL LIKE query to Elasticsearch:
SELECT * FROM articles 
WHERE title LIKE '%machine learning%' 
OR description LIKE '%AI%'
AND published_date >= '2024-01-01'
```

**Expected Output:**
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "published_date": {
              "gte": "2024-01-01"
            }
          }
        }
      ],
      "should": [
        {
          "match_phrase": {
            "title": "machine learning"
          }
        },
        {
          "match": {
            "description": "AI"
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}
```

### Instruction 5: Complex SQL with Multiple Conditions

**Prompt:**
```
Convert this complex SQL query to Elasticsearch:
SELECT * FROM events
WHERE (event_type = 'click' OR event_type = 'view')
AND user_id IN (100, 200, 300)
AND timestamp BETWEEN '2024-01-01' AND '2024-12-31'
AND metadata->>'source' = 'mobile'
ORDER BY timestamp DESC
LIMIT 20 OFFSET 40
```

**Expected Output:**
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "terms": {
            "user_id": [100, 200, 300]
          }
        },
        {
          "range": {
            "timestamp": {
              "gte": "2024-01-01",
              "lte": "2024-12-31"
            }
          }
        },
        {
          "term": {
            "metadata.source": "mobile"
          }
        }
      ],
      "should": [
        {
          "term": {
            "event_type": "click"
          }
        },
        {
          "term": {
            "event_type": "view"
          }
        }
      ],
      "minimum_should_match": 1
    }
  },
  "sort": [
    {
      "timestamp": {
        "order": "desc"
      }
    }
  ],
  "from": 40,
  "size": 20
}
```

## Tips for Using GitHub Copilot

1. **Be Specific**: Include context about your data structure and index mapping
2. **Iterative Refinement**: Start with basic queries and gradually add complexity
3. **Use Comments**: Add comments describing the desired output format
4. **Leverage Chat**: Use GitHub Copilot Chat for explanations and variations
5. **Test Queries**: Always test generated queries with sample data

## Common Patterns

### SQL to Elasticsearch Mapping

| SQL Concept | Elasticsearch Equivalent |
|-------------|-------------------------|
| WHERE | query.bool.must |
| OR | query.bool.should |
| NOT | query.bool.must_not |
| ORDER BY | sort |
| LIMIT | size |
| OFFSET | from |
| GROUP BY | aggregations.terms |
| COUNT | aggregations.value_count |
| AVG | aggregations.avg |
| SUM | aggregations.sum |
| MIN/MAX | aggregations.min/max |
| LIKE | match/wildcard/regexp |
| IN | terms |
| BETWEEN | range.gte/lte |

## Advanced Use Cases

### Full-Text Search with Scoring
```
Instruction: "Convert this SQL to Elasticsearch with relevance scoring and fuzzy matching"
SQL: SELECT * FROM products WHERE name LIKE '%laptop%' OR description LIKE '%laptop%'
```

### Geospatial Queries
```
Instruction: "Convert this location-based SQL query to Elasticsearch geo query"
SQL: SELECT * FROM stores WHERE distance(lat, lon, 40.7128, -74.0060) < 10
```

### Date Histogram Aggregations
```
Instruction: "Convert this time-based SQL aggregation to Elasticsearch date histogram"
SQL: SELECT DATE_TRUNC('day', created_at) as day, COUNT(*) FROM orders GROUP BY day
```
