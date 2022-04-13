import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self):
        pass


class ScatterplotVisualizer(Visualizer):
    def __init__(self):
        super().__init__()

    def draw_scatterplot(self, x, y=None, title=None, save_path=None):
        if y is None:
            plt.scatter(x[:, 0], x[:, 1], s=5, alpha=0.8)
        else:
            plt.scatter(x[:, 0], x[:, 1], c=y, s=5, alpha=0.8)
        plt.title(title)
        if save_path is not None:
            plt.savefig(save_path)
        plt.show()


class LinePlotVisualizer(Visualizer):
    def __init__(self):
        super().__init__()

    def draw_lineplot(self, x, title=None, save_path=None):
        x = np.array(x)
        if len(x.shape) == 1:
            plt.plot(x)
        elif len(x.shape) == 2:
            for i in range(x.shape[1]):
                plt.plot(x[:, i])
        plt.title(title)
        if save_path is not None:
            plt.savefig(save_path)
        plt.show()
