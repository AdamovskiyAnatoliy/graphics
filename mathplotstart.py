import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10, 10, 0.1)

plt.figure(1)
plt.subplot(211)
plt.plot(t, t, 'r--', t, t**2, t, t**3)
plt.axis([-10, 10, -100, 100])
plt.xlabel("X cordenat 1 graf")
plt.ylabel("Y cordent 1 graf")
plt.grid(True)

plt.subplot(212)
plt.plot(t, np.sin(t))
plt.xlabel("X cordenat 2 graf")
plt.ylabel("Y cordent 2 graf")
plt.grid(True)

plt.show()