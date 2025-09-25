# Datasets API

The Datasets API provides methods to manage your datasets, including creating, updating, deleting, and retrieving datasets and their records.

## Create Dataset

Create a new dataset with a specified schema.

### Method Signature

```python
client.datasets.create(
    name: str,
    schema: Dict[str, Any],
    enable_housekeeping: Optional[bool] = True
) -> CreateDatasetResponse
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `str` | Yes | The dataset name |
| `schema` | `Dict[str, Any]` | Yes | The dataset schema |
| `enable_housekeeping` | `bool` | No | Whether to enable housekeeping (default: True) |

### Examples

#### Basic Dataset Creation

```python
# Create a simple dataset
dataset_response = client.datasets.create(
    name="user_interactions",
    schema={
        "user_id": {"type": "str", "identifier": True},
        "item_id": {"type": "str", "identifier": True},
        "rating": {"type": "float", "required": True}
    }
)

print(f"Created dataset: {dataset_response.dataset_id}")
```

#### Using Schema Builder

```python
from rose_sdk import build_schema_from_sample

# Build schema from sample data
sample_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user1", "item_id": "item2", "rating": 3.0}
]

schema = build_schema_from_sample(
    sample_records=sample_records,
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)

dataset_response = client.datasets.create(
    name="user_interactions",
    schema=schema
)
```

### Response

```python
CreateDatasetResponse(
    dataset_id="dataset_12345"
)

# Expected output:
# Created dataset: dataset_12345
```

## List Datasets

Get a list of all datasets in your account.

### Method Signature

```python
client.datasets.list() -> List[Dataset]
```

### Examples

```python
# Get all datasets
datasets = client.datasets.list()

for dataset in datasets:
    print(f"Dataset: {dataset.dataset_name} (ID: {dataset.dataset_id})")
    print(f"Status: {dataset.status}")
    print(f"Created: {dataset.created_at}")
```

### Response

```python
[
    Dataset(
        account_id="account_123",
        dataset_name="user_interactions",
        dataset_id="dataset_12345",
        schema={...},
        status="active",
        created_at="2024-01-15T10:30:00Z",
        updated_at="2024-01-15T10:30:00Z"
    )
]

# Expected output:
# Dataset: user_interactions (ID: dataset_12345)
# Status: active
# Created: 2024-01-15T10:30:00Z
```

## Get Dataset

Retrieve a specific dataset by ID.

### Method Signature

```python
client.datasets.get(dataset_id: str) -> Dataset
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dataset_id` | `str` | Yes | The dataset ID |

### Examples

```python
# Get a specific dataset
dataset = client.datasets.get("dataset_12345")

print(f"Dataset: {dataset.dataset_name}")
print(f"Schema: {dataset.schema}")
print(f"Status: {dataset.status}")
```

## Update Dataset

Update an existing dataset.

### Method Signature

```python
client.datasets.update(
    dataset_id: str,
    name: Optional[str] = None,
    enable_housekeeping: Optional[bool] = None
) -> Dataset
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dataset_id` | `str` | Yes | The dataset ID |
| `name` | `str` | No | New dataset name |
| `enable_housekeeping` | `bool` | No | Enable/disable housekeeping |

### Examples

```python
# Update dataset name
updated_dataset = client.datasets.update(
    dataset_id="dataset_12345",
    name="updated_user_interactions"
)

# Disable housekeeping
updated_dataset = client.datasets.update(
    dataset_id="dataset_12345",
    enable_housekeeping=False
)
```

## Delete Dataset

Delete a dataset and all its data.

### Method Signature

```python
client.datasets.delete(dataset_id: str) -> None
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dataset_id` | `str` | Yes | The dataset ID to delete |

### Examples

```python
# Delete a dataset
client.datasets.delete("dataset_12345")
print("Dataset deleted successfully")
```

## Dataset Records

### Add Records

Add records to a dataset.

#### Method Signature

```python
client.datasets.records.create(
    dataset_id: str,
    records: List[Record]
) -> None
```

#### Examples

```python
from rose_sdk import convert_records_to_rose_format

# Simple records
simple_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user1", "item_id": "item2", "rating": 3.0}
]

# Convert to Rose format
rose_records = convert_records_to_rose_format(simple_records)

# Add records
client.datasets.records.create("dataset_12345", rose_records)
```

### List Records

Get records from a dataset.

#### Method Signature

```python
client.datasets.records.list(
    dataset_id: str,
    size: Optional[int] = None
) -> List[Record]
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dataset_id` | `str` | Yes | The dataset ID |
| `size` | `int` | No | Number of records to retrieve |

#### Examples

```python
# Get all records
records = client.datasets.records.list("dataset_12345")

# Get limited number of records
records = client.datasets.records.list("dataset_12345", size=100)

