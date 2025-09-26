from functools import partial
from pathlib import Path
from typing import Iterable
from sphinx_polyversion import *
from sphinx_polyversion.git import closest_tag
from sphinx_polyversion.pyvenv import Poetry, VirtualPythonEnvironment

# ...

#: Arguments to pass to `uv pip install`
UV_ARGS = "-e .[dev]"

#: Arguments to pass to Poetry install (for older versions)
POETRY_ARGS = "--sync"


class UvEnv(VirtualPythonEnvironment):
    """
    A virtual Python environment using `uv` as the package manager.

    This class extends the `VirtualPythonEnvironment` to use `uv` for managing
    the Python environment and dependencies.
    """

    def __init__(
        self,
        path: Path,
        name: str,
        *,
        args: Iterable[str],
        env: dict[str, str] | None = None,
    ):
        super().__init__(
            path,
            name,
            path / ".venv",  # placeholder, determined later
            env=env,
        )
        self.args = args

    async def __aenter__(self):
        # TODO: Call uv to create the python venv
        # TODO: Call uv to install dependencies and package using `self.args`
        # TODO: Ensure `self.venv` is set to the correct path
        return self


#:  Mapping of revisions to (changes of) the environment parameters
ENVIRONMENT = {
    None: Poetry.factory(args=POETRY_ARGS.split()),
    "v7.1": UvEnv.factory(args=UV_ARGS.split()),
}

# ...

DefaultDriver(
    # ...
    env=ENVIRONMENT,
    selector=partial(closest_tag, root),
    # ...
).run(MOCK, SEQUENTIAL)
