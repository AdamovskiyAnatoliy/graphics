import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 3]

x2 = [1, 2, 3]
y2 = [6, 3, 7]

plt.plot(x, y, label='First line')
plt.plot(x2, y2, label='Second line')

plt.xlabel('Plot Number')
plt.ylabel('Importent var')

plt.title('Intersting Graph\nCheck it out')
plt.legend()

plt.show()