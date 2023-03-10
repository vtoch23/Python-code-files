import numpy as np
import matplotlib as mtl
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
mtl.get_configdir()
"/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages"

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0,105)
ax.set_ylim(0,12)
line, = ax.plot(0,0)

def animation_frame(i):
    x_data.append(i*20)
    y_data.append(i)

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    return line,

animat = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,10,0.01), interval=10)
plt.show()
