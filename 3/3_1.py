import numpy as np
import matplotlib.pyplot as plt

# zestaw 3
# dwa barh odwrotnie obok siebie horyzontalnie subplotSSS
width1 = [-35, -20, -50, -30, -40]
width2 = [37, 37, 40, 33, 36]
bars = ('A', 'B', 'C', 'D', 'E')
x_pos = np.arange(len(bars))

fig, (ax1, ax2) = plt.subplots(1, 2)
# storzenie figury, w niej 2 ploty, mozna sie odnisic po ax[0, 0] albo ax[0] albo stworzyc zmienna

ax1.barh(x_pos, width1, color=['lime', 'gold', 'blue', 'mediumpurple', 'indianred'])
# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)')
ax1.set_title('wykres 1')
# ax1.set_xlim(-52, 0)
# ax1.set_xticks([-50, 0])
ax1.set_xticks(np.arange(-50, 1, step=10))
# -50 do 1 bo przedział prawostronnie domkniety

ax2.barh(x_pos, width2, color=['yellowgreen', 'mediumslateblue', 'orange', 'green', 'yellowgreen'])
# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x)')
ax2.set_title('wykres 2')

plt.show()
