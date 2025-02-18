import pandas as pd
import numpy as np
pd.set_option('future.no_silent_downcasting', True)

file_appt = '/Users/jshensley/Desktop/codewars/DFY_Analysis/appointment-reporting-2025-02-04_17-27-48.csv'
file_attr = '/Users/jshensley/Desktop/codewars/DFY_Analysis/attribution-reporting-2025-02-04_17-31-24.csv'
file_call = '/Users/jshensley/Desktop/codewars/DFY_Analysis/call-reporting-2025-02-04_17-29-59.csv'



df_call = pd.read_csv(file_call)
df_call.astype(str)
df_call = df_call.apply(lambda x: x.astype(str).str.strip().replace('-', np.nan))
df_call = df_call.replace('', np.nan)
df_call = df_call.dropna(axis=1, how='all')
df_call['Contact Phone'] = df_call['Contact Phone'].apply(lambda x: x[1:4])
contact_phone_group = df_call.groupby('Contact Phone')['Contact Phone'].count().sort_values(ascending=False)
contact_name_group = df_call.groupby(['Contact Name', 'Call Status'])['Contact Name'].count().sort_values(ascending=False)

unique_marketing_campaign = df_call['Marketing Campaign'].unique()
unique_call_status = df_call['Call Status'].unique()

df_appt = pd.read_csv(file_appt)




df_attr = pd.read_csv(file_attr)
