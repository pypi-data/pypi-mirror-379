# Changelog

All notable changes to the Rose Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive documentation following Recombee API structure
- Detailed API reference with examples
- User guide and integration tips
- Basic and advanced examples
- Error handling documentation

## [1.0.0] - 2025-09-20

### Added
- Initial release of Rose Python SDK
- Core client functionality
- User management (add, update, delete, get, list)
- Item management (add, update, delete, get, list)
- Recommendation engine integration
- Interaction tracking
- Search functionality
- Batch operations
- Error handling with custom exceptions
- Type hints throughout the codebase
- Comprehensive test suite
- Documentation and examples

### Features
- **Client Management**: Easy-to-use client with configuration options
- **User Operations**: Complete user lifecycle management
- **Item Operations**: Full item catalog management
- **Recommendations**: Personalized recommendation engine
- **Interactions**: User behavior tracking
- **Search**: Advanced search capabilities
- **Batch Operations**: Efficient bulk operations
- **Error Handling**: Comprehensive error management
- **Type Safety**: Full type hints and validation

### API Endpoints
- `GET /recommendations/users/{user_id}` - Get user recommendations
- `GET /recommendations/items/{item_id}` - Get item recommendations
- `GET /recommendations/trending` - Get trending items
- `GET /recommendations/popular` - Get popular items
- `POST /users` - Create user
- `GET /users/{user_id}` - Get user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user
- `GET /users` - List users
- `POST /items` - Create item
- `GET /items/{item_id}` - Get item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item
- `GET /items` - List items
- `POST /interactions` - Record interaction
- `GET /search/items` - Search items
- `GET /search/users` - Search users
- `POST /batch` - Batch operations

### Dependencies
- `requests>=2.28.0` - HTTP library
- `pydantic>=1.10.0` - Data validation
- `httpx>=0.24.0` - Async HTTP client
- `typing-extensions>=4.0.0` - Type hints support

### Documentation
- Complete API reference
- Getting started guide
- Installation instructions
- Configuration guide
- Examples and tutorials
- Error handling guide
- Best practices

## Support

For questions about version compatibility or migration assistance:

- **Documentation**: [https://docs.rose.example.com](https://docs.rose.example.com)
- **GitHub Issues**: [https://github.com/luli0034/rose-python-sdk/issues](https://github.com/luli0034/rose-python-sdk/issues)
- **Email**: support@rose.example.com

## Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/luli0034/rose-python-sdk/blob/main/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [License](license.md) file for details.
