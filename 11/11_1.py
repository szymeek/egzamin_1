import numpy as np
import matplotlib.pyplot as plt

# zestaw 11
# # prosty jeden wykres dwoch funkcji, zapis png
x = np.arange(0, 3 * np.pi, 0.1)
y1 = np.sin(2 * x)
y2 = (3 * x) - 5
y3 = 2 * (np.cos(x))
plt.plot(x, y1, 'g', label='y1', linestyle="-.")
plt.plot(x, y2, 'r', label='y2', linestyle="--")
plt.plot(x, y3, 'y', label='y3', linestyle=":")
plt.xlim(0, 3 * np.pi)

plt.title('tytul')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend(title='Legenda:')
plt.grid()
# plt.savefig('wykreszad1.png', format='png')

plt.show()
