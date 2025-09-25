# Pipelines & Queries

Understanding pipelines and queries is essential for building effective recommendation systems with the Rose Recommendation Service.

## What are Pipelines?

A **pipeline** is a machine learning workflow that processes your dataset to generate recommendations. It defines:
- **Algorithm** - The recommendation algorithm to use
- **Parameters** - Configuration settings for the algorithm
- **Data processing** - How to transform and prepare your data

## What are Queries?

A **query** is a specific way to retrieve recommendations from a trained pipeline. Each pipeline can have multiple queries that serve different purposes:
- **User recommendations** - Get items for a specific user
- **Item similarity** - Find similar items
- **Trending items** - Get popular items
- **Custom queries** - Specialized recommendation logic

## Pipeline Lifecycle

### 1. Create Pipeline

```python
# Create a collaborative filtering pipeline
pipeline = client.pipelines.create(
    name="movie_recommendations",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100,
        "regularization": 0.01
    }
)

print(f"Created pipeline: {pipeline.pipeline_id}")
# Expected output: Created pipeline: pipeline_12345
```

### 2. Pipeline Processing

The pipeline automatically processes your dataset:
- **Data validation** - Ensures data meets requirements
- **Model training** - Trains the recommendation model
- **Query generation** - Creates available queries

### 3. Check Pipeline Status

```python
# Check if pipeline is ready
pipeline = client.pipelines.get("pipeline_12345")
print(f"Pipeline status: {pipeline.status}")

# Expected outputs:
# - "CREATE SUCCESSFUL" - Ready to use
# - "CREATE FAILED" - Processing failed
# - "UPDATE SUCCESSFUL" - Updated successfully
```

### 4. Get Available Queries

```python
# Get queries when pipeline is ready
if pipeline.status == "CREATE SUCCESSFUL":
    queries = client.pipelines.list_queries("pipeline_12345")
    
    for query in queries:
        print(f"Query: {query.query_name} (ID: {query.query_id})")
        print(f"Static: {query.is_static}")
    
    # Expected output:
    # Query: user_recommendations (ID: query_67890)
    # Static: True
    # Query: item_similarity (ID: query_67891)
    # Static: False
```

### 5. Use Queries for Recommendations

```python
# Get recommendations using a query
recommendations = client.recommendations.get(
    query_id="query_67890",
    parameters={"user_id": "user123"}
)

print(f"Recommendations: {recommendations.data}")
# Expected output: [{"item_id": "item1", "score": 0.95}, ...]
```

## Common Pipeline Algorithms

### Collaborative Filtering

Finds users with similar preferences and recommends items they liked:

```python
collaborative_pipeline = client.pipelines.create(
    name="collaborative_filtering",
    properties={
        "algorithm": "collaborative_filtering",
        "similarity_metric": "cosine",
        "min_support": 5,
        "max_recommendations": 100
    }
)
```

**Best for**: User-item interactions (ratings, purchases, views)

### Matrix Factorization

Decomposes user-item interaction matrix into lower-dimensional representations:

```python
matrix_pipeline = client.pipelines.create(
    name="matrix_factorization",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100,
        "regularization": 0.01,
        "learning_rate": 0.01
    }
)
```

**Best for**: Sparse interaction data, cold start problems

### Content-Based Filtering

Recommends items similar to those a user has interacted with:

```python
content_pipeline = client.pipelines.create(
    name="content_based",
    properties={
        "algorithm": "content_based",
        "features": ["genre", "director", "year", "rating"],
        "similarity_metric": "cosine",
        "min_support": 3
    }
)
```

**Best for**: Rich item metadata, new users

### Hybrid Approach

Combines multiple algorithms for better recommendations:

```python
hybrid_pipeline = client.pipelines.create(
    name="hybrid_recommendations",
    properties={
        "algorithm": "hybrid",
        "components": [
            {
                "type": "collaborative_filtering",
                "weight": 0.7,
                "similarity_metric": "cosine"
            },
            {
                "type": "content_based",
                "weight": 0.3,
                "features": ["genre", "director"]
            }
        ]
    }
)
```

**Best for**: Complex scenarios requiring multiple signals

## Query Types

### Static Queries

Pre-computed recommendations that are fast to retrieve:

```python
# Static query - recommendations are pre-computed
recommendations = client.recommendations.get(
    query_id="static_user_recommendations",
    parameters={"user_id": "user123"}
)

# Expected: Fast response, limited personalization
```

### Dynamic Queries

Real-time recommendations computed on-demand:

```python
# Dynamic query - computed in real-time
recommendations = client.recommendations.get(
    query_id="dynamic_similarity",
    parameters={
        "item_id": "item123",
        "category": "electronics",
        "limit": 10
    }
)

# Expected: Slower response, highly personalized
```

## Pipeline Parameters

### Collaborative Filtering Parameters

```python
properties = {
    "algorithm": "collaborative_filtering",
    "similarity_metric": "cosine",  # cosine, pearson, jaccard
    "min_support": 5,               # Minimum interactions for similarity
    "max_recommendations": 100,     # Maximum recommendations per query
    "exclude_known": True           # Exclude items user already interacted with
}
```

### Matrix Factorization Parameters

