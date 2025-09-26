# Changelog

All notable changes to the Memara Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-15

### Added
- Initial release of the Memara Python SDK
- Core memory operations (create, get, search, delete)
- Space management (list, create)
- Comprehensive error handling with custom exceptions
- Type-safe data models using Pydantic
- Context manager support for automatic cleanup
- Environment variable configuration support
- Full test suite with pytest
- Complete documentation and usage examples

### Features
- **Memory Management**: Create, retrieve, search, and delete memories
- **Space Management**: Organize memories in spaces with templates
- **Authentication**: API key-based authentication with environment variable support  
- **Error Handling**: Custom exceptions for different error scenarios
- **Type Safety**: Full type hints and Pydantic models
- **Developer Experience**: Clean API design with comprehensive documentation

### Dependencies
- `httpx>=0.24.0` for HTTP client functionality
- `pydantic>=2.0.0` for data validation and serialization

### Supported Python Versions
- Python 3.9+
- Python 3.10
- Python 3.11
- Python 3.12

## [Unreleased]

### Planned for v0.2.0
- Async client support (`AsyncMemara`)
- Memory update/edit operations
- Advanced search filters and options
- Bulk operations for memories
- Streaming responses for large datasets
- Enhanced error reporting with detailed context
- Performance optimizations
- Additional space management features
