import numpy as np
from numba import compiler, types
from scipy import integrate
import matplotlib.pyplot as plt
import time


flatten = lambda l: np.array([item for sublist in l for item in sublist])

#xs = np.linspace(-1-1j, 1-1j, 100)
#ys = np.linspace(-1-1j, -1+1j, 100)
xs = np.linspace(-1,1, 100)
ys = np.linspace(-1j, 1j, 100)
X, Y = np.meshgrid(xs,ys)

compgrid = X+Y

flatgrid = flatten(compgrid)
grid_abs = np.abs(flatgrid)

actual_roots = np.array([1.76929, -0.884646 + 0.589743j, -0.884646 - 0.589743j])
roots_abs = np.abs(actual_roots)
colors = 'gyr'



def newton_n(x0, iters):
    for i in range(iters): x0 = x0 - (x0**3-2*x0-2)/(3*x0**2 - 2)
    return x0

newton_compiled = compiler.compile_isolated(newton_n, [types.complex128, types.double], return_type=types.complex128).entry_point

print()

start_time = time.perf_counter()
print('One call in pure python in:')
print(newton_n(flatgrid[20], 10))
print("--- %s seconds ---" % (time.perf_counter() - start_time))

print()

start_time = time.perf_counter()
res = np.array([newton_n(x, 10) for x in flatgrid])
print('100x100 with 10 iterations in pure python:')
print("--- %s seconds ---" % (time.perf_counter() - start_time))
abs_res = np.abs(res)

print()

start_time = time.perf_counter()
comp_res = np.array([newton_compiled(x, 100) for x in flatgrid])
print('100x100 with 100 iterations using numba:')
print("--- %s seconds ---" % (time.perf_counter() - start_time))

print()

fig, ax = plt.subplots(figsize = (5,5))
start_time = time.perf_counter()

comp_res_color_codes = list(map(lambda x: np.argmin(np.abs(actual_roots-x)), comp_res))

ax.scatter(flatgrid.real, flatgrid.imag,s = 3.5, c = ['gyr'[i] for i in comp_res_color_codes])
print('Plot drawn in:')
print("--- %s seconds ---" % (time.perf_counter() - start_time))
plt.show()


#for i in range(110):
    #print(flatgrid[i].real, flatgrid[i].imag, sep = ' ')
