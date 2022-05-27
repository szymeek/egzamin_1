import numpy as np
import matplotlib.pyplot as plt

# zestaw 4
# # prosty wykres x3 liniowy, legenda
x = np.arange(-7, 7, 0.1)
y1 = 20 * np.sin(x)
y2 = ((2 * x) / 5) - 2
y3 = 7 - x
plt.plot(x, y1, 'r', label='20*sin(x)', linestyle="--")
plt.plot(x, y2, 'y', label='2x/5-2', linestyle="--")
plt.plot(x, y3, 'g', label='7-x', linestyle="-")
plt.xlim(-7.9, 7.9)
plt.ylim(-30, 30)

plt.title('tytul ABCD')
# plt.xlabel('x label')
# plt.ylabel('y label')
plt.legend(title='Legenda:', loc='lower left')
# plt.grid()


plt.show()

