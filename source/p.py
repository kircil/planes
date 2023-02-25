import pandas as pd
import numpy as np

df0 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_0.csv')
df1 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_1.csv')
df2 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_2.csv')
df3 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_3.csv')
df4 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_4.csv')
df5 = pd.read_csv('/Users/aviator172rr/Desktop/planes/input/fuel_efficiency_5.csv')
df = pd.concat([df0, df1, df2, df3, df4, df5])

print(df.iloc[4])