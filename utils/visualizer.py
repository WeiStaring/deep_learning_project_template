import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self):
        pass


class ScatterplotVisualizer(Visualizer):
    def __init__(self):
        super().__init__()

    def draw_scatterplot(self, x, y=None, title=None):
        if y is None:
            plt.scatter(x[:, 0], x[:, 1], s=5, alpha=0.8)
        else:
            plt.scatter(x[:, 0], x[:, 1], c=y, s=5, alpha=0.8)
        plt.title(title)
        plt.show()


class LinePlotVisualizer(Visualizer):
    def __init__(self):
        super().__init__()

    def draw_lineplot(self, x, title=None, legend=None):
        x = np.array(x)
        for i in range(x.shape[1]):
            plt.plot(x[:, i])
        plt.title(title)
        plt.legend(legend)
        plt.show()
