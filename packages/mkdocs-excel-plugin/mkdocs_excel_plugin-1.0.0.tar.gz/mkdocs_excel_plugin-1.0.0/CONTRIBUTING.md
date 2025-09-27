# Contributing to mkdocs-excel-plugin

Thank you for your interest in contributing to mkdocs-excel-plugin! We welcome contributions from everyone.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Wangjunyu/mkdocs-excel-plugin.git
   cd mkdocs-excel-plugin
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=mkdocs_excel

# Run specific test
pytest tests/test_plugin.py::test_specific_function
```

## Code Style

We use the following tools to maintain code quality:

- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

```bash
# Format code
black mkdocs_excel/ tests/

# Check linting
flake8 mkdocs_excel/ tests/

# Type checking
mypy mkdocs_excel/
```

## Submitting Changes

1. **Fork** the repository
2. **Create** a new branch for your feature/fix
3. **Make** your changes
4. **Add** tests for your changes
5. **Run** the test suite
6. **Submit** a pull request

## Pull Request Guidelines

- Include a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Add tests for new functionality
- Update documentation if needed

## Reporting Bugs

Please use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) when reporting bugs.

## Feature Requests

Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) for suggesting new features.

## Code of Conduct

Please be respectful and inclusive in all interactions. We're all here to learn and improve the project together.

## Questions?

Feel free to open an issue or discussion if you have questions about contributing!