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

If you are using `.python-version` file you might want to set the python
version for the project automatically. This Poetry plugin does exactly that.

**`pyproject.toml`**
```toml
# ...
[tool.poetry.dependencies]
python = "3.11.*"
poetry = "^1.5"
# ...
```

It targets application developers that don't want to define Python version
in multiple places and their preferred way is to use `.python-version` file.

**`.python-version`**
```
3.11.3
```

Once you have correctly installed this plugin and your project contains
`.python-version` file you will see following output when you run `poetry install`:

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
- [ ] configuration options - use opt-in rather then always enabled
- [ ] documentation
