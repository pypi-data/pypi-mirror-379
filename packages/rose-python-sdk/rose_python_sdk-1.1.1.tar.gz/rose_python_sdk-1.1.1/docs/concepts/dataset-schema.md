# Dataset Schema

Understanding dataset schemas is crucial for working with the Rose Recommendation Service. A schema defines the structure, types, and constraints of your data.

## What is a Dataset Schema?

A dataset schema is a blueprint that describes:
- **Field names** and their data types
- **Identifier fields** that uniquely identify records
- **Required fields** that must be present in every record
- **Optional fields** that may or may not be present

## Schema Structure

A Rose dataset schema is a dictionary where each field is defined with its properties:

```python
schema = {
    "field_name": {
        "type": "str",           # Data type
        "identifier": True,      # Is this an identifier field?
        "required": True         # Is this field required?
    }
}
```

## Field Properties

### Type
Defines the data type of the field. Supported types:
- `"str"` - String
- `"int"` - Integer  
- `"float"` - Floating point number
- `"bool"` - Boolean
- `"list"` - Array of values
- `"map"` - Nested object

### Identifier
- `True` - Field is used to uniquely identify records
- `False` - Field is not an identifier (default)

### Required
- `True` - Field must be present in every record
- `False` - Field is optional (default)

## Example Schemas

### Basic User-Item Interaction Schema

```python
interaction_schema = {
    "user_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "item_id": {
        "type": "str", 
        "identifier": True,
        "required": True
    },
    "rating": {
        "type": "float",
        "required": True
    },
    "timestamp": {
        "type": "int",
        "required": False
    },
    "category": {
        "type": "str",
        "required": False
    }
}
```

### Product Catalog Schema

```python
product_schema = {
    "product_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "name": {
        "type": "str",
        "required": True
    },
    "price": {
        "type": "float",
        "required": True
    },
    "category": {
        "type": "str",
        "required": True
    },
    "in_stock": {
        "type": "bool",
        "required": False
    },
    "tags": {
        "type": "list",
        "required": False
    },
    "specifications": {
        "type": "map",
        "required": False
    }
}
```

## Automatic Schema Generation

The SDK can automatically generate schemas from sample data:

```python
from rose_sdk import build_schema_from_sample

# Sample data
sample_records = [
    {
        "user_id": "user1",
        "item_id": "item1", 
        "rating": 4.5,
        "category": "electronics",
        "timestamp": 1678886400
    },
    {
        "user_id": "user2",
        "item_id": "item1",
        "rating": 3.0,
        "category": "electronics", 
        "timestamp": 1678886500
    }
]

# Generate schema
schema = build_schema_from_sample(
    sample_records=sample_records,
    identifier_fields=["user_id", "item_id"],
    required_fields=["rating"]
)

# Result:
# {
#     "user_id": {"type": "str", "identifier": True, "required": True},
#     "item_id": {"type": "str", "identifier": True, "required": True},
#     "rating": {"type": "float", "required": True},
#     "category": {"type": "str", "required": False},
#     "timestamp": {"type": "int", "required": False}
# }
```

## Schema from Dictionary

You can also build schemas from dictionary definitions:

```python
from rose_sdk import build_schema_from_dict

# Define schema as dictionary
schema_dict = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "item_id": {"type": "str", "identifier": True, "required": True},
    "rating": {"type": "float", "required": True}
}

# Build schema
schema = build_schema_from_dict(schema_dict)
```

## Identifier Fields

Identifier fields are used to uniquely identify records. They are crucial for:
- **Data deduplication** - Preventing duplicate records
- **Record updates** - Updating specific records
- **Data integrity** - Ensuring data consistency

### Single Identifier

```python
# One field as identifier
schema = {
    "user_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "name": {
        "type": "str",
        "required": True
    }
}
```

### Composite Identifiers

```python
# Multiple fields as composite identifier
schema = {
    "user_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "item_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "rating": {
        "type": "float",
        "required": True
    }
}
# This means the combination of user_id + item_id must be unique
```

## Required vs Optional Fields

### Required Fields
Must be present in every record:

```python
schema = {
    "user_id": {
        "type": "str",
        "required": True  # Must be present
    },
    "rating": {
        "type": "float", 
        "required": True  # Must be present
    }
}
```

### Optional Fields
May or may not be present:

```python
schema = {
    "user_id": {
        "type": "str",
        "required": True
    },
    "rating": {
        "type": "float",
        "required": True
    },
    "comment": {
        "type": "str",
        "required": False  # Optional field
    },
    "timestamp": {
        "type": "int",
        "required": False  # Optional field
    }
}
```

## Complex Data Types

### List Fields

```python
schema = {
    "user_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "categories": {
        "type": "list",
        "required": False
    },
    "tags": {
        "type": "list", 
        "required": False
    }
}

# Example data:
# {
#     "user_id": {"str": "user1"},
#     "categories": {"list": ["electronics", "gadgets"]},
#     "tags": {"list": ["premium", "wireless"]}
# }
```

