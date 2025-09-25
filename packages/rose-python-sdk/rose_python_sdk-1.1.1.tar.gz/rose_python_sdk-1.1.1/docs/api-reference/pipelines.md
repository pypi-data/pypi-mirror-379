# Pipelines API

The Pipelines API provides methods to manage recommendation pipelines, which process datasets to generate recommendations.

## Create Pipeline

Create a new recommendation pipeline.

### Method Signature

```python
client.pipelines.create(
    name: str,
    properties: Dict[str, Any]
) -> CreatePipelineResponse
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `str` | Yes | The pipeline name |
| `properties` | `Dict[str, Any]` | Yes | The pipeline configuration properties |

### Examples

#### Basic Pipeline Creation

```python
# Create a collaborative filtering pipeline
pipeline = client.pipelines.create(
    name="collaborative_filtering",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100,
        "regularization": 0.01
    }
)

print(f"Created pipeline: {pipeline.pipeline_id}")
```

#### Advanced Pipeline Configuration

```python
# Create a more complex pipeline
pipeline = client.pipelines.create(
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
                "features": ["genre", "director", "year"]
            }
        ],
        "min_support": 5,
        "max_recommendations": 100
    }
)
```

### Response

```python
CreatePipelineResponse(
    pipeline_id="pipeline_12345"
)
```

## List Pipelines

Get a list of all pipelines in your account.

### Method Signature

```python
client.pipelines.list() -> List[Pipeline]
```

### Examples

```python
# Get all pipelines
pipelines = client.pipelines.list()

for pipeline in pipelines:
    print(f"Pipeline: {pipeline.pipeline_name} (ID: {pipeline.pipeline_id})")
    print(f"Status: {pipeline.status}")
    print(f"Properties: {pipeline.properties}")
```

### Response

```python
[
    Pipeline(
        account_id="account_123",
        pipeline_name="collaborative_filtering",
        pipeline_id="pipeline_12345",
        status="CREATE SUCCESSFUL",
        properties={
            "algorithm": "matrix_factorization",
            "factors": 50,
            "iterations": 100
        }
    )
]
```

## Get Pipeline

Retrieve a specific pipeline by ID.

### Method Signature

```python
client.pipelines.get(pipeline_id: str) -> Pipeline
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pipeline_id` | `str` | Yes | The pipeline ID |

### Examples

```python
# Get a specific pipeline
pipeline = client.pipelines.get("pipeline_12345")

print(f"Pipeline: {pipeline.pipeline_name}")
print(f"Status: {pipeline.status}")
print(f"Algorithm: {pipeline.properties.get('algorithm')}")
```

## Update Pipeline

Update an existing pipeline's properties.

### Method Signature

```python
client.pipelines.update(
    pipeline_id: str,
    properties: Dict[str, Any]
) -> None
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pipeline_id` | `str` | Yes | The pipeline ID |
| `properties` | `Dict[str, Any]` | Yes | The new pipeline properties |

### Examples

```python
# Update pipeline properties
client.pipelines.update(
    pipeline_id="pipeline_12345",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 100,  # Increased from 50
        "iterations": 200,  # Increased from 100
        "regularization": 0.005  # Decreased regularization
    }
)

print("Pipeline updated successfully")
```

## Delete Pipeline

Delete a pipeline and all its associated queries.

### Method Signature

```python
client.pipelines.delete(pipeline_id: str) -> None
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pipeline_id` | `str` | Yes | The pipeline ID to delete |

### Examples

```python
# Delete a pipeline
client.pipelines.delete("pipeline_12345")
print("Pipeline deleted successfully")
```

## List Queries

Get all queries associated with a pipeline.

### Method Signature

```python
client.pipelines.list_queries(pipeline_id: str) -> List[Query]
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pipeline_id` | `str` | Yes | The pipeline ID |

### Examples

```python
# Get queries for a pipeline
queries = client.pipelines.list_queries("pipeline_12345")

for query in queries:
    print(f"Query: {query.query_name} (ID: {query.query_id})")
    print(f"Static: {query.is_static}")
