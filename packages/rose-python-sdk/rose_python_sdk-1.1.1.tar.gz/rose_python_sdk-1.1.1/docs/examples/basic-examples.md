# Basic Examples

This section provides comprehensive examples to get you started with the Rose Python SDK, organized by functionality.

## Quick Start

A simple example to verify your installation and basic setup.

```python
from rose_sdk import RoseClient

# Initialize the client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# List datasets
datasets = client.datasets.list()
print(f"Found {len(datasets)} datasets")

# Create a new dataset
dataset = client.datasets.create(
    name="user_interactions",
    schema={
        "user_id": {"type": "string"},
        "item_id": {"type": "string"}, 
        "rating": {"type": "float"}
    }
)
print(f"Created dataset: {dataset.dataset_id}")
```

## Dataset Management

Learn how to create, manage, and work with datasets in the Rose system.

### Creating Datasets

```python
from rose_sdk import RoseClient

client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# Create a simple dataset
dataset = client.datasets.create(
    name="product_catalog",
    schema={
        "product_id": {"type": "string"},
        "title": {"type": "string"},
        "category": {"type": "string"},
        "price": {"type": "float"}
    }
)

print(f"Created dataset: {dataset.dataset_id}")
```

### Working with Records

```python
# Add records to dataset
records = [
    {
        "product_id": "laptop-001",
        "title": "MacBook Pro 16-inch",
        "category": "electronics",
        "price": 2499.99
    },
    {
        "product_id": "phone-001", 
        "title": "iPhone 15",
        "category": "electronics",
        "price": 799.99
    }
]

# Append records
client.datasets.records.append(dataset.dataset_id, records)

# Get records
all_records = client.datasets.records.list(dataset.dataset_id)
print(f"Dataset has {len(all_records)} records")
```

### Batch Operations

```python
# Prepare batch data
batch_data = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user1", "item_id": "item2", "rating": 3.0},
    {"user_id": "user2", "item_id": "item1", "rating": 5.0}
]

# Import batch data
batch_info = client.datasets.batch.import_records(
    dataset_id=dataset.dataset_id,
    records=batch_data
)

print(f"Batch import started: {batch_info.batch_id}")
print(f"Status: {batch_info.status}")

# Check batch status
batch_status = client.datasets.batch.get_status(
    dataset_id=dataset.dataset_id,
    batch_id=batch_info.batch_id
)

print(f"Batch status: {batch_status.status}")
print(f"Processed records: {batch_status.processed_count}")
```

## Pipeline Management

Pipelines process your datasets to generate recommendations. Learn how to create and manage them.

### Creating Pipelines

```python
from rose_sdk.utils import create_pipeline

# Create a recommendation pipeline
pipeline_config = create_pipeline(
    account_id="your_account_id",
    pipeline_name="collaborative_filtering",
    scenario="realtime_leaderboard",
    dataset_mapping={
        "interaction": dataset.dataset_id,
        "metadata": metadata_dataset.dataset_id
    }
)

# Create the pipeline via API
pipeline = client.pipelines.create(
    name=pipeline_config["pipeline_name"],
    properties=pipeline_config["properties"]
)

print(f"Created pipeline: {pipeline.pipeline_id}")
```

### Monitoring Pipeline Status

```python
# Check pipeline status
pipeline = client.pipelines.get(pipeline.pipeline_id)
print(f"Pipeline status: {pipeline.status}")

# List all pipelines
pipelines = client.pipelines.list()
for p in pipelines:
    print(f"Pipeline: {p.pipeline_name} - Status: {p.status}")

# List pipeline queries
queries = client.pipelines.list_queries(pipeline.pipeline_id)
for q in queries:
    print(f"Query: {q.query_name} - Type: {q.query_type}")
```

## Recommendation System

Get personalized recommendations from your trained pipelines.

### Getting Recommendations

```python
# Get recommendations from a pipeline query
recommendations = client.recommendations.get(
    query_id="your_query_id",
    parameters={"user_id": "user1"}
)

print(f"Recommendations: {recommendations.data}")
```

### Working with Query Results

```python
# Get query details
query = client.pipelines.get_query("your_query_id")
print(f"Query: {query.query_name}")
print(f"Status: {query.status}")
```

## Role Management

