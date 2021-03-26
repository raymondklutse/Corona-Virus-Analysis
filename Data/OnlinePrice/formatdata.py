import pandas as pd
import numpy as np

filepath = "onlinepricechangesdataset.xlsx"
df = pd.read_excel(filepath, sheet_name='Indices')

sheet_name = df.columns[0]
header = df.iloc[1,:]
df.columns = header
df = df.iloc[2:,:].reset_index(drop=True)
#print(df.head())

#print(df.head().stack())

df_dates = df.iloc[:,2:].stack().reset_index()
df_dates.columns = ['Index','Date','Price']

df_items = df.iloc[:,[0,1]].reset_index()
df_items.columns = ['Index','Category','Item']

df_items['Category'] = df_items['Category'].apply(lambda x: np.NaN if x == " " else x)
df_items['Category']  = df_items['Category'].fillna(method='ffill')
print(df_items.head(10))


final_df = df_dates.merge(df_items,on = "Index", how="left").drop('Index', axis=1).dropna()
#print(final_df.head())

print(final_df.shape)
#final_df.to_csv("onlinepricechanges.csv")
