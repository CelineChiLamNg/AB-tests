import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List


def stacked_bar_plot(df: pd.DataFrame, col: str, hue: str,
                     color: Optional[List[str]] = None,
                     title: Optional[str] = None, xlabel: Optional[str] = None,
                     ylabel: Optional[str] = None) -> None:
    """
    Plots a stacked bar chart with the given DataFrame and column,
    with stack segments defined by hue.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        col (str): The column name to be used as the x-axis.
        hue (str): The column name used to define the stack segments.
        color (Optional[List[str]]): A list of colors for each stack segment.
        title (Optional[str]): The title of the plot.
        xlabel (Optional[str]): The label for the x-axis.
        ylabel (Optional[str]): The label for the y-axis.

    """
    categories = df[col].unique()
    hues = df[hue].unique()

    if color is None:
        color = sns.color_palette('dark', n_colors=len(hues))

    fig, ax = plt.subplots()

    bottom = np.zeros(len(categories))

    for idx, h in enumerate(hues):
        group_data = df[df[hue] == h].groupby(col).size().reindex(categories,
                                                                  fill_value=0)
        plt.bar(categories, group_data, bottom=bottom, color=color[idx],
                label=h)
        bottom += group_data.values

    plt.xlabel(xlabel if xlabel else col)
    plt.ylabel(ylabel if ylabel else 'Count')
    plt.title(title if title else f'{col} Counts by {hue}')
    plt.legend(title=hue)

    plt.show()