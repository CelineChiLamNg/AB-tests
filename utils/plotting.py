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
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


def plot_with_error_bars(df_analytical, df_bootstrap):
    fig, ax = plt.subplots(figsize=(10, 6))
    n_groups = len(df_analytical)

    index = np.arange(n_groups)
    bar_width = 0.35

    errors_analytical = [df_analytical['Mean'] - df_analytical['CI Lower'],
                         df_analytical['CI Upper'] - df_analytical['Mean']]

    errors_bootstrap = [df_bootstrap['Mean'] - df_bootstrap['CI Lower'],
                        df_bootstrap['CI Upper'] - df_bootstrap['Mean']]


    rects1 = ax.bar(index, df_analytical['Mean'], bar_width,
                    color='b', label='Analytical',
                    yerr=np.abs(errors_analytical), capsize=5)

    rects2 = ax.bar(index + bar_width, df_bootstrap['Mean'], bar_width,
                    color='g', label='Bootstrap',
                    yerr=np.abs(errors_bootstrap), capsize=5)

    ax.set_xlabel('Promotion')
    ax.set_ylabel('Sales Mean')
    ax.set_title('Sales Means and Confidence Intervals by Promotion')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(['Promotion 1', 'Promotion 2', 'Promotion 3'])
    ax.legend()

    plt.show()