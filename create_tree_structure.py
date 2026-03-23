from multiprocessing.connection import default_family

import pandas as pd
import numpy as np
from itertools import combinations, permutations
import warnings
from dataclasses import dataclass, field

from pandas.core.config_init import performance_warnings

# 1 open df
file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)

# 2 create date dup column...there are already other dup cols from source
df.insert(2, 'date_dup', df.plaedt == df.psdlm)

# id dup cols  ... must be in order ... i believe they will be since it iterates left to right
cols = [i for i in df.columns if '_dup' in i]

# get unique vals in dup cols for class Node
nodes = {}  # [(1, [False]), (2, [False, True]), (3, [False, True]), (4, [False, True])]
num = 0
for col in cols:
    d = df[col].unique().tolist()
    nodes[num] = {"node_val": d, "num_values": len(d)}
    num += 1


@dataclass
class Node:
    """
    A bool class representing a node in the tree structure.
    Args:
        node_val: boolean, True or False
        node_address: int, first digit = tree level, 0 being parent, additional digits = number
        of lines from left margin
        parent: Node, the parent of this node
        children: dict, a dictionary that maps child nodes to their children using node_address

    """
    node_val: bool
    node_address: int
    parent_address: int
    children_addresses: dict = field(default_factory=dict)  # {"left": None, "right": None}


# {0: {'Node': [False], 'num_values': 1}, 1: {'Node': [False, True], 'num_values': 2},
# 2: {'Node': [False, True], 'num_values': 2}, 3: {'Node': [False, True], 'num_values': 2}}
tree = {}
for node in nodes:
    curr_node = nodes.get(node)
    val = curr_node.get('node_val')
    stop = ''

# number of leaves = 8

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