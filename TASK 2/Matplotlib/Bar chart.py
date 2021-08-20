from matplotlib import pyplot as plt
import numpy as np
plt.style.use('seaborn')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  #ages on x axis

x_indexes= np.arange(len(ages_x))
width=0.25

dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752] #median salaries on y axis

py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

#plt.plot(ages_x, py_dev_y,label='Python')
plt.bar(x_indexes - width, py_dev_y,width=width, label='Python')

#plt.plot(ages_x, js_dev_y ,label='JavaScript')
plt.bar(x_indexes + width, js_dev_y,width=width, label='JavaScript')

#plt.plot(ages_x, dev_y,color='#444444',linestyle='--',label='All Devs')
plt.bar(x_indexes, dev_y, color='#444444',width=width , label='All Devs') #for bar charts

plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

leg=plt.legend();

plt.tight_layout()

plt.grid(True)

plt.show()
plt.savefig('plot.png')