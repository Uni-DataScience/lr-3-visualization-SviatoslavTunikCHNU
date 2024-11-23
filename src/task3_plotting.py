import collections

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    fig, _ = plt.subplots()

    counts = collections.Counter(data)

    plt.bar(range(len(counts)), list(counts.values()), tick_label=list(counts.keys()))

    plt.xlabel('Values')
    plt.ylabel('Counts')
    plt.title('Counts of Values')

    plt.savefig("mygraph3_1.png")


def plot_2d(x, y):
    fig, _ = plt.subplots()

    plt.scatter(x,y,s=10)
    plt.savefig("mygraph3_2.png")


def plot_3d(x, y, z):
    fig, _ = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.savefig("mygraph3_3.png")

# Example data
x = np.linspace(0, 10, 20)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
