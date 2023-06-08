from cleo.io.io import IO
from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry


class PythonVersionPlugin(Plugin):
    """Poetry plugin that loads .python-version file and sets the python dependency version in pyproject.toml"""

    def activate(self, poetry: Poetry, io: IO):
        io.write_line("Setting Python version from .python-version file")
        # show current python version
        io.write_line(f"Current Package Python versions: {poetry.package.python_versions}")
        io.write_line(f'Current PyProject dependencies Python: '
                      f'{poetry.pyproject.data["tool"]["poetry"]["dependencies"]["python"]}')

        with open(".python-version") as f:
            version = f.read().strip()
            poetry.package.python_versions = version
            poetry.pyproject.data["tool"]["poetry"]["dependencies"]["python"] = version

        io.write_line(f"New Package Python versions: {poetry.package.python_versions}")
        io.write_line(f'New PyProject dependencies Python: '
                      f'{poetry.pyproject.data["tool"]["poetry"]["dependencies"]["python"]}')
