import pandas as pd
import numpy as np
from itertools import combinations, permutations

file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)

df_data_tree = df[['plpln_dup', 'sku_dup', 'pscrtn_dup']]

date_ser = df.plaedt == df.psdlm
df_data_tree.insert(0, 'date_dup', date_ser)
df.insert(2, 'date_dup', date_ser)

# todo: goal: create a dataframe with unique combinations of the columns values
# number cols to ensure they remain ordered and create a reference for tracking changes
cols = df_data_tree.columns
cols_ordered = []
un_vals = []
num = 0
for col in cols:
    name = f"{num}_{col}"
    cols_ordered.append(name)
    un_vals.append(
        (name, f"length: {df_data_tree[col].nunique()}", (name, df_data_tree[col].unique().tolist()))
        )
    num += 1
df_data_tree.columns = cols_ordered

values_bool = [j[2] for j in un_vals]

# level_0 = str(values_bool[0][0])
# level_1 = [str(i) for i in values_bool[1]]
# level_2 = [str(i) for i in values_bool[2]]
# level_3 = [str(i) for i in values_bool[3]]




















# todo: goal2: print out the structure like a tree in the console