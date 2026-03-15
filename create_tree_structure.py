import pandas as pd
import numpy as np
from itertools import combinations, permutations
import warnings

from pandas.core.config_init import performance_warnings

# 1 open df
file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)

# 2 create dup columns
df.insert(2, 'date_dup', df.plaedt == df.psdlm)

# id dup cols
cols = [i for i in df.columns if '_dup' in i]

# get unique vals in col
nodes = []  # [(1, [False]), (2, [False, True]), (3, [False, True]), (4, [False, True])]
num = 1
for col in cols:
    d = df[col].unique().tolist()
    nodes.append((str(num), d, len(d)))
    num += 1

# determine number of possibilities but I don't think it matters if first node is 1 or 2 in length
# formula: if there is a single val in parent node,
# number of children nodes is:
# (number_cols ^ 2) /2
# if there is a binary parent node:
# then number_cols ^ 2
length = [i[2] for i in nodes]
tree_formula = (len(length) ** 2) / 2 if length[0] == 1 else len(length) ** 2

# tree: [('1', [False], 1), ('2', [False, True], 2), ('3', [False, True], 2), ('4', [False, True], 2)]
for node in nodes:

    stop = ''

# so number of leaves = 8

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

single_start = [(1, False), (2, [True, False]), (3, [True, False]), (4, [True, False])]
single_dict = {}

multi_start = [(1, [True, False]), (2, [True, False]), (3, [True, False]), (4, [True, False])]
multi_dict = {}
# keep track of index