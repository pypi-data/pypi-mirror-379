# TF AI Agents

[![PyPI version](https://badge.fury.io/py/tf-ai-agents.svg)](https://badge.fury.io/py/tf-ai-agents)
[![Python Support](https://img.shields.io/pypi/pyversions/tf-ai-agents.svg)](https://pypi.org/project/tf-ai-agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package for AI agent functionality by ThoughtFocus.

## Installation

You can install `tf-ai-agents` from PyPI:

```bash
pip install tf-ai-agents
```

Or install the development version from source:

```bash
git clone https://github.com/sonukumar-tf/tf-ai-agents.git
cd tf-ai-agents
pip install -e .
```

## Quick Start

```python
from tf_ai_agents import hello_world

# Basic usage
result = hello_world("Hello, AI!")
print(result)  # Output: "Hello, AI!"

# With debug mode
result = hello_world("Hello, AI!", debug=True)
# Output: 
# Hello World
# "Hello, AI!"
```

## Features

- Simple and intuitive API
- Debug mode for development
- Full type hints support
- Compatible with Python 3.11+

## Development

### Setup Development Environment

```bash
git clone https://github.com/sonukumar-tf/tf-ai-agents.git
cd tf-ai-agents
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black tf_ai_agents/
isort tf_ai_agents/
```

### Type Checking

```bash
mypy tf_ai_agents/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### 0.1.0a1 (2024-01-XX)

- Initial alpha release
- Added `hello_world` function with debug support
