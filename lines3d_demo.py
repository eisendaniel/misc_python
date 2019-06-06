import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(0, 20, 100)
y = np.cos(x)
z = np.sin(x)
ax.plot(x, y, z)
plt.show()
