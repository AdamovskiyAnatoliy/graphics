import matplotlib.pyplot as plt
import numpy as np 
"""
import csv

x = []
y = []

with open('exampel.txt', 'r') as csvfile:
	plots = csv.reader(csvfile, delimier=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))


plt.plot(x,y, label='Loaded from file')
"""

x, y = np.loadtxt('exampel.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from file')


plt.xlabel('x')
plt.ylabel('y')

plt.title('Intersting Graph\nCheck it out')
plt.legend()

plt.show() 