### Map Fields (Nested Objects)

```python
schema = {
    "user_id": {
        "type": "str",
        "identifier": True,
        "required": True
    },
    "profile": {
        "type": "map",
        "required": False
    },
    "preferences": {
        "type": "map",
        "required": False
    }
}

# Example data:
# {
#     "user_id": {"str": "user1"},
#     "profile": {
#         "map": {
#             "name": {"str": "John Doe"},
#             "age": {"int": 30}
#         }
#     },
#     "preferences": {
#         "map": {
#             "theme": {"str": "dark"},
#             "notifications": {"bool": True}
#         }
#     }
# }
```

## Schema Validation

The SDK validates data against schemas when:
- Creating datasets
- Adding records
- Updating records

### Validation Rules

1. **Required fields** must be present
2. **Data types** must match schema definition
3. **Identifier fields** must be unique
4. **Nested structures** must follow Rose format

### Example Validation

```python
# Valid record
valid_record = {
    "user_id": {"str": "user1"},
    "item_id": {"str": "item1"},
    "rating": {"float": 4.5}
}

# Invalid record - missing required field
invalid_record = {
    "user_id": {"str": "user1"},
    "item_id": {"str": "item1"}
    # Missing required "rating" field
}
```

## Best Practices

### 1. Choose Appropriate Identifiers

```python
# ✅ Good - meaningful identifiers
schema = {
    "user_id": {"type": "str", "identifier": True},
    "product_id": {"type": "str", "identifier": True}
}

# ❌ Avoid - unclear identifiers
schema = {
    "id1": {"type": "str", "identifier": True},
    "id2": {"type": "str", "identifier": True}
}
```

### 2. Use Consistent Data Types

```python
# ✅ Good - consistent types
schema = {
    "rating": {"type": "float", "required": True}
}

# ❌ Bad - mixed types for same field
# Some records: {"rating": {"float": 4.5}}
# Other records: {"rating": {"str": "good"}}
```

### 3. Mark Important Fields as Required

```python
# ✅ Good - essential fields are required
schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "item_id": {"type": "str", "identifier": True, "required": True},
    "rating": {"type": "float", "required": True},  # Essential for recommendations
    "comment": {"type": "str", "required": False}   # Nice to have
}
```

### 4. Use Descriptive Field Names

```python
# ✅ Good - descriptive names
schema = {
    "user_id": {"type": "str", "identifier": True},
    "product_id": {"type": "str", "identifier": True},
    "purchase_timestamp": {"type": "int", "required": False}
}

# ❌ Avoid - unclear names
schema = {
    "uid": {"type": "str", "identifier": True},
    "pid": {"type": "str", "identifier": True},
    "ts": {"type": "int", "required": False}
}
```

## Common Schema Patterns

### E-commerce Recommendation Schema

```python
ecommerce_schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "product_id": {"type": "str", "identifier": True, "required": True},
    "action": {"type": "str", "required": True},  # view, add_to_cart, purchase
    "rating": {"type": "float", "required": False},
    "timestamp": {"type": "int", "required": True},
    "category": {"type": "str", "required": False},
    "price": {"type": "float", "required": False}
}
```

### Content Recommendation Schema

```python
content_schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "content_id": {"type": "str", "identifier": True, "required": True},
    "interaction_type": {"type": "str", "required": True},  # read, like, share
    "duration": {"type": "int", "required": False},  # seconds
    "completion_rate": {"type": "float", "required": False},
    "content_category": {"type": "str", "required": False},
    "content_tags": {"type": "list", "required": False}
}
```

### Social Recommendation Schema

```python
social_schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "friend_id": {"type": "str", "identifier": True, "required": True},
    "relationship_type": {"type": "str", "required": True},  # friend, follower, colleague
    "interaction_count": {"type": "int", "required": False},
    "last_interaction": {"type": "int", "required": False},
    "mutual_friends": {"type": "list", "required": False}
}
```

## Schema Evolution

As your application grows, you may need to update schemas:

### Adding New Fields

```python
# Original schema
original_schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "item_id": {"type": "str", "identifier": True, "required": True},
    "rating": {"type": "float", "required": True}
}

# Updated schema with new field
updated_schema = {
    "user_id": {"type": "str", "identifier": True, "required": True},
    "item_id": {"type": "str", "identifier": True, "required": True},
    "rating": {"type": "float", "required": True},
    "timestamp": {"type": "int", "required": False}  # New field
}
```

### Changing Field Types

```python
# ❌ Avoid changing field types - can break existing data
# Original: {"rating": {"type": "float"}}
# Changed:  {"rating": {"type": "str"}}  # This will cause issues!

# ✅ Better approach - add new field
schema = {
    "rating": {"type": "float", "required": True},      # Keep original
    "rating_text": {"type": "str", "required": False}   # Add new field
}
```

Understanding dataset schemas is essential for building effective recommendation systems. A well-designed schema ensures data quality, enables proper validation, and supports the recommendation algorithms effectively.
