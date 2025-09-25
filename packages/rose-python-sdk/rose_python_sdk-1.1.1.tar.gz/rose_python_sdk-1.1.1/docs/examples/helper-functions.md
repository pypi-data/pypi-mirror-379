# Helper Functions

The Rose Python SDK provides several helper functions to simplify common operations. These utilities help you work with data more efficiently without dealing with low-level details.

## Schema Management

### Building Schemas from Sample Data

```python
from rose_sdk.utils import build_schema_from_sample

# Sample interaction data
sample_records = [
    {
        "user_id": "user_001",
        "item_id": "item_001",
        "rating": 4.5,
        "timestamp": "2024-01-15T10:30:00Z",
        "category": "electronics"
    },
    {
        "user_id": "user_002", 
        "item_id": "item_002",
        "rating": 3.0,
        "timestamp": "2024-01-15T11:15:00Z",
        "category": "clothing"
    }
]

# Generate schema automatically
schema = build_schema_from_sample(sample_records)
print(f"Generated schema: {schema}")

# Use the schema to create a dataset
dataset = client.datasets.create(
    name="interactions",
    schema=schema
)
```

### Building Schemas from Dictionary

```python
from rose_sdk.utils import build_schema_from_dict

# Define schema structure
schema_dict = {
    "user_id": "string",
    "item_id": "string", 
    "rating": "float",
    "timestamp": "string",
    "metadata": {
        "category": "string",
        "price": "float"
    }
}

# Convert to Rose schema format
schema = build_schema_from_dict(schema_dict)
print(f"Schema: {schema}")
```

### Schema Validation

```python
from rose_sdk.utils import validate_and_align_records

# Sample records with different structures
records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0, "extra_field": "value"}
]

# Validate and align records to schema
validated_records = validate_and_align_records(records, schema)
print(f"Validated records: {validated_records}")
```

## Record Conversion

### Converting to Rose Format

```python
from rose_sdk.utils import convert_records_to_rose_format

# Raw records
records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0}
]

# Convert to Rose format
rose_records = convert_records_to_rose_format(records)
print(f"Rose format records: {rose_records}")
```

### Converting from Rose Format

```python
from rose_sdk.utils import convert_rose_records_to_simple

# Rose format records (from API response)
rose_records = [
    {
        "user_id": {"string": "user1"},
        "item_id": {"string": "item1"},
        "rating": {"float": 4.5}
    }
]

# Convert to simple format
simple_records = convert_rose_records_to_simple(rose_records)
print(f"Simple records: {simple_records}")
```

### Timestamp Conversion

```python
from rose_sdk.utils import convert_timestamp_to_rose_format
from datetime import datetime

# Convert datetime to Rose timestamp format
timestamp = datetime.now()
rose_timestamp = convert_timestamp_to_rose_format(timestamp)
print(f"Rose timestamp: {rose_timestamp}")

# Convert Unix timestamp
unix_timestamp = 1705123456
rose_timestamp = convert_timestamp_to_rose_format(unix_timestamp)
print(f"Rose timestamp: {rose_timestamp}")
```

## Batch Data Processing

### Preparing Batch Data

```python
from rose_sdk.utils import prepare_batch_data, get_batch_headers

# Large dataset
records = [
    {"user_id": f"user_{i}", "item_id": f"item_{i}", "rating": 4.0}
    for i in range(1000)
]

# Prepare batch data
batch_data = prepare_batch_data(records)
print(f"Batch data prepared: {len(batch_data)} records")

# Get batch headers
headers = get_batch_headers()
print(f"Batch headers: {headers}")
```

### Batch Size Estimation

```python
from rose_sdk.utils import estimate_batch_size

# Estimate batch size for records
estimated_size = estimate_batch_size(records)
print(f"Estimated batch size: {estimated_size} bytes")

# Split records into smaller batches
from rose_sdk.utils import split_batch_records

batches = split_batch_records(records, max_size=100000)  # 100KB max
print(f"Split into {len(batches)} batches")
```

## Pipeline Management

### Quick Pipeline Creation

```python
from rose_sdk.utils import create_telasa_pipeline, create_realtime_leaderboard_pipeline

# Create Telasa pipeline (if supported)
telasa_pipeline = create_telasa_pipeline(
    account_id="your_account",
    pipeline_name="telasa_recs",
    interaction_log_dataset_id="dataset_1",
    item_metadata_dataset_id="dataset_2"
)

# Create realtime leaderboard pipeline
leaderboard_pipeline = create_realtime_leaderboard_pipeline(
    account_id="your_account", 
    pipeline_name="leaderboard",
    interaction_dataset_id="dataset_1",
    metadata_dataset_id="dataset_2"
)
```

### Custom Pipeline Creation

