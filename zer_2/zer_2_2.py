import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# df = pd.read_excel('ceny1.xlsx', index_col=0)
df = pd.read_excel('ceny1.xlsx')

# print(df.columns)

# print(df)

# print(df['Rok'])

# rozbicie ramki danych na 2  po wartosci w kolumnie
df1 = df.loc[df['Rodzaje towarów'] == "ryż - za 1kg"]
# print(df1)

df2 = df.loc[df['Rodzaje towarów'] == "mąka pszenna - za 1kg"]
# print(df2)

plt.plot(df1['Rok'], df1['Wartość'], 'r', label='ryż', linestyle="--")
plt.plot(df2['Rok'], df2['Wartość'], 'g', label='mąka', linestyle=":")

# plt.annotate('114899', xy=(2011, 4))
# annotate podpisuje dane na wykresie, w miejscu NA WYKRESIE x i y
plt.text(2011, 4, '114899')
# text podobnie, inna skladnia
plt.legend(title='Legenda:')
plt.xlim(2010, 2019)
plt.show()
