import matplotlib.pyplot as plt
import os
from PIL import Image

def apply_custom_plot_style():
    plt.rcParams.update({
        "axes.edgecolor": "#cccccc",
        "axes.linewidth": 1,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "axes.labelcolor": "#333333",
        "xtick.color": "#555555",
        "ytick.color": "#555555",
        "font.size": 10,
        "grid.color": "#dddddd",
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        "figure.facecolor": "white",
        "axes.facecolor": "#fafafa",
        "legend.frameon": False
    })

def plot_economic_data(data, filename="output/economic_indicators.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    apply_custom_plot_style()
    fig, axes = plt.subplots(len(data), 1, figsize=(10, 8))
    for ax, (name, df) in zip(axes, data.items()):
        ax.plot(df.index, df.values, label=name)
        ax.set_title(name)
        ax.set_ylabel("Value")
        ax.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    img = Image.open(filename)
    img.save(filename, optimize=True)
    plt.close()