```python
properties = {
    "algorithm": "matrix_factorization",
    "factors": 50,                  # Number of latent factors
    "iterations": 100,              # Training iterations
    "regularization": 0.01,         # L2 regularization
    "learning_rate": 0.01,          # Learning rate
    "bias": True                    # Include bias terms
}
```

### Content-Based Parameters

```python
properties = {
    "algorithm": "content_based",
    "features": ["genre", "director", "year"],  # Features to use
    "similarity_metric": "cosine",              # Similarity measure
    "min_support": 3,                           # Minimum feature matches
    "tfidf": True                               # Use TF-IDF weighting
}
```

## Query Parameters

### User Recommendation Parameters

```python
# Basic user recommendations
parameters = {
    "user_id": "user123"
}

# Advanced user recommendations
parameters = {
    "user_id": "user123",
    "category": "electronics",
    "exclude_items": ["item1", "item2"],
    "limit": 20,
    "min_score": 0.5
}
```

### Item Similarity Parameters

```python
# Find similar items
parameters = {
    "item_id": "item123"
}

# Find similar items with filters
parameters = {
    "item_id": "item123",
    "category": "electronics",
    "limit": 10,
    "min_similarity": 0.3
}
```

## Pipeline Status Management

### Status Values

- `CREATE SUCCESSFUL` - Pipeline created and ready
- `CREATE FAILED` - Pipeline creation failed
- `UPDATE SUCCESSFUL` - Pipeline updated successfully
- `UPDATE FAILED` - Pipeline update failed
- `DELETE SUCCESSFUL` - Pipeline deleted successfully
- `DELETE FAILED` - Pipeline deletion failed

### Status Checking

```python
def wait_for_pipeline_ready(pipeline_id, max_wait=300):
    """Wait for pipeline to be ready."""
    import time
    
    start_time = time.time()
    while time.time() - start_time < max_wait:
        pipeline = client.pipelines.get(pipeline_id)
        
        if pipeline.status == "CREATE SUCCESSFUL":
            print("✅ Pipeline is ready!")
            return True
        elif pipeline.status == "CREATE FAILED":
            print("❌ Pipeline creation failed!")
            return False
        else:
            print(f"⏳ Pipeline status: {pipeline.status}")
            time.sleep(10)
    
    print("⏰ Timeout waiting for pipeline")
    return False

# Usage
if wait_for_pipeline_ready("pipeline_12345"):
    queries = client.pipelines.list_queries("pipeline_12345")
    print(f"Available queries: {len(queries)}")
```

## Best Practices

### 1. Choose the Right Algorithm

```python
# For user-item interactions
if has_user_item_data:
    algorithm = "collaborative_filtering"
    
# For rich item metadata
elif has_item_metadata:
    algorithm = "content_based"
    
# For sparse data
elif data_is_sparse:
    algorithm = "matrix_factorization"
    
# For complex scenarios
else:
    algorithm = "hybrid"
```

### 2. Tune Parameters Carefully

```python
# Start with default parameters
pipeline = client.pipelines.create(
    name="test_pipeline",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 20,        # Start small
        "iterations": 50      # Start small
    }
)

# Test performance, then increase if needed
```

### 3. Use Appropriate Queries

```python
# For real-time recommendations
if need_real_time:
    use_dynamic_queries = True
    
# For high-volume recommendations
elif high_volume:
    use_static_queries = True
```

### 4. Monitor Pipeline Performance

```python
# Check pipeline status regularly
def monitor_pipeline(pipeline_id):
    pipeline = client.pipelines.get(pipeline_id)
    
    if pipeline.status == "CREATE FAILED":
        print("❌ Pipeline failed - check logs")
        return False
    elif pipeline.status == "CREATE SUCCESSFUL":
        print("✅ Pipeline ready")
        return True
    else:
        print(f"⏳ Pipeline processing: {pipeline.status}")
        return False
```

## Common Use Cases

### E-commerce Recommendations

```python
# Create e-commerce pipeline
ecommerce_pipeline = client.pipelines.create(
    name="ecommerce_recommendations",
    properties={
        "algorithm": "hybrid",
        "components": [
            {
                "type": "collaborative_filtering",
                "weight": 0.6,
                "similarity_metric": "cosine"
            },
            {
                "type": "content_based", 
                "weight": 0.4,
                "features": ["category", "brand", "price_range"]
            }
        ]
    }
)

# Get product recommendations
recommendations = client.recommendations.get(
    query_id="product_recommendations",
    parameters={
        "user_id": "customer_123",
        "category": "electronics",
        "limit": 12
    }
)
```

### Content Recommendations

```python
# Create content pipeline
content_pipeline = client.pipelines.create(
    name="content_recommendations",
    properties={
        "algorithm": "content_based",
        "features": ["topic", "author", "length", "difficulty"],
        "similarity_metric": "cosine",
        "tfidf": True
    }
)

# Get article recommendations
recommendations = client.recommendations.get(
    query_id="article_recommendations",
    parameters={
        "user_id": "reader_456",
        "topic": "technology",
        "limit": 10
    }
)
```

Understanding pipelines and queries is key to building effective recommendation systems. Choose the right algorithm for your data, tune parameters carefully, and use appropriate queries for your use case.
