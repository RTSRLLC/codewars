import pandas as pd
import numpy as np
from itertools import combinations, permutations
import warnings

from pandas.core.config_init import performance_warnings

file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)
df.insert(2, 'date_dup', df.plaedt == df.psdlm)

# todo: goal: create a dataframe with unique combinations of the columns values
cols = ['plaedt', 'psdlm', 'date_dup', 'plpln', 'plpln_dup', 'sku', 'sku_dup','pscrtn', 'pscrtn_dup']
un1_date = df.date_dup.unique().tolist()
un2_plpln = df.plpln_dup.unique().tolist()
un3_sku_dup = df.sku_dup.unique().tolist()
un4_pscrtn_dup = df.pscrtn_dup.unique().tolist()

d = {
    1: [False, False, False, False],
    2: [False, False, False, True],

    3: [False, False, True, False],
    4: [False, False, True, True],

    5: [False, True, False, False],
    6: [False, True, False, True],
    7: [False, True, True, False],
    8: [False, True, True, True],
    }

tree = {}
start = False
length = 4


# keep track of index




# todo: goal2: print out the structure like a tree in the console