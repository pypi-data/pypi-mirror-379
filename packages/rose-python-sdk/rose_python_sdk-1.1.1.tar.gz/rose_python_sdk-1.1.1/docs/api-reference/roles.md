# Roles API

The Roles API provides methods to manage user roles and permissions within your Rose account.

## Create Role

Create a new role with optional permissions.

### Method Signature

```python
client.roles.create(
    role_name: str,
    permission: Optional[str] = None,
    with_token: Optional[bool] = False,
    token_expiration: Optional[int] = None
) -> Role
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_name` | `str` | Yes | The name of the role |
| `permission` | `str` | No | The permission in hex string |
| `with_token` | `bool` | No | Whether to issue a token for the role (default: False) |
| `token_expiration` | `int` | No | The expiration time of the access token in seconds |

### Examples

#### Basic Role Creation

```python
# Create a basic role
role = client.roles.create(
    role_name="data_scientist",
    permission="0x1F"  # Example permission hex
)

print(f"Created role: {role.role_name} (ID: {role.role_id})")
```

#### Create Role with Token

```python
# Create role and immediately get a token
role_with_token = client.roles.create(
    role_name="api_user",
    permission="0x0F",
    with_token=True,
    token_expiration=3600  # 1 hour
)

print(f"Role: {role_with_token.role_name}")
print(f"Token: {role_with_token.token}")
```

### Response

```python
Role(
    account_id="account_123",
    role_name="data_scientist",
    role_id="role_12345",
    permission="0x1F",
    expired_at=None
)
```

## List Roles

Get a list of all roles in your account.

### Method Signature

```python
client.roles.list() -> List[Role]
```

### Examples

```python
# Get all roles
roles = client.roles.list()

for role in roles:
    print(f"Role: {role.role_name} (ID: {role.role_id})")
    print(f"Permission: {role.permission}")
    print(f"Expired at: {role.expired_at}")
```

### Response

```python
[
    Role(
        account_id="account_123",
        role_name="admin",
        role_id="role_12345",
        permission="0xFF",
        expired_at=None
    ),
    Role(
        account_id="account_123",
        role_name="data_scientist",
        role_id="role_67890",
        permission="0x1F",
        expired_at=1678886400
    )
]
```

## Get Role

Retrieve a specific role by ID.

### Method Signature

```python
client.roles.get(role_id: str) -> Role
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_id` | `str` | Yes | The role ID |

### Examples

```python
# Get a specific role
role = client.roles.get("role_12345")

print(f"Role: {role.role_name}")
print(f"Permission: {role.permission}")
print(f"Account: {role.account_id}")
```

## Update Role

Update a role's permissions.

### Method Signature

```python
client.roles.update(
    role_id: str,
    permission: str
) -> Role
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_id` | `str` | Yes | The role ID |
| `permission` | `str` | Yes | The new permission in hex string |

### Examples

```python
# Update role permissions
updated_role = client.roles.update(
    role_id="role_12345",
    permission="0x3F"  # New permission level
)

print(f"Updated role: {updated_role.role_name}")
print(f"New permission: {updated_role.permission}")
```

## Delete Role

Delete a role and revoke all its tokens.

### Method Signature

```python
client.roles.delete(role_id: str) -> None
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_id` | `str` | Yes | The role ID to delete |

### Examples

```python
# Delete a role
client.roles.delete("role_12345")
print("Role deleted successfully")
```

## Issue Token

Issue a new access token for a role.

### Method Signature

```python
client.roles.issue_token(
    role_id: str,
    expired_at: Optional[int] = None,
    expiration: Optional[int] = None,
    tenant_id: Optional[str] = None
) -> RoleWithToken
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_id` | `str` | Yes | The role ID |
| `expired_at` | `int` | No | The expiration time as Unix timestamp |
| `expiration` | `int` | No | The expiration time in seconds from now |
| `tenant_id` | `str` | No | The tenant ID for the X-KK-Tenant-Id header |

### Examples

#### Issue Token with Expiration Duration

```python
# Issue token that expires in 1 hour
role_with_token = client.roles.issue_token(
    role_id="role_12345",
    expiration=3600  # 1 hour from now
)

print(f"Token: {role_with_token.token}")
print(f"Expires at: {role_with_token.expired_at}")
```

#### Issue Token with Specific Expiration Time

