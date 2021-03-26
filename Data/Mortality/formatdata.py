import pandas as pd
import numpy as np

filepath = "deaths_registered.xlsx"
df = pd.read_excel(filepath)
print(df.head(10))
df = df.iloc[5:,:].reset_index(drop=True)
df.columns = df.iloc[0,:]
df = df.iloc[1:,:].reset_index(drop=True)
df.columns = ['Year','Week_no','Deaths_except_COVID19','All_deaths_5_year_avg','Deaths_COVID']

print(type((df.iloc[0,0])))
df = df[df['Year'].isin([2020,2021])]
print(df.head())
df.reset_index(drop=True).to_csv("deaths_registered_cleaned.csv")
