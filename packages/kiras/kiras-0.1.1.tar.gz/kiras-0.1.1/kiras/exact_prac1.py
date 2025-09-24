import matplotlib.pyplot as plt
import numpy as np

def prac1():
    """Execute Prac 1 - Neural Network Visualization"""
    # Prac 1
    layers = [4, 8, 3]  # input, hidden, output
    fig, ax = plt.subplots(); ax.axis("off")

    for i, n in enumerate(layers):
        y = np.linspace(0, 1, n)
        for yy in y: ax.add_patch(plt.Circle((i, yy), 0.03, color="skyblue", ec="black"))
        if i < len(layers)-1:
            y_next = np.linspace(0, 1, layers[i+1])
            for y1 in y:
                for y2 in y_next: ax.plot([i, i+1], [y1, y2], "k-", lw=0.5)

    ax.set_title("4-8-3 Neural Network")
    plt.show()

# For backward compatibility
neural_network_visualization = prac1