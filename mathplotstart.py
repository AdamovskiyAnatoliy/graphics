from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# x, y, z = axes3d.get_test_data()

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(np.abs(x**3 + y**3)))

surf = ax1.plot_surface(x, y, z,
						cmap=cm.coolwarm,
                       	linewidth=0, 
                       	antialiased=False,
                       	alpha=0.3)
fig.colorbar(surf, shrink=0.5, aspect=5)

# cset = ax1.contourf(x, y, z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax1.contourf(x, y, z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax1.contourf(x, y, z, zdir='y', offset=40, cmap=cm.coolwarm)

# cset = ax1.contour(x, y, z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax1.contour(x, y, z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax1.contour(x, y, z, zdir='y', offset=40, cmap=cm.coolwarm)


ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()