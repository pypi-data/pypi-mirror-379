# Authentication & Roles

Understanding authentication and role-based access control is essential for securely using the Rose Recommendation Service.

## Authentication Overview

The Rose Recommendation Service uses **Bearer Token** authentication. You need a valid access token to make API requests.

## Getting Access Tokens

### 1. Create Account and Get Token

The easiest way to get started is to create a new account:

```python
# Create account with immediate token
account_with_token = client.accounts.create_with_token(
    account_id="my_new_account",
    expiration=3600  # 1 hour
)

print(f"Account: {account_with_token.account_id}")
print(f"Token: {account_with_token.token}")
# Expected output:
# Account: my_new_account
# Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### 2. Create Role and Issue Token

For more control, create a role and issue a token:

```python
# Create a role
role = client.roles.create(
    role_name="data_scientist",
    permission="0x1F"  # Example permission
)

# Issue token for the role
role_with_token = client.roles.issue_token(
    role_id=role.role_id,
    expiration=7200  # 2 hours
)

print(f"Role: {role_with_token.role_name}")
print(f"Token: {role_with_token.token}")
# Expected output:
# Role: data_scientist
# Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Using Access Tokens

### Initialize Client with Token

```python
from rose_sdk import RoseClient

# Initialize client with access token
client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="your_access_token_here"
)

# Test the connection
try:
    datasets = client.datasets.list()
    print(f"✅ Connected! Found {len(datasets)} datasets")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

### Update Token After Initialization

```python
# Set or update access token
client.set_access_token("new_access_token")

# Verify new token works
datasets = client.datasets.list()
print("✅ Token updated successfully")
```

## Role-Based Access Control

### Understanding Roles

Roles define what actions a user can perform:

```python
# List all roles in your account
roles = client.roles.list()

for role in roles:
    print(f"Role: {role.role_name}")
    print(f"ID: {role.role_id}")
    print(f"Permission: {role.permission}")
    print(f"Expired: {role.expired_at}")
    print("---")

# Expected output:
# Role: admin
# ID: role_12345
# Permission: 0xFF
# Expired: None
# ---
# Role: data_scientist
# ID: role_67890
# Permission: 0x1F
# Expired: 1678886400
# ---
```

### Permission Levels

Permissions are represented as hexadecimal values:

| Permission | Hex Value | Description |
|------------|-----------|-------------|
| Read Only | `0x01` | Can read data only |
| Read/Write | `0x03` | Can read and write data |
| Data Science | `0x1F` | Can manage datasets and pipelines |
| API Access | `0x0F` | Can make API calls |
| Admin | `0xFF` | Full access to everything |

### Create Different Role Types

```python
# Create read-only role
readonly_role = client.roles.create(
    role_name="readonly_user",
    permission="0x01"
)

# Create data scientist role
data_scientist_role = client.roles.create(
    role_name="data_scientist",
    permission="0x1F"
)

# Create admin role
admin_role = client.roles.create(
    role_name="admin",
    permission="0xFF"
)

print("✅ Created roles with different permissions")
```

## Token Management

### Token Expiration

Tokens have expiration times for security:

```python
# Issue token with specific expiration
role_with_token = client.roles.issue_token(
    role_id="role_12345",
    expiration=3600  # 1 hour from now
)

print(f"Token expires at: {role_with_token.expired_at}")
# Expected output: Token expires at: 1678886400
```

### Check Token Expiration

```python
import time

def is_token_expired(expired_at):
    """Check if token is expired."""
    if expired_at is None:
        return False  # Never expires
    
    current_time = int(time.time())
    return current_time >= expired_at

# Check token
if is_token_expired(role_with_token.expired_at):
    print("❌ Token is expired")
else:
    print("✅ Token is still valid")
```

### Refresh Expired Tokens

```python
# Issue new token when old one expires
if is_token_expired(role_with_token.expired_at):
    new_token = client.roles.issue_token(
        role_id="role_12345",
        expiration=3600
    )
    client.set_access_token(new_token.token)
    print("✅ Token refreshed")
```

## Security Best Practices

### 1. Use Appropriate Token Expiration

```python
# Short expiration for sensitive operations
sensitive_token = client.roles.issue_token(
    role_id="admin_role",
    expiration=1800  # 30 minutes
)

