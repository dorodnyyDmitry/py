import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-1, 1, 2000)
ylist = np.linspace(-1, 1, 2000)
X, Y = np.meshgrid(xlist, ylist)

Z = abs(X) + abs(Y) + (np.sin(X+Y))**2

pts = X**2 +Y**2 > 1

mask = np.ones(X.shape)
mask[pts] = 0

levels = [0.0, 0.5, 1.0,  1.2,  1.5]
contour = plt.contour(X*mask, Y*mask, Z, levels)

plt.show()
