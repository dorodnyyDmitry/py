import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri


print('grid density?:')
grid_density = int(input())

radii = np.linspace(0, 1, grid_density)
angles = np.linspace(0, 2 * 3.14, grid_density)
angles = np.repeat(angles[..., np.newaxis], grid_density, axis=1)
angles[:, 1::2] += 3.14 / grid_density

X = (radii * np.cos(angles)).flatten()
Y = (radii * np.sin(angles)).flatten()
Z = abs(X) + abs(Y) + (np.sin(X + Y))**2

triang = tri.Triangulation(X, Y)
fig1, ax1 = plt.subplots()

tcf = ax1.tricontourf(triang, Z)

ax1.tricontour(triang, Z, colors='k')

plt.show()