# Longer expiration for regular operations
regular_token = client.roles.issue_token(
    role_id="data_scientist_role",
    expiration=86400  # 24 hours
)
```

### 2. Rotate Tokens Regularly

```python
def rotate_token_safely(role_id, current_token):
    """Safely rotate a token."""
    try:
        # Issue new token
        new_token = client.roles.issue_token(
            role_id=role_id,
            expiration=3600
        )
        
        # Update client
        client.set_access_token(new_token.token)
        
        # Revoke old token (if possible)
        # Note: This depends on your implementation
        
        print("✅ Token rotated successfully")
        return new_token.token
        
    except Exception as e:
        print(f"❌ Token rotation failed: {e}")
        return current_token
```

### 3. Use Least Privilege Principle

```python
# Create role with minimal required permissions
minimal_role = client.roles.create(
    role_name="readonly_analyst",
    permission="0x01"  # Read-only access
)

# Only give admin permissions when absolutely necessary
admin_role = client.roles.create(
    role_name="system_admin",
    permission="0xFF"  # Full access
)
```

### 4. Monitor Token Usage

```python
def monitor_token_usage(role_id):
    """Monitor token usage and expiration."""
    role = client.roles.get(role_id)
    
    if role.expired_at:
        time_until_expiry = role.expired_at - int(time.time())
        print(f"Token expires in {time_until_expiry} seconds")
        
        if time_until_expiry < 300:  # Less than 5 minutes
            print("⚠️  Token expires soon - consider refreshing")
    else:
        print("Token never expires")
```

## Error Handling

### Authentication Errors

```python
from rose_sdk import RoseAuthenticationError

try:
    datasets = client.datasets.list()
except RoseAuthenticationError as e:
    print(f"❌ Authentication failed: {e}")
    print("Please check your access token")
except Exception as e:
    print(f"❌ Other error: {e}")
```

### Token Expiration Handling

```python
def handle_token_expiration(func, *args, **kwargs):
    """Handle token expiration automatically."""
    try:
        return func(*args, **kwargs)
    except RoseAuthenticationError:
        print("🔄 Token expired, refreshing...")
        
        # Refresh token logic here
        new_token = refresh_token()
        client.set_access_token(new_token)
        
        # Retry the operation
        return func(*args, **kwargs)
```

## Multi-Environment Setup

### Development Environment

```python
# Development account
dev_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="dev_token_here"
)

# Test with development data
dev_datasets = dev_client.datasets.list()
print(f"Development datasets: {len(dev_datasets)}")
```

### Production Environment

```python
# Production account
prod_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token="prod_token_here"
)

# Use production data
prod_datasets = prod_client.datasets.list()
print(f"Production datasets: {len(prod_datasets)}")
```

### Environment-Specific Roles

```python
# Create environment-specific roles
environments = ["dev", "staging", "prod"]

for env in environments:
    role = client.roles.create(
        role_name=f"{env}_data_scientist",
        permission="0x1F"
    )
    
    token = client.roles.issue_token(
        role_id=role.role_id,
        expiration=86400  # 24 hours
    )
    
    print(f"✅ Created {env} role with token")
```

## Complete Authentication Workflow

```python
def setup_authentication(account_id, role_name, permission="0x1F"):
    """Complete authentication setup workflow."""
    
    try:
        # 1. Create account
        account = client.accounts.create(account_id)
        print(f"✅ Created account: {account.account_id}")
        
        # 2. Create role
        role = client.roles.create(
            role_name=role_name,
            permission=permission
        )
        print(f"✅ Created role: {role.role_name}")
        
        # 3. Issue token
        role_with_token = client.roles.issue_token(
            role_id=role.role_id,
            expiration=3600
        )
        print(f"✅ Issued token for role: {role_with_token.role_name}")
        
        # 4. Test authentication
        test_client = RoseClient(
            base_url="https://admin.rose.blendvision.com",
            access_token=role_with_token.token
        )
        
        datasets = test_client.datasets.list()
        print(f"✅ Authentication test passed - found {len(datasets)} datasets")
        
        return role_with_token
        
    except Exception as e:
        print(f"❌ Authentication setup failed: {e}")
        return None

# Usage
auth_result = setup_authentication(
    account_id="my_project",
    role_name="data_scientist",
    permission="0x1F"
)

if auth_result:
    print(f"🎉 Ready to use! Token: {auth_result.token[:20]}...")
```

Understanding authentication and roles is crucial for secure and effective use of the Rose Recommendation Service. Always follow security best practices and use appropriate permission levels for your use case.
