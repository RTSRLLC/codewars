from multiprocessing.connection import default_family

import pandas as pd
import numpy as np
from itertools import combinations, permutations
import warnings
from dataclasses import dataclass, field

from pandas.core.config_init import performance_warnings


def node_identification(df: pd.DataFrame) -> dict:
    """ get unique values in duplicated columns for future Node class creation """
    # id dup cols  ... must be in order ... i believe they will be since it iterates left to right
    cols = [i for i in df.columns if '_dup' in i]

    # get unique vals in dup cols for class Node
    nodes = {}  # [(1, [False]), (2, [False, True]), (3, [False, True]), (4, [False, True])]
    num = 1
    for col in cols:
        d = sorted(df[col].unique())  # sorted ensures False come before True
        nodes[str(num)] = {"node_val": d, "num_values": len(d)}
        num += 1
    return nodes


# 1 open df
file = '/Users/jshensley/Desktop/PycharmProjects/codewars/input_files/create_tree_python.xlsx'
df = pd.read_excel(file)

# 2 create date dup column...there are already other dup cols from source
df.insert(2, 'date_dup', df.plaedt == df.psdlm)


@dataclass
class Node:
    """
    A bool class representing a node in the tree structure.
    Attributes:
        node_val: boolean, True or False
        node_address: (num 1, num 2) =- (tree level, level position). 1 = top-most parent.
            34 = 3 levels down, 4th node from left.
        parent_add: address of parent if exists. if no parent, None.
        child_add: follows same formula as above if there are children. If bottom level, is None.
        l_marg_dist: int
    """
    node_val: bool
    node_address: int
    parent_add: int
    child_add: dict = field(default_factory=dict)  # {"left": None, "right": None}
    l_marg_dist: int = 0


nodes_2_be = node_identification(df)

# {0: {'Node': [False], 'num_values': 1}, 1: {'Node': [False, True], 'num_values': 2},
# 2: {'Node': [False, True], 'num_values': 2}, 3: {'Node': [False, True], 'num_values': 2}}

tree = {}
address = ''
for level, node_2_be in nodes_2_be.items():
    address = level
    curr_node = node_2_be.get('node_val')
    num_nodes = node_2_be.get('num_values')

    for b in range(1, len(curr_node) + 1):
        address += str(b)
        if not tree:
            node_address = int(address)
            node_new = Node(node_val=curr_node[int(b - 1)], node_address=node_address, parent_add=node_address)
            tree[node_address] = node_new

        else:





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