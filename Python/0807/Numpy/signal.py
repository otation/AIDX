import numpy as np
import matplotlib.pyplot as plt

pure = np.linspace(1, 10, 100)
noise = np.random.normal(0, 1, 100)

signal = pure + noise
plt.plot(signal)
plt.show()