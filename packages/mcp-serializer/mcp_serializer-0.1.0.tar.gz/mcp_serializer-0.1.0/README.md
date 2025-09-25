# MCP Serializer

A serialization library for Model Context Protocol.

## Installation

```bash
pip install mcp-serializer
```

## Usage

This package is currently in early development. More documentation will be added as features are implemented.

## Development

To set up for development:

```bash
# Clone the repository
git clone https://github.com/mdamire/mcp-serializer.git
cd mcp-serializer

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .

# Run tests
pytest

# Run code formatting
black src tests
isort src tests

# Run type checking
mypy src
```

## License

MIT License. See [LICENSE](LICENSE) for details.