Manage user roles and permissions for secure access to your Rose account.

### Creating Roles

```python
from rose_sdk.models.permission import create_data_client_role, create_admin_role

# Create a data client role
role = client.roles.create(
    name="Data Client",
    permissions=create_data_client_role()
)

print(f"Created role: {role.role_id}")
```

### Managing Permissions

```python
# List all roles
roles = client.roles.list()
for role in roles:
    print(f"Role: {role.role_name} - Permissions: {role.permissions}")

# Update role permissions
client.roles.update(
    role_id=role.role_id,
    permissions=create_admin_role()
)
```

## Account Management

Create and manage Rose accounts for your organization.

### Creating Accounts

```python
# Create a new account
account = client.accounts.create(
    account_id="my_company",
    admin_role_name="Admin"
)

print(f"Created account: {account.account_id}")
print(f"Admin token: {account.admin_token}")
```

### Working with Tokens

```python
# List accounts
accounts = client.accounts.list()
for account in accounts:
    print(f"Account: {account.account_id}")

# Get account details
account = client.accounts.get("my_company")
print(f"Account status: {account.status}")
```

## Utility Functions

Use helper functions to simplify common operations.

### Schema Building

```python
from rose_sdk.utils import build_schema_from_sample

# Build schema from sample data
sample_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0}
]

schema = build_schema_from_sample(sample_records)
print(f"Generated schema: {schema}")

# Create dataset with generated schema
dataset = client.datasets.create(
    name="auto_schema_dataset",
    schema=schema
)
```

### Record Conversion

```python
from rose_sdk.utils import convert_records_to_rose_format

# Convert records to Rose format
records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0}
]

rose_records = convert_records_to_rose_format(records)
print(f"Converted records: {rose_records}")
```

## Error Handling

Handle errors gracefully with proper exception handling.

```python
from rose_sdk.exceptions import (
    RoseAPIError,
    RoseAuthenticationError,
    RoseValidationError,
    RoseNotFoundError
)

def safe_create_dataset(name, schema):
    """Safely create a dataset with error handling"""
    try:
        dataset = client.datasets.create(name=name, schema=schema)
        return dataset
    except RoseValidationError as e:
        print(f"Validation error: {e.message}")
        return None
    except RoseAuthenticationError as e:
        print(f"Authentication failed: {e.message}")
        return None
    except RoseAPIError as e:
        print(f"API error: {e.message} (Status: {e.status_code})")
        return None

# Usage
dataset = safe_create_dataset("test_dataset", {"id": {"type": "string"}})
```

## Complete Workflow

Here's a complete example showing the full workflow from setup to getting recommendations.

### Workflow Overview

The complete recommendation system workflow follows these steps:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ROSE RECOMMENDATION WORKFLOW                 │
└─────────────────────────────────────────────────────────────────┘

1. INITIALIZATION
   ┌───────────────────┐
   │ Initialize Client │
   │ - Set base URL    │
   │ - Set access token│
   └───────────────────┘
            │
            ▼

2. DATA PREPARATION
   ┌───────────────────┐    ┌──────────────────┐
   │ Create Interaction│    │ Create Metadata  │
   │ Dataset           │    │ Dataset          │
   │ - Define schema   │    │ - Define schema  │
   │ - Set data types  │    │ - Set data types │
   └───────────────────┘    └──────────────────┘
            │                         │
            ▼                         ▼
   ┌──────────────────┐    ┌─────────────────┐
   │ Add Interaction  │    │ Add Metadata    │
   │ Records          │    │ Records         │
   │ - User behavior  │    │ - Item details  │
   │ - Ratings/views  │    │ - Categories    │
   └──────────────────┘    └─────────────────┘

3. PIPELINE CREATION
   ┌─────────────────────────────────────────┐
   │ Create Recommendation Pipeline          │
   │ - Map datasets to pipeline              │
   │ - Configure scenario (e.g., realtime)   │
   │ - Set algorithm parameters              │
   └─────────────────────────────────────────┘
            │
            ▼

4. PIPELINE TRAINING
   ┌─────────────────────────────────────────┐
   │ Monitor Pipeline Status                 │
   │ - Wait for CREATE SUCCESSFUL            │
   │ - Handle failures if any                │
   │ - Pipeline processes your data          │
   └─────────────────────────────────────────┘
            │
            ▼

