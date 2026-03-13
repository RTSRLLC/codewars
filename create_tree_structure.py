import pandas as pd
import numpy as np

file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)

df_data_tree = df[['plpln_dup','sku_dup','pscrtn_dup']]

date_ser = df.plaedt == df.psdlm
df_data_tree.insert(0, 'date_dup', date_ser)

# todo: goal: create a dataframe with unique combinations of the columns values
cols = df_data_tree.columns
cols_ordered = []
un_vals = []
num = 0
for col in cols:
    name = f"{num}_{col}"
    cols_ordered.append(name)
    un_vals.append(
        (name, f"length: {df_data_tree[col].nunique()}", f"vals: {df_data_tree[col].unique()}")
        )
    num += 1

df_data_tree.columns = cols_ordered










# todo: goal2: print out the structure like a tree in the console