```python
import time

# Issue token that expires at specific time
expiration_time = int(time.time()) + 7200  # 2 hours from now
role_with_token = client.roles.issue_token(
    role_id="role_12345",
    expired_at=expiration_time
)

print(f"Token: {role_with_token.token}")
```

#### Issue Token with Tenant ID

```python
# Issue token with tenant ID
role_with_token = client.roles.issue_token(
    role_id="role_12345",
    expiration=3600,
    tenant_id="tenant_123"
)

print(f"Token: {role_with_token.token}")
```

### Response

```python
RoleWithToken(
    account_id="account_123",
    role_name="data_scientist",
    role_id="role_12345",
    permission="0x1F",
    expired_at=1678886400,
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
)
```

## Revoke Token

Revoke the access token for a role.

### Method Signature

```python
client.roles.revoke_token(role_id: str) -> None
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role_id` | `str` | Yes | The role ID |

### Examples

```python
# Revoke token for a role
client.roles.revoke_token("role_12345")
print("Token revoked successfully")
```

## Permission Management

### Common Permission Values

```python
# Example permission hex values
PERMISSIONS = {
    "read_only": "0x01",      # Read access only
    "read_write": "0x03",     # Read and write access
    "admin": "0xFF",          # Full admin access
    "data_scientist": "0x1F", # Data science operations
    "api_user": "0x0F"        # API access
}
```

### Using Permissions

```python
# Create role with specific permissions
role = client.roles.create(
    role_name="read_only_user",
    permission=PERMISSIONS["read_only"]
)

# Update role permissions
updated_role = client.roles.update(
    role_id=role.role_id,
    permission=PERMISSIONS["read_write"]
)
```

## Error Handling

```python
from rose_sdk import (
    RoseAPIError,
    RoseNotFoundError,
    RoseValidationError,
    RosePermissionError
)

try:
    role = client.roles.get("role_12345")
except RoseNotFoundError:
    print("Role not found")
except RoseValidationError as e:
    print(f"Validation error: {e}")
except RosePermissionError as e:
    print(f"Permission error: {e}")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Best Practices

1. **Principle of Least Privilege**: Give roles only the minimum permissions needed
2. **Token Expiration**: Set appropriate token expiration times for security
3. **Regular Rotation**: Regularly rotate tokens for sensitive roles
4. **Monitor Usage**: Track role usage and permissions
5. **Clean Up**: Remove unused roles and revoke unnecessary tokens

## Examples

### Complete Role Management Workflow

```python
# Create different types of roles
roles_to_create = [
    {
        "name": "admin",
        "permission": "0xFF",
        "with_token": True,
        "expiration": 86400  # 24 hours
    },
    {
        "name": "data_scientist",
        "permission": "0x1F",
        "with_token": True,
        "expiration": 3600  # 1 hour
    },
    {
        "name": "read_only",
        "permission": "0x01",
        "with_token": False
    }
]

created_roles = []
for role_config in roles_to_create:
    role = client.roles.create(**role_config)
    created_roles.append(role)
    print(f"Created role: {role.role_name}")

# List all roles
all_roles = client.roles.list()
print(f"Total roles: {len(all_roles)}")

# Update a role's permissions
if created_roles:
    role_to_update = created_roles[0]
    updated_role = client.roles.update(
        role_id=role_to_update.role_id,
        permission="0x3F"  # Increased permissions
    )
    print(f"Updated role: {updated_role.role_name}")

# Issue new token for a role
role_with_token = client.roles.issue_token(
    role_id=created_roles[0].role_id,
    expiration=7200  # 2 hours
)
print(f"Issued new token for: {role_with_token.role_name}")

# Clean up - delete test roles
for role in created_roles:
    if "test" in role.role_name.lower():
        client.roles.delete(role.role_id)
        print(f"Deleted test role: {role.role_name}")
```

### Token Management

```python
# Issue multiple tokens for different purposes
tokens = {}

# Long-term token for admin operations
admin_token = client.roles.issue_token(
    role_id="admin_role_id",
    expiration=86400  # 24 hours
)
tokens["admin"] = admin_token.token

# Short-term token for API operations
api_token = client.roles.issue_token(
    role_id="api_role_id",
    expiration=3600  # 1 hour
)
tokens["api"] = api_token.token

# Use tokens with different clients
admin_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token=tokens["admin"]
)

api_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token=tokens["api"]
)

# Revoke tokens when done
client.roles.revoke_token("admin_role_id")
client.roles.revoke_token("api_role_id")
print("All tokens revoked")
```
