"""Poetry plugin to read Python version from .python-version file."""

from poetry.utils._compat import metadata


__version__ = metadata.version("poetry-plugin-export")
