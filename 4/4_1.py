import numpy as np
import matplotlib.pyplot as plt

# zestaw 4
# # prosty jeden wykres dwoch funkcji, zpis pdf
x = np.arange(-5, 5, 0.1)
y1 = -(x ** 3) + (3*x) - 7
y2 = (4 * x) + 6
y3 = 6 + (4 * (x ** 3))
plt.plot(x, y1, 'g', label='y1', linestyle="-.")
plt.plot(x, y2, 'r', label='y2', linestyle="--")
plt.plot(x, y3, 'y', label='y3', linestyle=":")
plt.xlim(-5, 5)

plt.title('tytul')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend(title='Legenda:')
plt.grid()
# plt.savefig('wykreszad1.pdf',format='pdf')

plt.show()

