import numpy as np
import matplotlib.pyplot as plt

# zestaw 2
# dwa slupkowe poziome wykresy obok siebie subplot, tytul, zapis jpg
width1 = [35, 45, 15, 40, 39]
bars = ('A', 'B', 'C', 'D', 'E')
x_pos = np.arange(len(bars))
plt.subplot(2, 2, 1)
plt.barh(x_pos, width1, color=['lightblue', 'pink', 'darkorange', 'gray', 'purple'])
plt.yticks(x_pos, bars)
plt.title('wykres lewy')


width2 = [-30, -32, -34, -33, -31]
plt.subplot(2, 2, 2)
plt.barh(x_pos, width2, color=['violet', 'darkturquoise', 'darkturquoise', 'brown', 'olive'])
plt.yticks(x_pos, bars)
# plt.gca().invert_xaxis()
# do odwracania wykrsow
plt.title('wykres prawy')

# zapis jpg
from PIL import Image
plt.savefig('plot.png')
im1 = Image.open('plot.png')
im1 = im1.convert('RGB')
im1.save('plot.jpg')

plt.show()
