import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dataframe na wykres slupkowy bez transpozycji, z indeksem w lewym gornym

# df = pd.read_excel('ceny1.xlsx', index_col=0)
df = pd.read_excel('mieszkania1.xlsx')

# grupa = df.groupby(['Formy budownictwa'])
# etykiety = list(grupa.groups.keys())

# print(grupa.groups)

# print(df.index)
# print(df.columns)

# df1 = df.loc[df['Formy budownictwa'] == 'indywidualne']
# to samo co nizej

# rozbicie na 3 ramki danych pogrupowane po formie budownictwa
df1 = df[df['Formy budownictwa'] == 'indywidualne']
df2 = df[df['Formy budownictwa'] == 'spółdzielcze']
df3 = df[df['Formy budownictwa'] == 'komunalne']

x = np.arange(0, len(df1))

plt.bar(x, df2["Wartość"], width=0.25, label='spółdzielcze', color='green')
plt.bar(x-0.25, df3["Wartość"], width=0.25, label='komunalne', color='blue')
plt.bar(x+0.25, df1["Wartość"], width=0.25, label='indywidualne', color='brown')

plt.legend(loc=7)
plt.title('Rodzaj formy budownictwa w poszczególnych latach')
plt.ylabel('Wartość')
plt.xlabel('Lata')
plt.xticks(x, df1['Rok'])
plt.text(-0.5, 65000, '114899')
# plt.annotate('114899', [-0.5, 65000])
plt.show()

