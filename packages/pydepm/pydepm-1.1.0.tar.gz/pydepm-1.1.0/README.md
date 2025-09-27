# PyDepM — Python Dependency Manager

[![PyPI version](https://img.shields.io/pypi/v/pydepm.svg)](https://pypi.org/project/pydepm/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydepm.svg)](https://pypi.org/project/pydepm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PyDepM** (Python Dependency Manager) is a modern, dependency management tool for Python projects that combines the simplicity of npm with Python's powerful packaging ecosystem. It provides two main tools: `pydep` for dependency management and project scaffolding, and `pydepx` for enhanced script execution.

## Features

### **Pydep - Core Dependency Manager**
- **Project Scaffolding**: Initialize apps or modules with sensible defaults
- **Dependency Management**: Add, remove, and update dependencies with version pinning
- **Virtual Environment Management**: Automatic venv creation and management
- **Lockfile Support**: Generate and use `pypackage-lock.json` for reproducible installs
- **Build System**: Build wheels, sdists, and PyInstaller executables
- **Security Auditing**: Vulnerability scanning with `pip-audit`
- **Script Runner**: npm-like script execution from `pypackage.json`
- **Dependency Analysis**: Understand why packages are installed with `pydep why`
- **Bidirectional conversion** between `pypackage.json` and `pyproject.toml` with `pydep convert`
- **Custom fields support**: Preserve non-standard fields during conversion
- **Smart field mapping**: Handles project metadata, dependencies, and custom sections

### **Pydepx - Enhanced Execution Tool**
- **Rich Output**: Beautiful, colorized command output with real-time streaming
- **Smart Module Execution**: Automatic Python module detection and execution
- **Cross-Platform**: Consistent behavior on Windows, macOS, and Linux
- **Signal Handling**: Graceful interrupt handling for long-running processes
- **Encoding Support**: Robust handling of various terminal encodings

## Installation

```bash
pip install pydepm
```

This installs both `pydep` and `pydepx` commands globally.

## Quick Start

### Create a New Project

```bash
# Create an application
pydep init --type app

# Or create a reusable module
pydep init my-module --type module 
```

### Manage Dependencies

```bash
# Install all dependencies
pydep install

# Add a package
pydep add requests
pydep add "flask>=2.0.0"

# Add with caret syntax (equivalent to npm's ^)
pydep add "numpy^1.24.0"

# Remove a package
pydep remove requests
```

### Run Scripts

```bash
# Run scripts defined in pypackage.json
pydep run dev
pydep run test

# Use pydepx for enhanced execution
pydepx black .                    # Run code formatter
pydepx -m pytest tests/          # Run tests as module
pydepx -m http.server 8000       # Run HTTP server
```

## Table of Contents

- [Project Structure](#project-structure)
- [pydep Commands](#pydep-commands)
- [pydepx Usage](#pydepx-usage)
- [Configuration](#configuration)
- [Advanced Features](#advanced-features)
- [Examples](#examples)
- [Contributing](#contributing)

## Project Structure

PyDepM uses a `pypackage.json` file to manage project configuration:

```json
{
  "type": "app",
  "name": "my-project",
  "version": "0.1.0",
  "description": "My Python application",
  "dependencies": {
    "requests": "^2.28.0",
    "rich": "==12.6.0"
  },
  "optionalDependencies": {
    "dev": {
      "pytest": ">=7.0.0",
      "pytest-cov": ">=4.0.0",
      "black": ">=23.0.0",
      "mypy": ">=1.0.0"
    },
    "test": {
      "pytest": ">=7.0.0",
      "pytest-asyncio": ">=0.20.0",
      "httpx": ">=0.23.0"
    },
    "docs": {
      "sphinx": ">=6.0.0",
      "sphinx-rtd-theme": ">=1.0.0"
    }
  },
  "scripts": {
    "dev": "python main.py",
    "test": "pytest tests/"
  },
  "useGlobalDeps": false
}
```

### Converting Between Formats

PyDepM provides seamless conversion between `pypackage.json` and `pyproject.toml`:

```bash
# Convert pyproject.toml to pypackage.json
pydep convert --from toml

# Convert pypackage.json to pyproject.toml
pydep convert --to toml
```

#### Custom Fields Handling

When converting from `pyproject.toml` to `pypackage.json`:
- Standard fields (name, version, description, etc.) are mapped directly
- Custom fields under `[project]` are preserved with `project.` prefix
- Non-standard sections are preserved in the `pyproject._raw` field

Example conversion:

`pyproject.toml`:
```toml
[project]
name = "my-project"
version = "0.1.0"
[project.urls]
Homepage = "https://example.com"
```

Converts to `pypackage.json`:
```json
{
  "name": "my-project",
  "version": "0.1.0",
  "pyproject": {
    "project.urls": {
      "Homepage": "https://example.com"
    }
  }
}
```

### Managing Optional Dependencies

Optional dependencies are grouped by purpose (e.g., `dev`, `test`, `docs`) and can be installed interactively when running `pydep install`:

```bash
# Install all optional dependencies
pydep install
```

PyDepM will prompt you to select which optional dependency groups to install during the installation process.

## pydep Commands

### Project Management
```bash
pydep init [name] [--type app|module]  # Initialize new project
pydep install [-e] [-g]                # Install dependencies
pydep build                            # Build package/executable
```

### Dependency Management
```bash
pydep add <package> [--global]         # Add package(s)
pydep remove <package> [--global]      # Remove package(s)
pydep update [packages] [--global]     # Update packages
pydep list                             # List installed packages
pydep why <package>                    # Show dependency reason
pydep outdated                         # Check for outdated packages
pydep clear-cache [--max-age DAYS]     # Clear package cache (default max-age is 30 days)
```

### Security & Quality
```bash
pydep audit [--json] [--extended]      # Security audit
pydep convert --to lock [--hashes]     # Generate lockfile
pydep convert --to toml [-o dir]       # Generate pyproject.toml
```

### Script Execution
```bash
pydep run <script>                     # Run project script
```

## pydepx Usage

`pydepx` enhances command execution with rich output and better handling:

```bash
# Direct command execution
pydepx black

# Module execution (python -m style)
pydepx -m pytest -v tests/
pydepx -m pip install package
pydepx -m http.server --bind 127.0.0.1 8000
```

## Configuration

### Project Types

**Application (app)**: Standalone applications with executable support
- Default project type
- Can build executables with PyInstaller
- Optional `pyproject.toml` generation

**Module (module)**: Reusable Python packages
- Always generates `pyproject.toml`
- Supports setuptools packaging
- CLI entry point generation

### Virtual Environments

By default, PyDepM creates and uses virtual environments. You can override this:

```bash
# Use global Python site-packages for a command
pydep install --global
pydep add requests --global

# Configure project to always use global deps
pydep init --type app --global-deps
```

## Advanced Features

### Configuration Conversion
```bash
# Convert to pyproject.toml
pydep convert --to toml

# Convert from pyproject.toml to pypackage.json
pydep convert --from toml

# Generate lockfile (no hashes)
pydep convert --to lock

# Generate lockfile with SHA256 hashes
pydep convert --to lock --hashes
```

### Executable Building
For app-type projects, configure executables in `pypackage.json`:

```json
{
  "executable": {
    "target": "main.py",
    "parameters": ["--onefile", "--name=myapp"],
    "output": "dist/"
  }
}
```

Build with:
```bash
pydep build
```

### Custom pyproject.toml
For advanced use cases, you can provide custom `pyproject.toml` content:
```json
{
  "pyproject": {
    "[project.urls]": "https://github.com/ZtaMDev/PyDepM.git"
  }
}
```

or you can use the _raw option to put pyproject.toml content directly:

```json
{
  "_raw": "[project.urls] = 'https://github.com/ZtaMDev/PyDepM.git'"
}
```

## Examples

### Complete Workflow

```bash
# Create and set up a new module
pydep init --type module my-package
cd my-package

# Add dependencies
pydep add rich
pydep add "pytest^7.0.0" --dev

# Install everything
pydep install

# Run tests
pydep run test
# or with enhanced output
pydepx -m pytest tests/

# Build package
pydep build

# Security audit
pydep audit
```

### Development Scripts

Define scripts in `pypackage.json`:

```json
{
  "scripts": {
    "dev": "python main.py",
    "test": "pytest tests/ -v",
    "lint": "pylint src/",
    "format": "black . && isort ."
  }
}
```
 
## Branch Protection

The `CrystalMain` branch is protected with the following rules to ensure code quality:

### Required Status Checks
- Unit tests (all Python versions)
- Integration tests
- Performance tests
- Security audit
- No merge conflicts
  
### Pull Request Requirements
- 1 approval required
- Stale approvals dismissed on new commits
- Last push must be approved
- Conversation resolution required
- Linear history required 
 
### Admin Bypass
- Repository owner can bypass branch protection rules when needed

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

```bash
git clone https://github.com/ZtaMDev/PyDepM.git
cd PyDepM
pip install -e .
```

## License

MIT License - see [LICENSE](https://opensource.org/licenses/MIT) for details.

---

**PyDepM** makes Python dependency management intuitive and powerful, combining the best practices from modern development workflows with Python's rich ecosystem.
