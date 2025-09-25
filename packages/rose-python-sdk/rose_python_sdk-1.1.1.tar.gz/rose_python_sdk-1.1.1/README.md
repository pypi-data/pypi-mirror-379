# Rose Python SDK

<div align="center">
  <img src="./docs/assets/images/rose-logo.png" alt="Rose Python SDK" width="200" />
</div>

A comprehensive Python SDK for interacting with the Rose Recommendation Service API. This SDK provides a clean, type-safe interface for managing datasets, pipelines, roles, and recommendations.

## 🚀 Features

- **Complete API Coverage**: Full support for all Rose Recommendation Service endpoints
- **Type Safety**: Built with Pydantic for robust data validation and type hints
- **Comprehensive Error Handling**: Detailed exception classes for different error scenarios
- **Batch Operations**: Efficient batch data processing and upload capabilities
- **Schema Management**: Automatic schema inference and validation
- **Pipeline Management**: Intuitive pipeline creation and management tools
- **Role-Based Access Control**: Complete permission and role management system
- **Helper Functions**: High-level utilities for common operations

## 📦 Installation

```bash
pip install rose-python-sdk
```

## 🏃‍♂️ Quick Start

### Basic Setup

```python
from rose_sdk import RoseClient

# Initialize the client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)
```

### Create a Dataset with Data

```python
from rose_sdk import quick_create_dataset_with_data

# Create dataset with sample data
dataset_id = quick_create_dataset_with_data(
    client=client,
    name="user_interactions",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5},
        {"user_id": "user1", "item_id": "item2", "rating": 3.0},
        {"user_id": "user2", "item_id": "item1", "rating": 5.0}
    ],
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)
```

### Create a Recommendation Pipeline

```python
from rose_sdk.utils import create_pipeline

# Create a pipeline with dataset mapping
pipeline_response = create_pipeline(
    client=client,
    account_id="your_account",
    pipeline_name="recommendation_pipeline",
    scenario="realtime_leaderboard",
    dataset_mapping={
        "interaction": dataset_id,  # Map pipeline key to your dataset
        "metadata": "your_metadata_dataset_id"
    }
)
```

### Get Recommendations

```python
# Get recommendations for a user
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user1"}
)

print(f"Recommendations: {recommendations.data}")
```

## 📚 Documentation

- **[Complete Documentation](https://luli0034.github.io/rose-python-sdk/)** - Full documentation with API reference, examples, and guides
- **[GitHub Repository](https://github.com/luli0034/rose-python-sdk)** - Source code and issue tracking
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project

## 📚 Core Modules

### 1. Client (`RoseClient`)
The main client class that provides access to all Rose services:

```python
client = RoseClient(base_url="...", access_token="...")

# Access different services
client.datasets.create(...)      # Dataset management
client.pipelines.create(...)     # Pipeline management  
client.roles.create(...)         # Role management
client.recommendations.get(...)  # Get recommendations
```

### 2. Services
Organized service classes for different API endpoints:

- **`DatasetService`**: Create, manage, and query datasets
- **`PipelineService`**: Create and manage recommendation pipelines
- **`RoleService`**: Manage user roles and permissions
- **`RecommendationService`**: Get recommendations and query results

### 3. Models
Type-safe data models using Pydantic:

- **`Dataset`**: Dataset information and metadata
- **`Pipeline`**: Pipeline configuration and status
- **`Role`**: User roles and permissions
- **`Query`**: Query definitions and results

### 4. Utils
Utility functions for common operations:

- **Record Conversion**: Convert between Python and Rose data formats
- **Schema Management**: Build and validate dataset schemas
- **Batch Processing**: Handle large data uploads efficiently
- **Pipeline Building**: Create pipelines with minimal configuration

### 5. Helpers
High-level helper functions for quick operations:

- **`quick_create_dataset_with_data()`**: Create dataset and add data in one call
- **`quick_batch_upload()`**: Upload large amounts of data efficiently
- **`quick_setup_recommendation_system()`**: Complete end-to-end setup

## 📖 Examples

The SDK includes comprehensive examples in the `examples/` directory:

### Role Management
```bash
python examples/01_role_management/01_basic_permissions.py
python examples/01_role_management/02_api_usage.py
```

### Dataset Management
```bash
python examples/02_dataset_management/01_basic_datasets.py
python examples/02_dataset_management/02_api_usage.py
```

### Records Management
```bash
python examples/03_records_management/01_basic_ingestion.py
python examples/03_records_management/02_records_management.py
```

### Batch Data Management
```bash
python examples/04_batch_data_management/01_batch_append.py
python examples/04_batch_data_management/02_batch_overwrite.py
```

### Pipeline Management
```bash
python examples/05_pipeline_management/01_create_pipeline.py
python examples/05_pipeline_management/02_update_pipeline.py
python examples/05_pipeline_management/04_delete_pipeline.py
python examples/05_pipeline_management/05_list_queries.py
```

## 🔧 Advanced Usage

### Schema Validation

```python
from rose_sdk.utils import validate_and_align_records

# Validate records against dataset schema
validated_records = validate_and_align_records(
    dataset_id=dataset_id,
    records=your_records,
    client=client
)
```

### Batch Operations

```python
from rose_sdk.utils import prepare_batch_data, get_batch_headers

# Prepare large dataset for batch upload
batch_data = prepare_batch_data(records)
headers = get_batch_headers()

# Upload in batches
client.datasets.batch.upload_batch(dataset_id, batch_id, batch_data)
```

### Pipeline Building

```python
from rose_sdk.utils import PipelineBuilder

# Build complex pipeline configurations
pipeline_config = (PipelineBuilder("account", "pipeline_name", "scenario")
    .add_dataset("interaction", dataset_id)
    .add_dataset("metadata", metadata_dataset_id)
    .set_custom_property("custom_setting", "value")
    .build())
```

## 🛠️ Error Handling

The SDK provides detailed exception classes for different error scenarios:

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
    dataset = client.datasets.get("invalid_id")
except RoseNotFoundError:
    print("Dataset not found")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## 🔐 Authentication

The SDK supports multiple authentication methods:

```python
# Access token authentication
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_token"
)

# Environment variables
import os
client = RoseClient(
    base_url=os.getenv('ROSE_BASE_URL'),
    access_token=os.getenv('ROSE_ACCESS_TOKEN')
)
```

## 📋 Requirements

- Python 3.11+
- requests
- pydantic
- typing-extensions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 Links

- [API Documentation](https://luli0034.github.io/rose-python-sdk/#/api-reference/overview)
- [GitHub Repository](https://github.com/luli0034/rose-python-sdk)
- [PyPI Package](https://pypi.org/project/rose-python-sdk/)

## 🚀 CI/CD

This project uses GitHub Actions for automated testing and publishing:

- **Tests**: Automatically run on every push and pull request
- **Publishing**: Automatically publish to PyPI when version tags are pushed
- **Releases**: Automatically create GitHub releases

For setup instructions, see the [Contributing Guide](CONTRIBUTING.md).

## 📊 Status

![Tests](https://github.com/luli0034/rose-python-sdk/workflows/Test/badge.svg)
![PyPI](https://img.shields.io/pypi/v/rose-python-sdk)
![Python](https://img.shields.io/pypi/pyversions/rose-python-sdk)
![License](https://img.shields.io/pypi/l/rose-python-sdk)

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact: luli245683@gmail.com
