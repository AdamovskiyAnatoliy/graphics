import numpy as np
import matplotlib.pyplot as plt

N = 150
r = 2 * np.random.rand(N)
theta1 = 2 * np.pi * np.random.rand(N)
area = 20 * r**2
colors = theta1

t = np.arange(0,4,0.01) 
theta2 = 2 * np.pi * t
t = np.cos(5*theta2)

ax1 = plt.subplot(211, projection='polar')
ax1.scatter(theta1, r, 
			c=colors,
			s=area, 
			cmap='Pastel1', 
			alpha=0.75)

ax2 = plt.subplot(212, projection='polar')
ax2.plot(theta2, t, c='r', label='Rose')

plt.legend()
plt.show()