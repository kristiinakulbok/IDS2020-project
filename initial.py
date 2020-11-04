import pandas as pd

df_white = pd.read_csv("winequality-white.csv", sep=";")
df_red = pd.read_csv("winequality-red.csv", sep=";")

print(df_white.head())
print(df_red.head())