# Contributing to Nitro

Thank you for your interest in contributing to Nitro! This document provides guidelines for contributors.

## Development Setup

### Prerequisites
- Python 3.9+
- Git
- uv (recommended for dependency management)

### Clone the Repository
```bash
git clone https://github.com/yourusername/nitro.git
cd nitro
```

### Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .[llm]  # Install in editable mode with LLM dependencies

# Or using uv
uv sync --extra llm
```

### Install Development Dependencies
```bash
pip install pytest mypy build twine
# Or
uv add --dev pytest mypy build twine
```

## Building and Testing

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=nitro

# Run integration tests (requires API keys)
pytest tests/test_llm.py::TestLLMIntegration -v
```

### Type Checking
```bash
mypy src/nitro
```

### Build Package
```bash
# Build wheel and sdist
python -m build

# Or with uv
uv build
```

### Test Installation
```bash
# Install from local build
pip install dist/nitrotools-*.whl

# Test import
python -c "from nitro import get_llm; print('OK')"
```

## Code Style

### Python Code
- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters (Black default)
- Use descriptive variable names

### Commit Messages
- Use conventional commits format
- Examples:
  - `feat: add new LLM provider`
  - `fix: resolve config loading issue`
  - `docs: update README installation instructions`

### Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests and type checking
5. Update documentation if needed
6. Commit with clear messages
7. Push to your fork
8. Create a Pull Request

## Reporting Issues

### Bug Reports
- Use the issue template
- Include Python version, OS, and error traceback
- Provide minimal reproducible example
- Check existing issues first

### Feature Requests
- Describe the problem you're solving
- Explain why it's needed
- Provide use case examples

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors.

## License

By contributing, you agree that your contributions will be licensed under the same MIT License as the project.