```

### Response

```python
[
    Query(
        pipeline_id="pipeline_12345",
        query_name="user_recommendations",
        query_id="query_67890",
        is_static=True
    ),
    Query(
        pipeline_id="pipeline_12345",
        query_name="item_similarity",
        query_id="query_67891",
        is_static=False
    )
]
```

### Pipeline Status Requirements

The `list_queries` method requires the pipeline to be in "CREATE SUCCESSFUL" status:

```python
try:
    queries = client.pipelines.list_queries("pipeline_12345")
except ValueError as e:
    print(f"Error: {e}")
    # Pipeline might still be processing
```

## Pipeline Status

Pipelines have different status values:

- `CREATE SUCCESSFUL`: Pipeline created and ready to use
- `CREATE FAILED`: Pipeline creation failed
- `UPDATE SUCCESSFUL`: Pipeline updated successfully
- `UPDATE FAILED`: Pipeline update failed
- `DELETE SUCCESSFUL`: Pipeline deleted successfully
- `DELETE FAILED`: Pipeline deletion failed

## Common Pipeline Properties

### Collaborative Filtering

```python
properties = {
    "algorithm": "collaborative_filtering",
    "similarity_metric": "cosine",  # or "pearson", "jaccard"
    "min_support": 5,
    "max_recommendations": 100
}
```

### Matrix Factorization

```python
properties = {
    "algorithm": "matrix_factorization",
    "factors": 50,
    "iterations": 100,
    "regularization": 0.01,
    "learning_rate": 0.01
}
```

### Content-Based Filtering

```python
properties = {
    "algorithm": "content_based",
    "features": ["genre", "director", "year", "rating"],
    "similarity_metric": "cosine",
    "min_support": 3
}
```

### Hybrid Approach

```python
properties = {
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
```

## Error Handling

```python
from rose_sdk import (
    RoseAPIError,
    RoseNotFoundError,
    RoseValidationError
)

try:
    pipeline = client.pipelines.get("pipeline_12345")
except RoseNotFoundError:
    print("Pipeline not found")
except RoseValidationError as e:
    print(f"Validation error: {e}")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Best Practices

1. **Choose Appropriate Algorithms**: Select algorithms based on your data and use case
2. **Tune Parameters**: Experiment with different parameter values for better performance
3. **Monitor Status**: Check pipeline status before using queries
4. **Handle Errors**: Always handle API errors gracefully
5. **Test Thoroughly**: Test pipelines with sample data before production use

## Examples

### Complete Pipeline Workflow

```python
# Create a pipeline
pipeline = client.pipelines.create(
    name="movie_recommendations",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100,
        "regularization": 0.01
    }
)

pipeline_id = pipeline.pipeline_id
print(f"Created pipeline: {pipeline_id}")

# Wait for pipeline to be ready (check status)
pipeline = client.pipelines.get(pipeline_id)
print(f"Pipeline status: {pipeline.status}")

# Get queries when ready
if pipeline.status == "CREATE SUCCESSFUL":
    queries = client.pipelines.list_queries(pipeline_id)
    print(f"Available queries: {[q.query_name for q in queries]}")
    
    # Use queries for recommendations
    for query in queries:
        print(f"Query: {query.query_name} (ID: {query.query_id})")
```

### Pipeline Management

```python
# List all pipelines
pipelines = client.pipelines.list()

# Find pipelines by name
movie_pipelines = [p for p in pipelines if "movie" in p.pipeline_name.lower()]

# Update a pipeline
if movie_pipelines:
    pipeline = movie_pipelines[0]
    client.pipelines.update(
        pipeline.pipeline_id,
        {
            "algorithm": "matrix_factorization",
            "factors": 100,  # Increased factors
            "iterations": 200  # Increased iterations
        }
    )
    print(f"Updated pipeline: {pipeline.pipeline_name}")

# Delete old pipelines
for pipeline in pipelines:
    if "old" in pipeline.pipeline_name.lower():
        client.pipelines.delete(pipeline.pipeline_id)
        print(f"Deleted old pipeline: {pipeline.pipeline_name}")
```
