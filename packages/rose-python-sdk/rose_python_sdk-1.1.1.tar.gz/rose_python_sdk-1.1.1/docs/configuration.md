# Configuration

This guide covers all configuration options for the Rose Python SDK.

## Environment Variables

You can configure the SDK using environment variables:

```bash
export ROSE_API_URL="https://api.rose.example.com"
export ROSE_API_KEY="your-api-key-here"
export ROSE_TIMEOUT="30"
export ROSE_MAX_RETRIES="3"
```

## Client Configuration

### Basic Configuration

```python
from rose_sdk import RoseClient

# Using environment variables
client = RoseClient()

# With explicit configuration
client = RoseClient(
    base_url="https://api.rose.example.com",
    api_key="your-api-key-here"
)
```

### Advanced Configuration

```python
client = RoseClient(
    base_url="https://api.rose.example.com",
    api_key="your-api-key-here",
    timeout=30,                    # Request timeout in seconds
    max_retries=3,                 # Maximum retry attempts
    retry_delay=1.0,              # Delay between retries
    verify_ssl=True,              # SSL certificate verification
    user_agent="MyApp/1.0",       # Custom user agent
    headers={                      # Additional headers
        "X-Custom-Header": "value"
    }
)
```

## Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `base_url` | `str` | `None` | Base URL of the Rose API |
| `api_key` | `str` | `None` | Your Rose API key |
| `timeout` | `int` | `30` | Request timeout in seconds |
| `max_retries` | `int` | `3` | Maximum retry attempts |
| `retry_delay` | `float` | `1.0` | Delay between retries in seconds |
| `verify_ssl` | `bool` | `True` | SSL certificate verification |
| `user_agent` | `str` | `Rose-Python-SDK/1.0` | User agent string |
| `headers` | `dict` | `{}` | Additional HTTP headers |

## Environment-Specific Configuration

### Development

```python
# Development configuration
client = RoseClient(
    base_url="https://dev-api.rose.example.com",
    api_key="dev-api-key",
    timeout=60,
    verify_ssl=False  # Only for development
)
```

### Production

```python
# Production configuration
client = RoseClient(
    base_url="https://api.rose.example.com",
    api_key="prod-api-key",
    timeout=30,
    max_retries=5,
    verify_ssl=True
)
```

### Testing

```python
# Testing configuration
client = RoseClient(
    base_url="https://test-api.rose.example.com",
    api_key="test-api-key",
    timeout=10,
    max_retries=1
)
```

## Configuration Files

### Using a Configuration File

Create a `config.json` file:

```json
{
    "base_url": "https://api.rose.example.com",
    "api_key": "your-api-key-here",
    "timeout": 30,
    "max_retries": 3,
    "verify_ssl": true
}
```

Load the configuration:

```python
import json
from rose_sdk import RoseClient

with open('config.json', 'r') as f:
    config = json.load(f)

client = RoseClient(**config)
```

### Using YAML Configuration

Create a `config.yaml` file:

```yaml
base_url: "https://api.rose.example.com"
api_key: "your-api-key-here"
timeout: 30
max_retries: 3
verify_ssl: true
```

Load the configuration:

```python
import yaml
from rose_sdk import RoseClient

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

client = RoseClient(**config)
```

## Dynamic Configuration

### Runtime Configuration Updates

```python
# Update configuration at runtime
client.base_url = "https://new-api.rose.example.com"
client.timeout = 60
client.max_retries = 5
```

### Configuration Validation

```python
# Validate configuration
try:
    client.validate_config()
    print("Configuration is valid")
except ValueError as e:
    print(f"Configuration error: {e}")
```

## Best Practices

1. **Use Environment Variables**: Store sensitive data like API keys in environment variables
2. **Set Appropriate Timeouts**: Adjust timeouts based on your network conditions
3. **Enable Retries**: Use retries for better reliability
4. **Verify SSL**: Always verify SSL certificates in production
5. **Use Custom User Agents**: Include your application name in the user agent

## Troubleshooting

### Common Configuration Issues

**Issue**: `Connection timeout`

**Solution**: Increase the timeout value:
```python
client = RoseClient(timeout=60)
```

**Issue**: `SSL verification failed`

**Solution**: Check your SSL configuration:
```python
# For development only
client = RoseClient(verify_ssl=False)

# For production, ensure proper SSL certificates
client = RoseClient(verify_ssl=True)
```

**Issue**: `API key not found`

**Solution**: Ensure the API key is set:
```python
# Check environment variable
import os
print(os.getenv('ROSE_API_KEY'))

# Or set it explicitly
client = RoseClient(api_key="your-api-key")
```
