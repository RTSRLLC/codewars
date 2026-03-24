import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from multiprocessing.connection import default_family

from pandas.core.config_init import performance_warnings


def address_creation(df: list):
    """ create the tree address needed for the tree structure. """

    def node_identification(df_: pd.DataFrame) -> dict:
        """ get unique values in duplicated columns for future Node class creation """
        # id dup cols  ... must be in order ... i believe they will be since it iterates left to
        # right
        cols = [i for i in df_.columns if '_dup' in i]

        # get unique vals in dup cols for class Node
        nodes = {}  # [(1, [False]), (2, [False, True]), (3, [False, True]), (4, [False, True])]
        num = 1
        for col in cols:
            d = sorted(df_[col].unique())  # sorted ensures False come before True
            nodes[str(num)] = {"node_val": d, "num_values": len(d)}
            num += 1

        return nodes

    def number_needed_levels(n: int) -> list:
        """ generate the needed tree levels. all trees start with top node and branch out
         with factor n * 2 for the number of needed levels. """
        levels = [1, 2]
        for y in range(1, n - 1):
            levels.append(levels[y] * 2)
        return enumerate(levels, start=1)

    # extract T/F values for tree creation
    nodes_2_be = node_identification(df)

    # get how many nodes will be each level
    len_nodes_2_be = len(nodes_2_be)
    num_levels_nodes = number_needed_levels(n=len_nodes_2_be)

    addresses = []
    for level, nodes in num_levels_nodes:
        needed = [None] * nodes
        for i in range(len(needed)):
            needed[i] = int(str(level) + str(i + 1))
        addresses.append(needed)

    return addresses, nodes_2_be


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
    parent_add: int = None
    child_add: dict = field(default_factory=dict)  # {"left": None, "right": None}
    l_marg_dist: int = 0


addresses_4_tree, nodes_2_be = address_creation(df)


# node tree prep
def make_tree(addresses: list, node_vals: dict)-> dict:
    """
    create a concise dict with keys = addresses in tree and values =
    """
    nodes_2_be_zip = [i.get('node_val') for i in node_vals.values()]
    node_vals = list(zip(addresses, nodes_2_be_zip))

    node_vals_copy = node_vals.copy()
    tree = {}
    for item in node_vals_copy:  # is a tuple
        length = len(item[0])
        if length == 1:
            tree[item[0][0]] = Node(node_val=item[1][0], node_address=item[0][0], parent_add=None)
        elif length == 2:
            zip_ = list(zip(item[0], item[1]))
            for z in zip_:
                tree[z[0]] = Node(node_val=z[1], node_address=z[0], parent_add=-1)
        else:
            # make F, T same length as addresses
            tree_valz = item[1] * 2
            zip_ = list(zip(item[0], tree_valz))
            for z in zip_:
                tree[z[0]] = Node(node_val=z[1], node_address=z[0], parent_add=-1)


            stop = ''

        # tree[add] = branches

    return tree


tree  = make_tree(addresses_4_tree, nodes_2_be)

# todo: doing parents and children in another function