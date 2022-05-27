import numpy as np
import matplotlib.pyplot as plt

# slupkowy 2 na 1 z linia pozioma i kolorami

N = 5

first = (20, 10, 30, 7, 50)
second = (80, 55, 40, 15, 0)
# x = np.arange(0, 5, 0.1)
# y = 120
ind = np.arange(N)
# width = 0.35
width = 0.8

plt.bar(ind, first, width, color=['purple', 'skyblue', 'olive', 'dodgerblue', 'lime'], label="first")
plt.bar(ind, second, width, bottom=first, color=['teal', 'darkgreen', 'khaki', 'lightpink'], label="second")
# plt.plot(x, y, 'r')

# plt.ylabel('Contribution')
# plt.title('Contribution by the teams')
# plt.xticks(ind)
# plt.xticks(ind, ('T1', 'T2', 'T3', 'T4', 'T5'))

plt.hlines(y=120, xmin=0.0, xmax=4.8, color='g')

plt.yticks(np.arange(0, 141, 20))
# plt.legend()
plt.xlim(-0.8, 5.2)
plt.ylim(0, 150)
plt.title('tytul')
plt.show()
