import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

R=1.496000e+08

data = np.loadtxt('traj.txt', dtype = float)

df = pd.DataFrame(data, columns = ['x', 'y', 'z', 'vx', 'vy', 'vz', 't'])

print(df)

plt.plot(data[:, 0]*R, data[:, 1]*R)
plt.savefig('xy')
plt.clf()
plt.plot(data[:, 0]*R, data[:, 2]*R)
plt.savefig('xz')
plt.clf()
plt.plot(data[:, 1]*R, data[:, 2]*R)
plt.savefig('yz')
plt.clf()

df['absy'] = np.fabs(df['y'])

sortedf = df.sort_values('absy')

xz = sortedf[0:100:1]

apx = ((np.amin(xz[xz['x']>0]) - np.amax(xz[xz['x']<0]))*R)['x']
apz = ((np.amin(xz[xz['z']>0]) - np.amax(xz[xz['z']<0]))*R)['z']


df['absvy'] = np.fabs(df['vy'])

sortedvy = df.sort_values('absvy')
y = sortedvy[0:100:1]
apy = ((np.amin(y[y['y']>0]) - np.amax(y[y['y']<0]))*R)['y']

fig, ax = plt.subplots(1,3, figsize = (25,5))

ax[0].scatter(y[['x']]*R, y[['y']]*R, zorder = 100, color = 'r')   #(y[['x', 'y']]*R).plot.scatter(x = 'x', y = 'y', zorder = 100)
ax[0].scatter(xz[['x']]*R, xz[['y']]*R, zorder = 100, color = 'r')    #(xz[['x', 'y']]*R).plot.scatter(x = 'x', y = 'y', zorder = 100)
ax[0].plot(data[:, 0]*R, data[:, 1]*R, color = 'b')


ax[1].scatter(xz[['x']]*R, xz[['z']]*R, zorder = 100, color = 'r') #(xz[['x', 'z']]*R).plot.scatter(x = 'x', y = 'z',zorder= 100, color = 'r')
ax[1].plot(data[:, 0]*R, data[:, 2]*R, color = 'b')

ax[2].plot(data[:, 1]*R, data[:, 2]*R, color = 'b')
plt.show()

print('x: ', np.amax(data[:,0])*R - np.amin(data[:,0])*R,'y: ', np.amax(data[:,1])*R - np.amin(data[:,1])*R,'z: ', np.amax(data[:,2])*R - np.amin(data[:,2])*R)
