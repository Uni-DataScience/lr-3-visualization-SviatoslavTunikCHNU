import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """

    fig, ax = plt.subplots()

    counter = collections.Counter(data)

    category = counter.keys()
    counts = counter.values()
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(category, counts, color=bar_colors)

    ax.set_ylabel('категорія')
    ax.set_xlabel('частота')
    ax.set_title(str(data))

    plt.savefig("mygraph.png")

    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
