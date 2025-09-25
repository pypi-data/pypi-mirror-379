import pickle
from dataclasses import dataclass

from ordeq.framework.io import IO, T
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class Pickle(IO[T]):
    """`IO` that loads and saves a Pickle files.

    Example usage:

    ```python
    >>> from ordeq_files import Pickle
    >>> from pathlib import Path
    >>> MyPickle = Pickle(
    ...     path=Path("path/to.pkl")
    ... )

    ```
    """

    path: PathLike

    def load(self) -> T:
        with self.path.open("rb") as fh:
            return pickle.load(fh)

    def save(self, data: T, **save_options) -> None:
        with self.path.open("wb") as fh:
            pickle.dump(data, file=fh, **save_options)
