# Rose Python SDK

> A comprehensive Python SDK for interacting with the Rose Recommendation Service API

[![PyPI version](https://badge.fury.io/py/rose-python-sdk.svg)](https://badge.fury.io/py/rose-python-sdk)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🚀 **Complete API Coverage** - Full support for all Rose Recommendation Service endpoints
- 🛡️ **Type Safety** - Built with Pydantic for robust data validation and type hints
- ⚡ **Comprehensive Error Handling** - Detailed exception classes for different error scenarios
- 📦 **Batch Operations** - Efficient batch data processing and upload capabilities
- 🔧 **Schema Management** - Automatic schema inference and validation
- 🔄 **Pipeline Management** - Intuitive pipeline creation and management tools
- 👥 **Role-Based Access Control** - Complete permission and role management system
- 🛠️ **Helper Functions** - High-level utilities for common operations

## Quick Start

```python
from rose_sdk import RoseClient, quick_create_dataset_with_data

# Initialize the client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

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

# Create a pipeline
pipeline = client.pipelines.create(
    name="collaborative_filtering",
    properties={
        "algorithm": "matrix_factorization",
        "factors": 50,
        "iterations": 100
    }
)

# Get recommendations
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user1"}
)

print(f"Recommendations: {recommendations.data}")
```

## Installation

```bash
pip install rose-python-sdk
```


**Made with ❤️ for the Rose community**
