import os
from dataclasses import dataclass

import matplotlib.pyplot as plt
from ordeq.framework.io import Output
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class MatplotlibFigure(Output[plt.Figure]):
    """IO to save matplotlib Figures.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_matplotlib import MatplotlibFigure
    >>> MyFigure = MatplotlibFigure(
    ...     path=Path("path/figure.pdf")
    ... )

    ```

    """

    path: PathLike

    def save(self, fig: plt.Figure) -> None:
        with self.path.open(mode="wb") as fh:
            fig.savefig(fh, format=os.path.splitext(str(self.path))[1][1:])  # noqa: PTH122
