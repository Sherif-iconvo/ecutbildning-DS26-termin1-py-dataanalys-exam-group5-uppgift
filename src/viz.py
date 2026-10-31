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