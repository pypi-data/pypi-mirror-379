# Understanding Rose Format

The Rose Recommendation Service uses a specific data format for storing and processing records. Understanding this format is crucial for working effectively with the Rose Python SDK.

## What is Rose Format?

Rose format is a structured way of representing data that includes type information for each field. Unlike simple dictionaries, Rose format explicitly defines the data type of each value, which allows the system to process and validate data more effectively.

## Basic Structure

In Rose format, each field is represented as a dictionary where the key is the data type and the value is the actual data:

```python
# Simple dictionary format (what you might be used to)
simple_record = {
    "user_id": "user123",
    "item_id": "item456", 
    "rating": 4.5,
    "is_active": True
}

# Rose format (what the system expects)
rose_record = {
    "user_id": {"str": "user123"},
    "item_id": {"str": "item456"},
    "rating": {"float": 4.5},
    "is_active": {"bool": True}
}
```

## Supported Data Types

The Rose format supports the following data types:

| Type | Rose Format | Example |
|------|-------------|---------|
| String | `{"str": "value"}` | `{"name": {"str": "John"}}` |
| Integer | `{"int": 123}` | `{"age": {"int": 25}}` |
| Float | `{"float": 4.5}` | `{"rating": {"float": 4.5}}` |
| Boolean | `{"bool": true}` | `{"active": {"bool": true}}` |
| List | `{"list": [...]}` | `{"tags": {"list": ["tag1", "tag2"]}}` |
| Map/Object | `{"map": {...}}` | `{"metadata": {"map": {"key": "value"}}}` |

## Conversion Utilities

The Rose Python SDK provides utilities to convert between simple dictionaries and Rose format:

### Convert Simple to Rose Format

```python
from rose_sdk import convert_records_to_rose_format

# Simple records
simple_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5},
    {"user_id": "user2", "item_id": "item1", "rating": 3.0}
]

# Convert to Rose format
rose_records = convert_records_to_rose_format(simple_records)

# Result:
# [
#     {
#         "user_id": {"str": "user1"},
#         "item_id": {"str": "item1"}, 
#         "rating": {"float": 4.5}
#     },
#     {
#         "user_id": {"str": "user2"},
#         "item_id": {"str": "item1"},
#         "rating": {"float": 3.0}
#     }
# ]
```

### Convert Rose to Simple Format

```python
from rose_sdk import convert_rose_records_to_simple

# Rose format records
rose_records = [
    {
        "user_id": {"str": "user1"},
        "item_id": {"str": "item1"},
        "rating": {"float": 4.5}
    }
]

# Convert to simple format
simple_records = convert_rose_records_to_simple(rose_records)

# Result:
# [
#     {"user_id": "user1", "item_id": "item1", "rating": 4.5}
# ]
```

## Complex Data Types

### Lists

```python
# Simple format
simple_record = {
    "user_id": "user1",
    "categories": ["electronics", "gadgets", "tech"]
}

# Rose format
rose_record = {
    "user_id": {"str": "user1"},
    "categories": {"list": ["electronics", "gadgets", "tech"]}
}
```

### Nested Objects (Maps)

```python
# Simple format
simple_record = {
    "user_id": "user1",
    "profile": {
        "name": "John Doe",
        "age": 30,
        "preferences": {
            "theme": "dark",
            "notifications": True
        }
    }
}

# Rose format
rose_record = {
    "user_id": {"str": "user1"},
    "profile": {
        "map": {
            "name": {"str": "John Doe"},
            "age": {"int": 30},
            "preferences": {
                "map": {
                    "theme": {"str": "dark"},
                    "notifications": {"bool": True}
                }
            }
        }
    }
}
```

## Schema Inference

The SDK can automatically infer the Rose format schema from sample data:

```python
from rose_sdk import build_schema_from_sample

# Sample records
sample_records = [
    {"user_id": "user1", "item_id": "item1", "rating": 4.5, "category": "electronics"},
    {"user_id": "user2", "item_id": "item2", "rating": 3.0, "category": "books"}
]

# Build schema
schema = build_schema_from_sample(
    sample_records=sample_records,
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)

# Result:
# {
#     "user_id": {"type": "str", "identifier": True},
#     "item_id": {"type": "str", "identifier": True},
#     "rating": {"type": "float", "required": True},
#     "category": {"type": "str", "required": False}
# }
```

## Why Use Rose Format?

1. **Type Safety**: Explicit type information prevents data type errors
2. **Validation**: The system can validate data before processing
3. **Consistency**: Ensures all data follows the same structure
4. **Performance**: Optimized for the recommendation engine
5. **Flexibility**: Supports complex nested data structures

## Best Practices

1. **Use Conversion Utilities**: Always use the provided conversion functions
2. **Validate Data**: Check data types before conversion
3. **Handle Errors**: Always handle conversion errors gracefully
4. **Consistent Types**: Ensure the same field always has the same type
5. **Test with Sample Data**: Test conversions with your actual data

## Common Pitfalls

### Mixed Data Types

```python
# ❌ Wrong - mixed types for same field
bad_records = [
    {"rating": 4.5},      # float
    {"rating": "good"}    # string - inconsistent!
]

# ✅ Correct - consistent types
good_records = [
    {"rating": 4.5},      # float
    {"rating": 3.0}       # float - consistent!
]
```

### Missing Type Information

```python
# ❌ Wrong - missing type info
bad_rose_record = {
    "user_id": "user123"  # Should be {"str": "user123"}
}

# ✅ Correct - proper Rose format
good_rose_record = {
    "user_id": {"str": "user123"}
}
```

### Nested Structure Issues

```python
# ❌ Wrong - inconsistent nesting
bad_nested = {
    "profile": {
        "name": "John",           # Should be {"str": "John"}
        "age": 30                 # Should be {"int": 30}
    }
}

# ✅ Correct - proper nesting
good_nested = {
    "profile": {
        "map": {
            "name": {"str": "John"},
            "age": {"int": 30}
        }
    }
}
```

## Examples

### E-commerce Product Data

```python
# Simple format
product = {
    "product_id": "prod_123",
    "name": "Wireless Headphones",
    "price": 99.99,
    "in_stock": True,
    "categories": ["electronics", "audio"],
    "specifications": {
        "battery_life": "20 hours",
        "wireless": True,
        "color": "black"
    }
}

# Rose format
rose_product = {
    "product_id": {"str": "prod_123"},
    "name": {"str": "Wireless Headphones"},
    "price": {"float": 99.99},
    "in_stock": {"bool": True},
    "categories": {"list": ["electronics", "audio"]},
    "specifications": {
        "map": {
            "battery_life": {"str": "20 hours"},
            "wireless": {"bool": True},
            "color": {"str": "black"}
        }
    }
}
```

### User Interaction Data

```python
# Simple format
interaction = {
    "user_id": "user_456",
    "item_id": "prod_123",
    "action": "purchase",
    "timestamp": 1678886400,
    "metadata": {
        "quantity": 1,
        "discount_applied": 0.1,
        "payment_method": "credit_card"
    }
}

# Rose format
rose_interaction = {
    "user_id": {"str": "user_456"},
    "item_id": {"str": "prod_123"},
    "action": {"str": "purchase"},
    "timestamp": {"int": 1678886400},
    "metadata": {
        "map": {
            "quantity": {"int": 1},
            "discount_applied": {"float": 0.1},
            "payment_method": {"str": "credit_card"}
        }
    }
}
```

Understanding Rose format is essential for working with the Rose Recommendation Service. The SDK's conversion utilities make it easy to work with familiar dictionary formats while ensuring compatibility with the system's requirements.
