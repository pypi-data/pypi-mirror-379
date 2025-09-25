# API Reference Overview

This section provides comprehensive documentation for the Rose Python SDK based on the actual implementation.

## Base Information

- **SDK Version**: `1.1.0`
- **API Version**: `1.0`
- **Base URL**: `https://admin.rose.blendvision.com`
- **Content Type**: `application/json`
- **Authentication**: Bearer Token

## Quick Start

```python
from rose_sdk import RoseClient

# Initialize the client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# Get recommendations
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user123"}
)
```

## Core Services

The Rose Python SDK is organized into the following services:

### 🏢 Account Management
- Account creation and management
- Token generation and management
- Account information retrieval

### 📊 Dataset Management
- [Create Dataset](datasets.md#create-dataset)
- [List Datasets](datasets.md#list-datasets)
- [Get Dataset](datasets.md#get-dataset)
- [Update Dataset](datasets.md#update-dataset)
- [Delete Dataset](datasets.md#delete-dataset)
- [Dataset Records](datasets.md#records)
- [Batch Operations](datasets.md#batch-operations)

### 🔄 Pipeline Management
- [Create Pipeline](pipelines.md#create-pipeline)
- [List Pipelines](pipelines.md#list-pipelines)
- [Get Pipeline](pipelines.md#get-pipeline)
- [Update Pipeline](pipelines.md#update-pipeline)
- [Delete Pipeline](pipelines.md#delete-pipeline)
- [Pipeline Queries](pipelines.md#queries)

### 🎯 Recommendations
- [Get Recommendations](recommendations.md#get-recommendations)
- [Batch Recommendations](recommendations.md#batch-recommendations)
- [Export Recommendations](recommendations.md#export-recommendations)

### 👥 Role Management
- [Create Role](roles.md#create-role)
- [List Roles](roles.md#list-roles)
- [Get Role](roles.md#get-role)
- [Update Role](roles.md#update-role)
- [Delete Role](roles.md#delete-role)

## Data Models

### Dataset
```python
class Dataset:
    account_id: str
    dataset_name: str
    dataset_id: str
    schema: Schema
    status: str
    created_at: str
    updated_at: str
```

### Recommendation
```python
class Recommendation:
    data: List[Dict[str, Any]]
```

### Pipeline
```python
class Pipeline:
    pipeline_id: str
    pipeline_name: str
    properties: Dict[str, Any]
    status: str
    created_at: str
    updated_at: str
```

### Record
```python
class Record:
    # Rose format with type information
    field_name: Dict[str, Any]  # {"str": "value"} or {"int": 123}
```

## Error Handling

The SDK provides comprehensive error handling with specific exception types:

```python
from rose_sdk import (
    RoseAPIError,
    RoseAuthenticationError,
    RosePermissionError,
    RoseNotFoundError,
    RoseValidationError,
    RoseConflictError,
    RoseServerError,
    RoseTimeoutError
)

try:
    dataset = client.datasets.get("dataset_id")
except RoseNotFoundError:
    print("Dataset not found")
except RoseAuthenticationError:
    print("Authentication failed")
except RoseAPIError as e:
    print(f"API Error: {e}")
```

## Helper Functions

The SDK includes high-level helper functions for common operations:

```python
from rose_sdk import (
    quick_create_dataset,
    quick_add_records,
    quick_get_records,
    quick_create_dataset_with_data,
    quick_batch_upload,
    quick_get_recommendations,
    quick_setup_recommendation_system,
    get_dataset_summary
)

# Quick dataset creation with data
dataset_id = quick_create_dataset_with_data(
    client=client,
    name="user_interactions",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5},
        {"user_id": "user1", "item_id": "item2", "rating": 3.0}
    ],
    identifier_fields=["user_id", "item_id"]
)

# Quick recommendations
recommendations = quick_get_recommendations(
    client=client,
    query_id="query_id",
    user_ids=["user1", "user2"],
    batch=True
)
```

## Schema Management

The SDK provides utilities for schema inference and management:

```python
from rose_sdk import build_schema_from_sample

# Build schema from sample data
schema = build_schema_from_sample(
    sample_records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5}
    ],
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)
```

## Batch Operations

Efficient batch processing for large datasets:

```python
# Batch upload records
batch_id = client.datasets.batch.start_upload(dataset_id)
client.datasets.batch.upload_batch(dataset_id, batch_id, records)
client.datasets.batch.complete_upload(dataset_id, batch_id)

# Batch recommendations
recommendations = client.recommendations.batch_query(
    query_id="query_id",
    payload=[
        {"user_id": "user1"},
        {"user_id": "user2"}
    ]
)
```

## Examples

### Complete Recommendation System Setup

```python
from rose_sdk import quick_setup_recommendation_system

# Set up complete recommendation system
dataset_id, pipeline_id, query_ids = quick_setup_recommendation_system(
    client=client,
    dataset_name="user_interactions",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5},
        {"user_id": "user1", "item_id": "item2", "rating": 3.0},
        {"user_id": "user2", "item_id": "item1", "rating": 5.0}
    ],
    pipeline_name="collaborative_filtering",
    pipeline_properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100
    },
    identifier_fields=["user_id", "item_id"]
)

# Get recommendations
recommendations = client.recommendations.get(
    query_id=query_ids[0],
    parameters={"user_id": "user1"}
)
```

## Next Steps

- [Dataset Management](datasets.md) - Manage your datasets
- [Pipeline Management](pipelines.md) - Create and manage pipelines
- [Recommendations](recommendations.md) - Get personalized recommendations
- [Role Management](roles.md) - Handle permissions and roles
- [Account Management](accounts.md) - Manage accounts and authentication