5. RECOMMENDATION GENERATION
   ┌─────────────────────────────────────────┐
   │ Get Recommendations                     │
   │ - Query the trained pipeline            │
   │ - Provide user parameters               │
   │ - Receive personalized results          │
   └─────────────────────────────────────────┘

DATA FLOW:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Interaction │    │ Metadata    │    │ Pipeline    │
│ Dataset     │───▶│ Dataset     │───▶│ Processing  │
│             │    │             │    │             │
│ user_id     │    │ item_id     │    │ Algorithm   │
│ item_id     │    │ title       │    │ Training    │
│ rating      │    │ category    │    │             │
│ timestamp   │    │ price       │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
                                 │
                                 ▼
                        ┌────────────────┐
                        │ Recommendations│
                        │                │
                        │ item_id        │
                        │ score          │
                        │ metadata       │
                        └────────────────┘
```

### Complete Implementation

```python
from rose_sdk import RoseClient
from rose_sdk.utils import create_pipeline

# Initialize client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# 1. Create datasets
print("Creating datasets...")
interaction_dataset = client.datasets.create(
    name="user_interactions",
    schema={
        "user_id": {"type": "string"},
        "item_id": {"type": "string"},
        "rating": {"type": "float"}
    }
)

metadata_dataset = client.datasets.create(
    name="item_metadata", 
    schema={
        "item_id": {"type": "string"},
        "title": {"type": "string"},
        "category": {"type": "string"}
    }
)

print(f"Created interaction dataset: {interaction_dataset.dataset_id}")
print(f"Created metadata dataset: {metadata_dataset.dataset_id}")

# 2. Add sample data
print("Adding sample data...")
interaction_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user1", "item_id": "item2", "rating": 3.0},
    {"user_id": "user2", "item_id": "item1", "rating": 5.0}
]

metadata_records = [
    {"item_id": "item1", "title": "Product 1", "category": "electronics"},
    {"item_id": "item2", "title": "Product 2", "category": "clothing"}
]

client.datasets.records.append(interaction_dataset.dataset_id, interaction_records)
client.datasets.records.append(metadata_dataset.dataset_id, metadata_records)

print("Sample data added successfully")

# 3. Create pipeline
print("Creating pipeline...")
pipeline_config = create_pipeline(
    account_id="your_account_id",
    pipeline_name="recommendation_pipeline",
    scenario="realtime_leaderboard",
    dataset_mapping={
        "interaction": interaction_dataset.dataset_id,
        "metadata": metadata_dataset.dataset_id
    }
)

pipeline = client.pipelines.create(
    name=pipeline_config["pipeline_name"],
    properties=pipeline_config["properties"]
)

print(f"Pipeline created: {pipeline.pipeline_id}")

# 4. Monitor pipeline status
print("Monitoring pipeline status...")
import time

while True:
    pipeline_status = client.pipelines.get(pipeline.pipeline_id)
    print(f"Pipeline status: {pipeline_status.status}")
    
    if pipeline_status.status in ["CREATE SUCCESSFUL", "UPDATE SUCCESSFUL"]:
        print("Pipeline is ready!")
        break
    elif pipeline_status.status in ["CREATE FAILED", "UPDATE FAILED"]:
        print("Pipeline failed!")
        break
    
    time.sleep(5)

# 5. Get recommendations
print("Getting recommendations...")
# Note: You'll need to get the actual query_id from your pipeline
# This is a placeholder - replace with your actual query_id
query_id = "your_query_id"

recommendations = client.recommendations.get(
    query_id=query_id,
    parameters={"user_id": "user1"}
)

print(f"Recommendations for user1: {recommendations.data}")
```

### Workflow Steps

1. **Initialize Client**: Set up connection to Rose API
2. **Create Datasets**: Define data structure for interactions and metadata
3. **Add Sample Data**: Populate datasets with example records
4. **Create Pipeline**: Configure recommendation pipeline with dataset mapping
5. **Monitor Status**: Wait for pipeline to be ready
6. **Get Recommendations**: Query the pipeline for personalized recommendations

This complete workflow demonstrates the full cycle of setting up a recommendation system with the Rose Python SDK.
