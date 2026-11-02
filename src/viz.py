import matplotlib.pyplot as plt
import pandas as pd


def create_bar_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str
) -> None:
    """
    Creates a reusable bar chart.
    """

    plt.figure(figsize=(8, 5))

    data.plot(kind="bar", color="skyblue")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    sample_data = pd.Series(
        [100, 200, 150],
        index=["A", "B", "C"]
    )

    create_bar_chart(
        sample_data,
        "Sample Chart",
        "Category",
        "Value"
    )
def pie_chart_top3(ax, x, y, title, legend_title=None):
    ax.pie(y, autopct="%1.1f%%")
    ax.legend(x, title=legend_title, loc="center left", bbox_to_anchor=(1, 0.5))
    ax.set_title(title)
import pandas as pd

def bar(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    x = x
    y = y
    ax.bar(x,y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax
