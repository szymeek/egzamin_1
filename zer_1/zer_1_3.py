import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('turystyka1.xlsx', header=None)
# print(df)
dfT = df.transpose()
print(dfT)
print(dfT.columns)
dfT.columns = ['kategoria hotelu', 'rok', 'ilosc']
print(dfT['kategoria hotelu'].unique())
df1 = dfT[dfT['rok'] == '2015']
df2 = dfT[dfT['rok'] == '2018']
labels1 = df1['kategoria hotelu']
sizes1 = df1['ilosc']
labels2 = df2['kategoria hotelu']
sizes2 = df2['ilosc']

# figsize - ustawienie wymiaru
fig, (ax1, ax2) = plt.subplots(2, figsize=(10, 10))
# wykres 1
ax1.pie(sizes1.values, labels=labels1, autopct='%1.1f%%', textprops={'size': 'smaller'})
# textprops - wymiar podpisow
ax1.set_title('rok 2015')
# ax1.legend()


# wykres 2
ax2.pie(sizes2.values, labels=labels2, autopct='%1.1f%%', textprops={'size': 'smaller'})
ax2.set_title('rok 2018')
# ax2.legend()

plt.show()
