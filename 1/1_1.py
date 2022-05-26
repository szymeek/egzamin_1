import numpy as np
import matplotlib.pyplot as plt

# sin i cos klasyczny, subplots dwa na jednym, rozna skala na osi y
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
x = np.arange(0, 5, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

ax1.plot(x, y1, 'r', label='sin(x)', linestyle="-")
ax1.set_ylim(-1, 1)
ax1.set_ylabel('os lewa', color='green')
ax1.set_xlabel('os dolna')
ax1.legend(loc='right')
# pierwsza_legenda = ax1.legend(loc='upper right')
# ax1.add_artist(pierwsza_legenda)

ax2.plot(x, y2, 'g', label='cos(x)', linestyle=":")
ax2.set_ylim(-2, 2)
ax2.set_ylabel('os prawa', color='red')
ax2.legend(loc='lower center')

plt.xlim(0, 5)
plt.title('tytul')
fig.tight_layout()

plt.show()
