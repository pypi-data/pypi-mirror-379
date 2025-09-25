# Getting Started

Welcome to the Rose Python SDK! This guide will help you get up and running quickly with the Rose Recommendation Service.

## Prerequisites

- Python 3.8 or higher
- A Rose API access token
- Basic knowledge of Python

## Installation

Install the Rose Python SDK using pip:

```bash
pip install rose-python-sdk
```

## Basic Usage

### 1. Import the SDK

```python
from rose_sdk import RoseClient, quick_create_dataset_with_data
```

### 2. Initialize the Client

```python
# Initialize the client with your credentials
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)
```

### 3. Create Your First Dataset

```python
# Create a dataset with sample data
dataset_id = quick_create_dataset_with_data(
    client=client,
    name="user_interactions",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5},
        {"user_id": "user1", "item_id": "item2", "rating": 3.0},
        {"user_id": "user2", "item_id": "item1", "rating": 5.0}
    ],
    identifier_fields=["user_id", "item_id"]
)

print(f"Created dataset: {dataset_id}")
```

### 4. Create a Pipeline

```python
# Create a recommendation pipeline
pipeline = client.pipelines.create(
    name="collaborative_filtering",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100
    }
)

print(f"Created pipeline: {pipeline.pipeline_id}")
```

### 5. Get Recommendations

```python
# Get recommendations
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user1"}
)

print(f"Recommendations: {recommendations.data}")
```

## Quick Start with Helper Functions

The Rose SDK provides helper functions to simplify common operations:

```python
from rose_sdk import quick_setup_recommendation_system

# Set up a complete recommendation system in one call
dataset_id, pipeline_id, query_ids = quick_setup_recommendation_system(
    client=client,
    dataset_name="movie_ratings",
    records=[
        {"user_id": "user1", "movie_id": "movie1", "rating": 4.5, "genre": "action"},
        {"user_id": "user1", "movie_id": "movie2", "rating": 3.0, "genre": "comedy"},
        {"user_id": "user2", "movie_id": "movie1", "rating": 5.0, "genre": "action"}
    ],
    pipeline_name="movie_recommendations",
    pipeline_properties={
        "algorithm": "collaborative_filtering",
        "similarity_metric": "cosine"
    },
    identifier_fields=["user_id", "movie_id"],
    required_fields=["rating"]
)

# Get recommendations
recommendations = client.recommendations.get(
    query_id=query_ids[0],
    parameters={"user_id": "user1"}
)
```

## Configuration

### Client Options

```python
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token",
    timeout=30,  # Request timeout in seconds
    max_retries=3  # Maximum retry attempts
)
```

### Authentication

The Rose SDK uses Bearer token authentication:

```python
# Set access token after initialization
client.set_access_token("new_access_token")
```

## Core Concepts

### Datasets
- Store your training data (user interactions, ratings, etc.)
- Define schemas with identifier and required fields
- Support batch operations for large datasets

### Pipelines
- Define recommendation algorithms and parameters
- Process datasets to generate recommendations
- Support various algorithms (collaborative filtering, matrix factorization, etc.)

### Recommendations
- Query trained pipelines to get personalized recommendations
- Support batch queries for multiple users
- Export recommendations for offline use

## Error Handling

The SDK provides comprehensive error handling:

```python
from rose_sdk import (
    RoseAPIError,
    RoseAuthenticationError,
    RoseNotFoundError,
    RoseValidationError
)

try:
    dataset = client.datasets.get("dataset_id")
except RoseNotFoundError:
    print("Dataset not found")
except RoseAuthenticationError:
    print("Authentication failed")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Next Steps

- [Installation Guide](installation.md) - Detailed setup instructions
- [API Reference](api-reference/overview.md) - Complete API documentation
- [Helper Functions](examples/helper-functions.md) - Learn about helper functions
- [Examples](examples/basic-examples.md) - See more examples

## Need Help?

- Check out our [API Reference](api-reference/overview.md) for detailed documentation
- Visit our [GitHub repository](https://github.com/luli0034/rose-python-sdk) for examples
- Open an [issue](https://github.com/luli0034/rose-python-sdk/issues) if you need support
