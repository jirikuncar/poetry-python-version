# Poetry Python Version

**This is a proof-of-concept work. Please add tests for your use-case. Thank you!**

This plugins reads `.python-version` file and sets the python version for the project where it is used.

## Installation

```bash
poetry self add poetry-python-version
# if you use pipx to install poetry
pipx inject poetry poetry-python-version
```

## Usage

When correctly installed you will see:

```
Setting Python version from .python-version file
Current Package Python versions: 3.11.*
Current PyProject dependencies Python: 3.11.*
New Package Python versions: 3.11.3
New PyProject dependencies Python: 3.11.3
```

## Development

Long TODO list

- [ ] tests
- [ ] configuration options
- [ ] documentation
