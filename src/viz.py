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