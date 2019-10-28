import matplotlib.pyplot as plt

import numpy as np

data = np.loadtxt('stockholm_td_adj.txt', dtype=float)

month = data[data[:, 1] == int(input())]

weather_info = np.column_stack((month[:, 0],month[:, 1], month[:, 2], np.sum(month[:, 3:6], axis = 1)/3))

temp = np.array([[i, np.amin(weather_info[weather_info[:, 2] == i], axis = 0)[3], np.amax(weather_info[weather_info[:, 2] == i], axis = 0)[3], sum(weather_info[weather_info[:, 2] == i][:, 3])/weather_info[weather_info[:, 2] == i].shape[0]] for i in range(1, 31)])


my_plot = plt.plot(temp[:, 0], temp[:, 1:], '-')

plt.setp(my_plot[0],linewidth=4, linestyle = '--')
plt.setp(my_plot[1],  linewidth=2, linestyle = 'dotted')
plt.setp(my_plot[2], markersize=10, linestyle = 'dashdot')

plt.title('temperature in Stockholm')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.xticks(np.arange(1, 31, 1))
plt.legend(('min', 'max', 'mean'), loc = 'upper right')

plt.show(my_plot)
