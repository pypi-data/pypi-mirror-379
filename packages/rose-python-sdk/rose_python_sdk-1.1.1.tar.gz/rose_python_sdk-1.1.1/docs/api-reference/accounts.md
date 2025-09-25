# Accounts API

The Accounts API provides methods to manage Rose accounts and their associated admin roles.

## Create Account

Create a new account with an "admin" role.

### Method Signature

```python
client.accounts.create(
    account_id: str,
    expiration: Optional[int] = None
) -> Role
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `account_id` | `str` | Yes | The account ID to create |
| `expiration` | `int` | No | The expiration time for future tokens in seconds |

### Examples

#### Basic Account Creation

```python
# Create a new account
account = client.accounts.create("my_new_account")

print(f"Created account: {account.account_id}")
print(f"Admin role ID: {account.role_id}")
print(f"Role name: {account.role_name}")
```

#### Create Account with Token Expiration

```python
# Create account with token expiration setting
account = client.accounts.create(
    account_id="my_new_account",
    expiration=86400  # 24 hours for future tokens
)

print(f"Created account with 24-hour token expiration")
```

### Response

```python
Role(
    account_id="my_new_account",
    role_name="admin",
    role_id="role_12345",
    permission=None,
    expired_at=None
)
```

### Important Notes

- This method only creates the account and admin role
- No token is generated automatically
- Use `create_with_token()` to get a token immediately
- Use `client.roles.issue_token()` to get a token for the admin role

## Create Account with Token

Create a new account and immediately issue a token.

### Method Signature

```python
client.accounts.create_with_token(
    account_id: str,
    expiration: Optional[int] = None
) -> RoleWithToken
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `account_id` | `str` | Yes | The account ID to create |
| `expiration` | `int` | No | The expiration time of the access token in seconds |

### Examples

#### Create Account with Immediate Token

```python
# Create account and get token immediately
account_with_token = client.accounts.create_with_token(
    account_id="my_new_account",
    expiration=3600  # 1 hour
)

print(f"Created account: {account_with_token.account_id}")
print(f"Access token: {account_with_token.token}")
print(f"Token expires at: {account_with_token.expired_at}")
```

#### Create Account with Default Token Expiration

```python
# Create account with default token expiration (1 hour)
account_with_token = client.accounts.create_with_token("my_new_account")

print(f"Account created with token: {account_with_token.token}")
```

### Response

```python
RoleWithToken(
    account_id="my_new_account",
    role_name="admin",
    role_id="role_12345",
    permission=None,
    expired_at=1678886400,
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
)
```

### Requirements

- Requires `RefreshAccessToken` permission
- If your token doesn't have this permission, use `create()` instead
- The method combines account creation and token issuance

## Error Handling

```python
from rose_sdk import (
    RoseAPIError,
    RoseValidationError,
    RosePermissionError,
    RoseConflictError
)

try:
    account = client.accounts.create("my_new_account")
except RoseConflictError:
    print("Account already exists")
except RoseValidationError as e:
    print(f"Validation error: {e}")
except RosePermissionError as e:
    print(f"Permission error: {e}")
except RoseAPIError as e:
    print(f"API error: {e}")
```

## Best Practices

1. **Unique Account IDs**: Use unique, descriptive account IDs
2. **Token Expiration**: Set appropriate token expiration times
3. **Permission Management**: Ensure your token has necessary permissions
4. **Error Handling**: Always handle account creation errors
5. **Security**: Store tokens securely and rotate them regularly

## Examples

### Complete Account Setup

```python
# Create account with token
account_with_token = client.accounts.create_with_token(
    account_id="ecommerce_recommendations",
    expiration=7200  # 2 hours
)

print(f"Account created: {account_with_token.account_id}")
print(f"Admin role: {account_with_token.role_name}")
print(f"Token: {account_with_token.token}")

# Use the new account immediately
new_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token=account_with_token.token
)

# Verify the account works
try:
    datasets = new_client.datasets.list()
    print(f"Account is working! Found {len(datasets)} datasets")
except Exception as e:
    print(f"Account verification failed: {e}")
```

### Account Creation with Error Handling

```python
def create_account_safely(account_id: str, expiration: int = 3600):
    """Create an account with proper error handling."""
    try:
        # Try to create account with token
        account = client.accounts.create_with_token(
            account_id=account_id,
            expiration=expiration
        )
        print(f"✅ Account '{account_id}' created successfully")
        return account
    except RoseConflictError:
        print(f"❌ Account '{account_id}' already exists")
        return None
    except RosePermissionError:
        print(f"❌ Insufficient permissions to create account '{account_id}'")
        # Fallback to create without token
        try:
            account = client.accounts.create(account_id, expiration)
            print(f"⚠️  Account '{account_id}' created without token")
            return account
        except Exception as e:
            print(f"❌ Failed to create account: {e}")
            return None
    except Exception as e:
        print(f"❌ Unexpected error creating account '{account_id}': {e}")
        return None

# Use the safe account creation
account = create_account_safely("my_safe_account", expiration=1800)
if account:
    print(f"Account ready: {account.account_id}")
```

### Multi-Account Management

```python
# Create multiple accounts for different environments
environments = [
    {"name": "dev_account", "expiration": 3600},
    {"name": "staging_account", "expiration": 7200},
    {"name": "prod_account", "expiration": 86400}
]

created_accounts = []
for env in environments:
    try:
        account = client.accounts.create_with_token(
            account_id=env["name"],
            expiration=env["expiration"]
        )
        created_accounts.append(account)
        print(f"✅ Created {env['name']} with {env['expiration']}s token")
    except RoseConflictError:
        print(f"⚠️  Account {env['name']} already exists")
    except Exception as e:
        print(f"❌ Failed to create {env['name']}: {e}")

print(f"Successfully created {len(created_accounts)} accounts")
```

### Account Verification

```python
def verify_account(account_with_token):
    """Verify that an account is working properly."""
    try:
        # Create client with the account's token
        test_client = RoseClient(
            base_url="https://admin.rose.blendvision.com",
            access_token=account_with_token.token
        )
        
        # Test basic operations
        datasets = test_client.datasets.list()
        pipelines = test_client.pipelines.list()
        roles = test_client.roles.list()
        
        print(f"✅ Account verification successful:")
        print(f"   - Datasets: {len(datasets)}")
        print(f"   - Pipelines: {len(pipelines)}")
        print(f"   - Roles: {len(roles)}")
        
        return True
    except Exception as e:
        print(f"❌ Account verification failed: {e}")
        return False

# Verify the created account
if account_with_token:
    verify_account(account_with_token)
```

### Token Management for New Account

```python
# After creating an account, manage its tokens
account = client.accounts.create("my_new_account")

# Issue a token for the admin role
admin_token = client.roles.issue_token(
    role_id=account.role_id,
    expiration=3600  # 1 hour
)

print(f"Admin token issued: {admin_token.token}")

# Use the token to create a client for this account
account_client = RoseClient(
    base_url="https://admin.rose.blendvision.com",
    access_token=admin_token.token
)

# Create additional roles for the account
data_scientist_role = account_client.roles.create(
    role_name="data_scientist",
    permission="0x1F",
    with_token=True,
    token_expiration=1800  # 30 minutes
)

print(f"Created data scientist role: {data_scientist_role.role_name}")
print(f"Data scientist token: {data_scientist_role.token}")
```
