import matplotlib 
from matplotlib import pyplot as plt
matplotlib.path = "/home/codespace/.config/matplotlib"
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()