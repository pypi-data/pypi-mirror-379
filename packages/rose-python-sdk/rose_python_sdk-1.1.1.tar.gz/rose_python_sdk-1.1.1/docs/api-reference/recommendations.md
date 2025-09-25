# Recommendations API

The Recommendations API provides methods to get personalized recommendations from trained pipelines.

## Get Recommendations

Get recommendation results from a specific query.

### Method Signature

```python
client.recommendations.get(
    query_id: str,
    parameters: Optional[Dict[str, Any]] = None
) -> Recommendation
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query_id` | `str` | Yes | The query ID from a trained pipeline |
| `parameters` | `Dict[str, Any]` | No | Parameters for the query (e.g., user_id) |

### Examples

#### Basic Usage

```python
# Get recommendations for a user
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user123"}
)

print(f"Recommendations: {recommendations.data}")
```

#### With Multiple Parameters

```python
# Get recommendations with additional parameters
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={
        "user_id": "user123",
        "category": "electronics",
        "limit": 10
    }
)

for item in recommendations.data:
    print(f"Recommended item: {item}")
```

### Response

```python
Recommendation(
    data=[
        {"item_id": "item123", "score": 0.95, "title": "Amazing Product"},
        {"item_id": "item456", "score": 0.87, "title": "Great Gadget"},
        {"item_id": "item789", "score": 0.82, "title": "Cool Item"}
    ]
)

# Expected output:
# Recommendations: [{'item_id': 'item123', 'score': 0.95, 'title': 'Amazing Product'}, ...]
```

## Batch Query

Get recommendations for multiple users in a single request.

### Method Signature

```python
client.recommendations.batch_query(
    query_id: str,
    payload: List[Dict[str, Any]]
) -> List[Recommendation]
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query_id` | `str` | Yes | The query ID from a trained pipeline |
| `payload` | `List[Dict[str, Any]]` | Yes | List of parameter groups for each user |

### Examples

#### Basic Batch Query

```python
# Get recommendations for multiple users
payload = [
    {"user_id": "user1"},
    {"user_id": "user2"},
    {"user_id": "user3"}
]

recommendations = client.recommendations.batch_query(
    query_id="your_query_id",
    payload=payload
)

for i, rec in enumerate(recommendations):
    print(f"User {i+1} recommendations: {rec.data}")
```

#### Batch Query with Different Parameters

```python
# Get recommendations with different parameters for each user
payload = [
    {"user_id": "user1", "category": "electronics"},
    {"user_id": "user2", "category": "books"},
    {"user_id": "user3", "category": "clothing"}
]

recommendations = client.recommendations.batch_query(
    query_id="your_query_id",
    payload=payload
)
```

### Response

```python
[
    Recommendation(data=[{"item_id": "item1", "score": 0.95}]),
    Recommendation(data=[{"item_id": "item2", "score": 0.87}]),
    Recommendation(data=[{"item_id": "item3", "score": 0.82}])
]

# Expected output:
# User 1 recommendations: [{'item_id': 'item1', 'score': 0.95}]
# User 2 recommendations: [{'item_id': 'item2', 'score': 0.87}]
# User 3 recommendations: [{'item_id': 'item3', 'score': 0.82}]
```

## Export Recommendations

Get information about exported recommendation results.

### Method Signature

```python
client.recommendations.get_export_info(
    query_id: str,
    expiration: Optional[int] = None
) -> RecommendationExportInfo
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query_id` | `str` | Yes | The query ID from a trained pipeline |
| `expiration` | `int` | No | The expiration time of the export information in seconds |

### Examples

#### Basic Export Info

```python
# Get export information
export_info = client.recommendations.get_export_info("your_query_id")

print(f"Export URL: {export_info.export}")
```

#### With Expiration

```python
# Get export information with expiration
export_info = client.recommendations.get_export_info(
    query_id="your_query_id",
    expiration=3600  # 1 hour
)
```

