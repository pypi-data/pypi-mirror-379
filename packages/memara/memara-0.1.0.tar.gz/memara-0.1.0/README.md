# Memara Python SDK

[![PyPI version](https://badge.fury.io/py/memara.svg)](https://badge.fury.io/py/memara)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The official Python SDK for the [Memara API](https://memara.io) - Give your AI a perfect memory.

## 🚀 Quick Start

### Installation

```bash
pip install memara
```

### Basic Usage

```python
from memara import Memara

# Initialize the client
client = Memara(api_key="your_api_key_here")

# Create a memory
memory = client.create_memory(
    content="Important meeting notes from today",
    tags=["work", "meeting", "important"],
    importance=8
)

# Search memories
results = client.search_memories(
    query="meeting notes",
    limit=10
)

# List all memories
memories = client.list_memories(page=1, size=20)

# Close the client when done
client.close()

# Or use as a context manager (recommended)
with Memara(api_key="your_api_key") as client:
    memory = client.create_memory("Hello from Python SDK!")
```

## 📖 Documentation

### Authentication

Get your API key from [Memara Dashboard](https://memara.io/dashboard) and set it either:

1. **As environment variable** (recommended):
```bash
export MEMARA_API_KEY="your_api_key_here"
```

2. **Or pass directly**:
```python
client = Memara(api_key="your_api_key_here")
```

### Configuration

```python
# Full configuration options
client = Memara(
    api_key="your_api_key",           # Your Memara API key
    base_url="https://api.memara.io", # API base URL (optional)
    timeout=30.0                      # Request timeout in seconds
)
```

### Memory Operations

#### Create Memory
```python
memory = client.create_memory(
    content="The content of your memory",
    tags=["tag1", "tag2"],           # Optional: list of tags
    source="my_app",                 # Optional: source identifier  
    importance=7,                    # Optional: 1-10 importance level
    space_id="space_uuid"            # Optional: specific space ID
)
```

#### Search Memories
```python
# Basic search
results = client.search_memories("your search query")

# Advanced search
results = client.search_memories(
    query="meeting notes",
    limit=20,                        # Max results to return
    space_id="specific_space_id",    # Search within specific space
    cross_space=False               # Search across all spaces
)
```

#### Get Memory by ID
```python
memory = client.get_memory("memory_uuid")

# With space context
memory = client.get_memory("memory_uuid", space_id="space_uuid")
```

#### Delete Memory
```python
result = client.delete_memory("memory_uuid")
```

### Space Operations

#### List Spaces
```python
spaces = client.list_spaces()
for space in spaces:
    print(f"Space: {space.name} ({space.memory_count} memories)")
```

#### Create Space
```python
space = client.create_space(
    name="My Project Space",
    icon="🚀",                      # Optional: emoji icon
    color="#6366F1",               # Optional: hex color
    template_type="work"           # Optional: template type
)
```

## 🔧 Advanced Usage

### Error Handling

```python
from memara import Memara, MemaraAPIError, MemaraAuthError

try:
    with Memara() as client:
        memory = client.create_memory("Test memory")
except MemaraAuthError:
    print("Authentication failed - check your API key")
except MemaraAPIError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Environment Variables

Set these environment variables for easier configuration:

```bash
export MEMARA_API_KEY="your_api_key_here"
export MEMARA_API_URL="https://api.memara.io"  # Optional: custom API URL
```

### Async Usage (Coming Soon)

Future versions will include async support:

```python
# Coming in v0.2.0
from memara import AsyncMemara

async with AsyncMemara(api_key="your_key") as client:
    memory = await client.create_memory("Async memory!")
```

## 🛠️ Development

### Contributing

1. Clone the repository
2. Install development dependencies: `pip install -e .[dev]`  
3. Run tests: `pytest`
4. Format code: `black memara/`
5. Type check: `mypy memara/`

### Running Tests

```bash
# Install with dev dependencies
pip install -e .[dev]

# Run tests
pytest

# Run tests with coverage
pytest --cov=memara
```

## 🔗 Links

- **Homepage**: [memara.io](https://memara.io)
- **Documentation**: [memara.io/docs](https://memara.io/docs)
- **API Reference**: [memara.io/docs/api](https://memara.io/docs/api)
- **GitHub**: [github.com/memara-ai/memara-python-sdk](https://github.com/memara-ai/memara-python-sdk)
- **PyPI**: [pypi.org/project/memara](https://pypi.org/project/memara/)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [memara.io/docs](https://memara.io/docs)
- **Discord**: [discord.memara.io](https://discord.memara.io)
- **Email**: [support@memara.io](mailto:support@memara.io)
- **Issues**: [GitHub Issues](https://github.com/memara-ai/memara-python-sdk/issues)

---

**Give your AI a perfect memory with Memara** 🧠✨
