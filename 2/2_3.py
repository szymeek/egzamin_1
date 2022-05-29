import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# od ziomeczka
df = pd.read_csv('nieruchomosci2.csv', delimiter=';', header=None)
dfT = df.transpose()

dfTT = dfT.reset_index()
dfTT.drop(axis=1, columns='index', inplace=True)

dfTT.columns = ['opis', 'metraz', 'rok', 'cena']
print(dfTT)


# moje
dff = pd.read_csv('nieruchomosci2.csv', delimiter=';', header=None)
dffT = dff.transpose()
dffT.columns = ['opis', 'metraz', 'rok', 'cena']
