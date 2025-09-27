# DinoScan - Python Code Analysis Tool

[![PyPI version](https://badge.fury.io/py/dinoscan.svg)](https://badge.fury.io/py/dinoscan)
[![Python Support](https://img.shields.io/pypi/pyversions/dinoscan.svg)](https://pypi.org/project/dinoscan/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DinoScan** is a comprehensive AST-based Python code analysis tool that provides real-time diagnostics, security scanning, and code quality metrics. It features 5 specialized analyzers designed to help you write better, more secure Python code.

## 🚀 Features

### Core Analysis Capabilities

- **Security Vulnerability Detection**: Identifies potential security issues like hardcoded secrets and dangerous function calls
- **Dead Code Analysis**: Finds unused functions, variables, and imports
- **Circular Import Detection**: Prevents import dependency issues
- **Documentation Analysis**: Ensures proper code documentation with docstrings
- **Duplicate Code Detection**: Identifies code duplication patterns

### Analysis Profiles

- **Minimal**: Essential issues only - security vulnerabilities and critical circular imports
- **Standard** (Default): Balanced analysis including documentation and minor dead code issues
- **Comprehensive**: Thorough analysis with detailed duplicate detection and advanced patterns

### Output Formats

- **JSON**: Machine-readable format for integration with other tools
- **Text**: Human-readable console output for direct review

## 📦 Installation

Install DinoScan using pip:

```bash
pip install dinoscan
```

Or install with development dependencies:

```bash
pip install dinoscan[dev]
```

## 🎯 Quick Start

### Command Line Usage

Analyze a single Python file:

```bash
# Run security analyzer
dinoscan security myfile.py

# Run all analyzers
dinoscan all myfile.py

# Use comprehensive profile
dinoscan security myfile.py --profile comprehensive

# Output as human-readable text
dinoscan all myfile.py --format text
```

### Programmatic Usage

```python
from dinoscan import DinoScan
from pathlib import Path

# Initialize scanner
scanner = DinoScan(profile="standard")

# Analyze a file with specific analyzer
results = scanner.analyze("myfile.py", "security")

# Analyze with all analyzers
all_results = scanner.analyze_all("myfile.py")

# Process results
for finding in results:
    print(f"{finding['severity']}: {finding['message']}")
    print(f"  File: {finding['file']}:{finding['line']}")
    print(f"  Rule: {finding['rule_id']}")
    if 'fix_suggestion' in finding:
        print(f"  Fix: {finding['fix_suggestion']}")
```

## 🔍 Analyzers

### Security Analyzer (`security`)

Detects potential security vulnerabilities:

```python
# This will be flagged
password = "hardcoded_secret"  # SEC001: Potential hardcoded secret
eval(user_input)               # SEC002: Dangerous function call
```

**Detected Issues:**

- Hardcoded secrets and passwords
- Dangerous function usage (`eval`, `exec`)
- Unsafe input handling patterns

### Dead Code Analyzer (`dead-code`)

Identifies unused code elements:

```python
def unused_function():  # DEAD001: Potentially unused definition
    return "never called"

def used_function():
    return "this is called"

result = used_function()  # This makes used_function "used"
```

### Circular Import Analyzer (`circular`)

Prevents import dependency cycles:

```python
# In module_a.py
from module_b import something  # CIRC001: Potential circular import

# If module_b.py also imports from module_a, this creates a cycle
```

### Documentation Analyzer (`docs`)

Ensures proper code documentation:

```python
def undocumented_function():  # DOC001: Function missing docstring
    return True

def documented_function():
    """This function has proper documentation."""  # ✓ Good
    return True

class UndocumentedClass:  # DOC002: Class missing docstring
    pass
```

### Duplicate Code Analyzer (`duplicates`)

Finds code duplication:

```python
def calculate_area_v1():  # DUP001: Duplicate function body detected
    length = 10
    width = 5
    return length * width

def calculate_area_v2():  # Same implementation = duplicate
    length = 10
    width = 5
    return length * width
```

## ⚙️ Configuration

### Analysis Profiles

```bash
# Minimal - only critical issues
dinoscan security myfile.py --profile minimal

# Standard - balanced analysis (default)
dinoscan all myfile.py --profile standard

# Comprehensive - thorough analysis
dinoscan all myfile.py --profile comprehensive
```

### Exclude Patterns

```bash
# Exclude test files and virtual environments
dinoscan all myproject/ --exclude "tests/*" --exclude "venv/*" --exclude "__pycache__/*"
```

### Available Analyzers

| Analyzer     | Description                      | Focus Area                    |
| ------------ | -------------------------------- | ----------------------------- |
| `security`   | Security vulnerability detection | Security issues, secrets      |
| `dead-code`  | Unused code detection            | Code cleanup, maintainability |
| `circular`   | Circular import detection        | Architecture, dependencies    |
| `docs`       | Documentation analysis           | Code documentation            |
| `duplicates` | Code duplication detection       | Code quality, DRY principle   |
| `all`        | Run all analyzers                | Comprehensive analysis        |

## 📊 Example Output

### JSON Format (Default)

```json
[
  {
    "file": "example.py",
    "line": 5,
    "column": 12,
    "severity": "warning",
    "message": "Potential hardcoded secret detected",
    "rule_id": "SEC001",
    "analyzer": "security",
    "category": "security",
    "fix_suggestion": "Move secrets to environment variables or secure configuration files"
  }
]
```

### Text Format

```
WARNING: Potential hardcoded secret detected [SEC001]
  --> example.py:5:12 (security)

ERROR: Dangerous function call: eval [SEC002]
  --> example.py:8:4 (security)
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension.git
cd DinoScan-VSCode-Extension/dinoscan-package

# Install in development mode
pip install -e .[dev]

# Run tests
pytest tests/ -v

# Run linting
black dinoscan/
isort dinoscan/
mypy dinoscan/
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v --cov=dinoscan

# Run specific test categories
pytest tests/test_core.py -v
pytest tests/test_analyzers.py -v
pytest tests/test_cli.py -v
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension/blob/main/CONTRIBUTING.md) for details.

### Areas for Contribution

- **New Analyzers**: Add specialized analyzers for specific Python patterns
- **Performance Improvements**: Optimize analysis speed and memory usage
- **Additional Output Formats**: Support for SARIF, XML, or other formats
- **Enhanced Detection**: Improve accuracy of existing analyzers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension/blob/main/LICENSE) file for details.

## 🔗 Related Projects

- **[DinoScan VS Code Extension](https://marketplace.visualstudio.com/items?itemName=dinoair.dinoscan-vscode)**: Integrates DinoScan directly into Visual Studio Code
- **[GitHub Repository](https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension)**: Source code and issue tracker

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dinopitstudiosowner/DinoScan-VSCode-Extension/discussions)

---

**Happy Analyzing!** 🦕✨ It's Free and Open Source!
