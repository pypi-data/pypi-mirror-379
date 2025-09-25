import math

import matplotlib.pyplot as plt
from ordeq_matplotlib import MatplotlibFigure


def test_figure(tmp_path):
    # Generate data for the exponential plot
    x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    y = [1, 1.6487, math.e, 4.4817, 7.3891, 12.1825, 20.0855, 33.1155, 54.5982]

    # Create the plot
    plt.plot(x, y)

    # Add grid
    plt.grid(True)

    # Add title and labels
    plt.title("Exponential Plot")
    plt.xlabel("x")
    plt.ylabel("exp(x)")

    figure = MatplotlibFigure(path=tmp_path / "figure.png")
    figure.save(plt.gcf())

    assert (tmp_path / "figure.png").exists()
    assert (tmp_path / "figure.png").read_bytes().startswith(b"\x89PNG\r\n")