```python
from rose_sdk.utils import create_pipeline

# Create custom pipeline
pipeline_config = create_pipeline(
    account_id="your_account",
    pipeline_name="custom_pipeline",
    scenario="realtime_leaderboard",
    dataset_mapping={
        "interaction": "interaction_dataset_id",
        "metadata": "metadata_dataset_id"
    },
    custom_property="custom_value"
)

print(f"Pipeline config: {pipeline_config}")
```

## Account Management

### Unique Account ID Generation

```python
from rose_sdk.utils import generate_unique_account_id

# Generate unique account ID
account_id = generate_unique_account_id("my_company")
print(f"Generated account ID: {account_id}")

# Generate with custom prefix
account_id = generate_unique_account_id("acme", length=12)
print(f"Custom account ID: {account_id}")
```

### Account Creation with Conflict Handling

```python
from rose_sdk.utils import create_account_with_conflict_handling

# Create account with automatic conflict resolution
account = create_account_with_conflict_handling(
    client=client,
    base_account_id="my_company",
    admin_role_name="Admin"
)

print(f"Created account: {account.account_id}")
```

### Account and Token Creation

```python
from rose_sdk.utils import create_account_and_token_with_conflict_handling

# Create account and get token
result = create_account_and_token_with_conflict_handling(
    client=client,
    base_account_id="my_company",
    admin_role_name="Admin"
)

print(f"Account: {result.account_id}")
print(f"Token: {result.admin_token}")
```

## Data Validation

### Record Format Validation

```python
from rose_sdk.utils import validate_rose_record_format

# Validate record format
record = {
    "user_id": {"string": "user1"},
    "item_id": {"string": "item1"},
    "rating": {"float": 4.5}
}

is_valid = validate_rose_record_format(record)
print(f"Record is valid: {is_valid}")

# Validate with schema
is_valid = validate_rose_record_format(record, schema)
print(f"Record matches schema: {is_valid}")
```

### Batch Record Validation

```python
from rose_sdk.utils import validate_batch_records

# Validate batch records
records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0}
]

validation_result = validate_batch_records(records, schema)
print(f"Validation result: {validation_result}")

if validation_result.is_valid:
    print("All records are valid")
else:
    print(f"Validation errors: {validation_result.errors}")
```

## Advanced Examples

### Complete Data Pipeline

```python
from rose_sdk.utils import (
    build_schema_from_sample,
    convert_records_to_rose_format,
    prepare_batch_data,
    create_pipeline
)

# 1. Build schema from sample data
sample_data = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5, "timestamp": "2024-01-15T10:30:00Z"},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0, "timestamp": "2024-01-15T11:15:00Z"}
]

schema = build_schema_from_sample(sample_data)
print(f"Generated schema: {schema}")

# 2. Create dataset
dataset = client.datasets.create(name="interactions", schema=schema)

# 3. Prepare large batch of data
large_dataset = [
    {"user_id": f"user_{i}", "item_id": f"item_{i}", "rating": 4.0, "timestamp": "2024-01-15T10:30:00Z"}
    for i in range(10000)
]

# Convert to Rose format
rose_records = convert_records_to_rose_format(large_dataset)

# Prepare for batch import
batch_data = prepare_batch_data(rose_records)

# 4. Import data
batch_info = client.datasets.batch.import_records(
    dataset_id=dataset.dataset_id,
    records=batch_data
)

print(f"Batch import started: {batch_info.batch_id}")

# 5. Create pipeline
pipeline_config = create_pipeline(
    account_id="your_account",
    pipeline_name="recommendation_pipeline",
    scenario="realtime_leaderboard",
    dataset_mapping={
        "interaction": dataset.dataset_id,
        "metadata": "metadata_dataset_id"
    }
)

pipeline = client.pipelines.create(
    name=pipeline_config["pipeline_name"],
    properties=pipeline_config["properties"]
)

print(f"Pipeline created: {pipeline.pipeline_id}")
```

### Error Handling with Utilities

```python
from rose_sdk.utils import validate_rose_record_format
from rose_sdk.exceptions import RoseValidationError

def safe_process_records(records, schema):
    """Safely process records with validation"""
    processed_records = []
    
    for i, record in enumerate(records):
        try:
            # Validate record format
            if not validate_rose_record_format(record, schema):
                print(f"Record {i} failed validation, skipping...")
                continue
                
            # Process record
            processed_records.append(record)
            
        except Exception as e:
            print(f"Error processing record {i}: {e}")
            continue
    
    return processed_records

# Usage
records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item2", "rating": "invalid"},  # Invalid rating
    {"user_id": "user3", "item_id": "item3", "rating": 3.0}
]

schema = {
    "user_id": {"type": "string"},
    "item_id": {"type": "string"},
    "rating": {"type": "float"}
}

processed = safe_process_records(records, schema)
print(f"Processed {len(processed)} valid records")
```

These helper functions make it easier to work with the Rose Python SDK by handling common tasks like schema generation, data conversion, and validation automatically.