# Convert to simple format
from rose_sdk import convert_rose_records_to_simple
simple_records = convert_rose_records_to_simple(records)
```

### Delete Records

Delete records from a dataset.

#### Method Signature

```python
client.datasets.records.delete(
    dataset_id: str,
    records: List[Record]
) -> None
```

#### Examples

```python
# Delete specific records
records_to_delete = convert_records_to_rose_format([
    {"user_id": "user1", "item_id": "item1"}
])

client.datasets.records.delete("dataset_12345", records_to_delete)
```

## Batch Operations

### Start Batch Upload

Start a batch upload operation.

#### Method Signature

```python
client.datasets.batch.start_upload(dataset_id: str) -> str
```

#### Examples

```python
# Start batch upload
batch_id = client.datasets.batch.start_upload("dataset_12345")
print(f"Started batch upload: {batch_id}")
```

### Upload Batch

Upload records in a batch.

#### Method Signature

```python
client.datasets.batch.upload_batch(
    dataset_id: str,
    batch_id: str,
    records: List[Record]
) -> None
```

#### Examples

```python
# Upload batch of records
records = convert_records_to_rose_format([
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item1", "rating": 5.0}
])

client.datasets.batch.upload_batch("dataset_12345", batch_id, records)
```

### Complete Upload

Complete a batch upload operation.

#### Method Signature

```python
client.datasets.batch.complete_upload(
    dataset_id: str,
    batch_id: str
) -> None
```

#### Examples

```python
# Complete batch upload
client.datasets.batch.complete_upload("dataset_12345", batch_id)
print("Batch upload completed")
```

### Upload Append

Append records to a dataset.

#### Method Signature

```python
client.datasets.batch.upload_append(
    dataset_id: str,
    records: List[Record]
) -> None
```

#### Examples

```python
# Append records
records = convert_records_to_rose_format([
    {"user_id": "user3", "item_id": "item1", "rating": 4.0}
])

client.datasets.batch.upload_append("dataset_12345", records)
```

## Helper Functions

### Quick Dataset Creation

```python
from rose_sdk import quick_create_dataset

# Create dataset from sample records
dataset_id = quick_create_dataset(
    client=client,
    name="user_interactions",
    sample_records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5}
    ],
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)
```

### Quick Dataset with Data

```python
from rose_sdk import quick_create_dataset_with_data

# Create dataset and add data
dataset_id = quick_create_dataset_with_data(
    client=client,
    name="user_interactions",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5},
        {"user_id": "user1", "item_id": "item2", "rating": 3.0}
    ],
    identifier_fields=["user_id", "item_id"]
)
```

### Quick Batch Upload

```python
from rose_sdk import quick_batch_upload

# Batch upload with overwrite mode
batch_id = quick_batch_upload(
    client=client,
    dataset_id="dataset_12345",
    records=[
        {"user_id": "user1", "item_id": "item1", "rating": 4.5}
    ],
    mode="overwrite"
)

# Batch upload with append mode
quick_batch_upload(
    client=client,
    dataset_id="dataset_12345",
    records=[
        {"user_id": "user2", "item_id": "item1", "rating": 5.0}
    ],
    mode="append"
)
```

## Error Handling

```python
from rose_sdk import (
    RoseAPIError,
    RoseNotFoundError,
    RoseValidationError,
    RoseConflictError
)

try:
    dataset = client.datasets.get("nonexistent_dataset")
except RoseNotFoundError:
    print("Dataset not found")
except RoseValidationError as e:
    print(f"Validation error: {e}")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Best Practices

1. **Use Schema Builder**: Use `build_schema_from_sample` for automatic schema generation
2. **Batch Operations**: Use batch operations for large datasets
3. **Identifier Fields**: Always specify identifier fields for proper data management
4. **Error Handling**: Always handle API errors gracefully
5. **Data Validation**: Validate data before uploading

## Examples

### Complete Dataset Workflow

```python
from rose_sdk import (
    RoseClient,
    quick_create_dataset_with_data,
    quick_batch_upload
)

# Initialize client
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token"
)

# Create dataset with initial data
dataset_id = quick_create_dataset_with_data(
    client=client,
    name="movie_ratings",
    records=[
        {"user_id": "user1", "movie_id": "movie1", "rating": 4.5, "genre": "action"},
        {"user_id": "user1", "movie_id": "movie2", "rating": 3.0, "genre": "comedy"},
        {"user_id": "user2", "movie_id": "movie1", "rating": 5.0, "genre": "action"}
    ],
    identifier_fields=["user_id", "movie_id"],
    required_fields=["rating"]
)

# Add more data using batch upload
new_ratings = [
    {"user_id": "user2", "movie_id": "movie2", "rating": 4.0, "genre": "comedy"},
    {"user_id": "user3", "movie_id": "movie1", "rating": 4.5, "genre": "action"}
]

quick_batch_upload(
    client=client,
    dataset_id=dataset_id,
    records=new_ratings,
    mode="append"
)

# Get dataset summary
from rose_sdk import get_dataset_summary
summary = get_dataset_summary(client, dataset_id)
print(f"Dataset has {summary['sample_count']} records")
```
