import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('turystyka1.xlsx', header=None)
print(df)
df1 = df.transpose()
print(df1)
