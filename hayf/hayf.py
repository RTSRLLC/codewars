import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file = "hayf_.xlsx"
df = pd.read_excel(file)

# forward fill df.year and change to df.year to int
df['year'] = df['year'].ffill()
df['year'] = df['year'].astype(int)

# Assuming df is your DataFrame and 'date' is the column of interest

# Forward fill missing values
df['date'] = df['date'].ffill()

# Convert the 'date' column to datetime, coercing errors into 'NaT'
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Fill 'NaT' values with a specific date (e.g., "1980-01-01")
specific_date = "1980-01-01"  # Modify as needed
df['date'] = df['date'].fillna(pd.to_datetime(specific_date))


# fill nan df.city and df.venue with 'unknown'
df['city'] = df['city'].fillna('unknown').astype(str)
df['venue'] = df['venue'].fillna('unknown').astype(str)

# fill face value with average of values around it and convert to float
for i in range(len(df['face value'])):
    if pd.isna(df['face value'].iloc[i]):
        # Calculate the mean of the last 3 non-NaN preceding values
        mean_val = df['face value'].iloc[max(0, i - 3):i].mean().round(2)
        df.at[i, 'face value'] = mean_val

df['face value'] = df['face value'].astype('float64')

# fill nan in df['anything written on ticket'] with 'nothing'
df['anything written on ticket'] = df['anything written on ticket'].fillna('nothing').astype(str)

# Replace all backslashes with nothing
df['anything written on ticket'] = df['anything written on ticket'].str.replace(r"\\", "")

# Replace erratic single quotes around commas and at the start/end of strings
df['anything written on ticket'] = (df['anything written on ticket']
                                    .str.replace(r"\'\,", "',").replace(r",\'",",'").str.strip("'\" "))

# Further strip spaces and double quotes
df['anything written on ticket'] = df['anything written on ticket'].str.strip()

# set index to the df.date column and sort asc
df = df.set_index(df['date'])
df = df.sort_index()

# write to excel
file = 'updated_hayf.xlsx'
df.to_excel(file)


