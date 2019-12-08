import numpy as np
from numba import compiler, types
from scipy import integrate
import matplotlib.pyplot as plt
from timeit import *
import time

params = np.array([1, 1.5, 2, 1.5])
a,b,c,d = params[0],params[1],params[2],params[3]

equil1 = np.array([0., 0.])
equil2 = np.array([c/d, a/b])

t0 = 0.
t1 = 100.
dt = 1.
s0 = np.array([1., 1.])

def df_dt(t, vars, params):
    a,b,c,d = params
    x, y = vars
    return np.array([(a - b*y)*x , (-c + d*x)*y])

print('python RHS calculation')
start_time = time.perf_counter()
print(df_dt(t0, s0, params))
print("--- %s seconds ---" % (time.perf_counter() - start_time))


start_time = time.perf_counter()
df_dt_compiled = compiler.compile_isolated(df_dt, [types.double, types.double[:], types.double[:]], return_type=types.double[:]).entry_point

print('numba RHS calculation')
start_time = time.perf_counter()
print(df_dt_compiled(t0, s0, params))
print("--- %s seconds ---" % (time.perf_counter() - start_time))

pyint = integrate.ode(df_dt)
pyint.set_integrator('dop853').set_f_params(params).set_initial_value(s0, t0)

cint = integrate.ode(df_dt_compiled)
cint.set_integrator('dop853').set_f_params(params).set_initial_value(s0, t0)

print('python 0...100')
start_time = time.perf_counter()
pyres = np.array([pyint.integrate(t) for t in np.linspace(t0, t1, 100)])
print("--- %s seconds ---" % (time.perf_counter() - start_time))

print('numba 0...100')
start_time = time.perf_counter()
numres = np.array([cint.integrate(t) for t in np.linspace(t0, t1, 100)])
print("--- %s seconds ---" % (time.perf_counter() - start_time))


fig, ax = plt.subplots(figsize = (5,5))

for v in np.linspace(0.3, 0.9, 5):
    vals = v * equil2
    pyint.set_initial_value(vals, t0)
    oderes = np.array([pyint.integrate(t) for t in np.linspace(t0, 10, 100)])
    ax.plot(oderes[:, 0], oderes[:, 1])

plt.show()
