import pandas as pd
import numpy as np

filepath = "infections.xlsx"
df_England = pd.read_excel(filepath,'1f').iloc[4:,:].reset_index(drop=True)
df_Wales = pd.read_excel(filepath,'2e').iloc[4:,:].reset_index(drop=True)
df_Nothern_Ireland = pd.read_excel(filepath,'3e').iloc[4:,:].reset_index(drop=True)
df_Scotland = pd.read_excel(filepath,'4e').iloc[4:,:].reset_index(drop=True)


def process_data(df,country):
    df_Males = df.iloc[2:9,[2,3,6]].reset_index(drop=True)
    df_Males.columns = ["Age_Band","Estimated_Percentage_People","Num_Infections"]
    df_Males['Sex']  = "Male"
    

    df_Females = df.iloc[2:9,[2,15,18]].reset_index(drop=True)
    df_Females.columns = ["Age_Band","Estimated_Percentage_People","Num_Infections"]
    df_Females['Sex']  = "Female"

    result = df_Males.append(df_Females)
    result['Country']  = country

    return result

df_England_processed = process_data(df_England,"England")
df_Wales_processed = process_data(df_Wales,"Wales")
df_Nothern_Ireland_processed = process_data(df_Nothern_Ireland,"Nothern_Ireland")
df_Scotland_processed = process_data(df_Scotland,"Scotland")

df_England_processed = process_data(df_England,"England")
dataframes = [df_England_processed,df_Wales_processed,df_Nothern_Ireland_processed,df_Scotland_processed]
final_df = pd.concat(dataframes).reset_index(drop=True).dropna()

print(final_df)

final_df.to_csv("infections_by_country_age_and_sex.csv")