### Response

```python
RecommendationExportInfo(
    export={
        "url": "https://export.example.com/recommendations.csv"
    }
)
```

## Helper Functions

### Quick Get Recommendations

Use the helper function for easier recommendation retrieval:

```python
from rose_sdk import quick_get_recommendations

# Get recommendations for multiple users
user_ids = ["user1", "user2", "user3"]
recommendations = quick_get_recommendations(
    client=client,
    query_id="your_query_id",
    user_ids=user_ids,
    batch=True  # Use batch query for efficiency
)

for i, rec in enumerate(recommendations):
    print(f"User {user_ids[i]}: {rec}")
```

### Individual vs Batch Queries

```python
# Individual queries (for single users)
recommendations = quick_get_recommendations(
    client=client,
    query_id="your_query_id",
    user_ids=["user1"],
    batch=False
)

# Batch queries (for multiple users - more efficient)
recommendations = quick_get_recommendations(
    client=client,
    query_id="your_query_id",
    user_ids=["user1", "user2", "user3"],
    batch=True
)
```

## Error Handling

```python
from rose_sdk import (
    RoseAPIError,
    RoseNotFoundError,
    RoseValidationError
)

try:
    recommendations = client.recommendations.get(
        query_id="your_query_id",
        parameters={"user_id": "user123"}
    )
except RoseNotFoundError:
    print("Query not found")
except RoseValidationError as e:
    print(f"Validation error: {e}")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Best Practices

1. **Use Batch Queries**: For multiple users, use batch queries for better performance
2. **Handle Errors**: Always handle API errors gracefully
3. **Cache Results**: Cache recommendations for better performance
4. **Monitor Performance**: Track recommendation quality and response times
5. **Validate Parameters**: Ensure query parameters are valid before making requests

## Examples

### E-commerce Recommendation System

```python
# Complete recommendation workflow
from rose_sdk import quick_setup_recommendation_system

# Set up recommendation system
dataset_id, pipeline_id, query_ids = quick_setup_recommendation_system(
    client=client,
    dataset_name="ecommerce_interactions",
    records=[
        {"user_id": "user1", "product_id": "product1", "rating": 4.5, "category": "electronics"},
        {"user_id": "user1", "product_id": "product2", "rating": 3.0, "category": "clothing"},
        {"user_id": "user2", "product_id": "product1", "rating": 5.0, "category": "electronics"}
    ],
    pipeline_name="product_recommendations",
    pipeline_properties={
        "algorithm": "collaborative_filtering",
        "similarity_metric": "cosine"
    },
    identifier_fields=["user_id", "product_id"],
    required_fields=["rating"]
)

# Get recommendations for users
user_ids = ["user1", "user2"]
recommendations = quick_get_recommendations(
    client=client,
    query_id=query_ids[0],
    user_ids=user_ids,
    batch=True
)

# Display results
for i, rec in enumerate(recommendations):
    print(f"Recommendations for {user_ids[i]}: {rec}")
```

### Movie Recommendation System

```python
# Movie recommendation example
recommendations = client.recommendations.get(
    query_id="movie_recommendations_query",
    parameters={
        "user_id": "movie_lover_123",
        "genre": "action",
        "year_min": 2020
    }
)

print("Recommended movies:")
for movie in recommendations.data:
    print(f"- {movie.get('title', 'Unknown')} (Score: {movie.get('score', 0)})")
```

### Real-time Recommendations

```python
# Real-time recommendation for current user
def get_homepage_recommendations(user_id: str, count: int = 10):
    """Get homepage recommendations for a user."""
    try:
        recommendations = client.recommendations.get(
            query_id="homepage_recommendations",
            parameters={
                "user_id": user_id,
                "limit": count,
                "context": "homepage"
            }
        )
        return recommendations.data
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return []

# Use in your application
user_id = "current_user_123"
recs = get_homepage_recommendations(user_id, count=12)
```
