import matplotlib.pyplot as plt
import os

def plot_economic_data(data, filename="output/economic_indicators.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axes = plt.subplots(len(data), 1, figsize=(10, 8))
    for ax, (name, df) in zip(axes, data.items()):
        ax.plot(df.index, df.values, label=name)
        ax.set_title(name)
        ax.set_ylabel("Value")
        ax.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
