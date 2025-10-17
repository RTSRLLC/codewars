import numpy as np
from itertools import product

"""
To find the minimal number of climb rounds (i.e., the minimum sum of absolute altitude differences along the path), 
you need to model the grid as a graph where each cell is a node, edges connect to adjacent cells in all four cardinal directions (North, East, South, West), 
and edge weights are the |altitude differences|. Then, use a shortest-path algorithm like Dijkstra's to compute the minimum-cost path from [0,0] to [N-1, N-1], 
as this accounts for any beneficial moves, including left or up, without restricting direction.
"""


def basic_test_cases():
    a = "\n".join([
        "000",
        "000",
        "000"
    ])  # test.assert_equals(path_finder(a), 0)

    b = "\n".join([
        "010",
        "010",
        "010"
    ])  # test.assert_equals(path_finder(b), 2)

    c = "\n".join([
        "010",
        "101",
        "010"
    ])  # test.assert_equals(path_finder(c), 4)

    d = "\n".join([
        "0707",
        "7070",
        "0707",
        "7070"
    ])  # test.assert_equals(path_finder(d), 42)

    e = "\n".join([
        "700000",
        "077770",
        "077770",
        "077770",
        "077770",
        "000007"
    ])  # test.assert_equals(path_finder(e), 14)

    f = "\n".join([
        "777000",
        "007000",
        "007000",
        "007000",
        "007000",
        "007777"
    ])  # test.assert_equals(path_finder(f), 0)

    g = "\n".join([
        "000000",
        "000000",
        "000000",
        "000010",
        "000109",
        "001010"
    ])  # test.assert_equals(path_finder(g), 4)

    return a, b, c, d, e, f, g


a_, b_, c_, d_, e_, f_, g_ = basic_test_cases()


def get_og_string(arr: list, length: int) -> tuple:
    arr_flat = list(arr.flatten())
    for i in range(length, length * length, length + 1):
        arr_flat.insert(i, '\n', )
    arr_flat = [str(i) for i in arr_flat]
    print(arr.shape)
    print(arr_flat)
    return arr.shape


def get_arr_addresses(arr: list, length: int) -> dict:
    iter_lst = [i for i in range(length)]
    indices = list(product(iter_lst, repeat=2))
    length_indices = len(indices)
    arr_values = []
    temp_arr = []
    for i in range(length_indices):
        vals = indices[i]
        k = str(vals[0]) + str(vals[1])
        v = str(arr[vals[0], vals[1]])
        temp_arr.append(','.join([k, v]))
    return np.array(temp_arr).reshape(int(np.sqrt(length_indices)), int(np.sqrt(length_indices)))


def reshape_vals_addresses(arr, length: int) -> list:
    addresses_flat = arr.flatten()

    arr_top = []
    arr_bottom = []
    for address in addresses_flat:
        ls = address.split(',')
        ls[1] = int(ls[1])
        arr_top.append(ls[0])
        arr_bottom.append(ls[1])

    arr_tp = np.array(arr_top).reshape(length, length)
    arr_bt = np.array(arr_bottom).reshape(length, length)
    arr_together = np.concatenate((arr_tp, arr_bt)).reshape(-1, length, length)
    return arr_together


def path_finder(area):
    area_list = [list(i) for i in area.split("\n")]
    bs_len = len(area_list)

    arr = np.array(area_list, dtype=int).reshape(bs_len, bs_len)
    arr_flat = list(arr.flatten())

    addresses = get_arr_addresses(arr, bs_len)
    addresses = reshape_vals_addresses(addresses, bs_len)

    # test = get_og_string(arr, bs_len)
    if np.sum(arr) == 0:
        return 0

    class Node:
        def __init__(self, arr):
            # self.arr = arr
            self.arr = arr
            self.bs_len = arr.shape[1]
            self.addresses = self.arr[0]
            self.values = self.arr[1].astype(int)
            self.nodes = dict(zip(self.addresses.flatten(), self.values.flatten()))
            self.tree = {}

        def available_directions(self):
            # ['00', '01', '02', '10', '11', '12', '20', '21', '22']
            # [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
            # {00: 0, 01: 1, 02: 0, 10: 1, 11: 0, 12: 1, 20: 0, 21: 1, 22: 0}
            # todo: a diagonal move is where both values increase/decrease by 1
            for k, v in self.nodes.items():
                zero, one = int(k[0]), int(k[1])
                zero_minus_1 = zero - 1
                one_plus_1 = one + 1
                zero_plus_1 = zero + 1
                one_minus_1 = one - 1
                N, E, S, W = self.directions(zero_minus_1, one_plus_1, zero_plus_1, one_minus_1, self.bs_len - 1)
                self.tree[k] = (N, E, S, W, v)

            return self.tree,self.values

        def directions(self, zm1: int, op1: int, zp1: int, om1: int, length: int):
            if zm1 < 0 or zm1 > length:
                n = None
            else:
                n = self.values[0 - 1, 1]
            if op1 < 0 or op1 > length:
                e = None
            else:
                e = self.values[0, 1 + 1]
            if zp1 < 0 or zp1 > length:
                s = None
            else:
                s = self.values[0 + 1, 1]
            if om1 < 0 or om1 > length:
                w = None
            else:
                w = self.values[0, 1 - 1]
            return n, e, s, w

    tree, vals = Node(addresses).available_directions()

    return tree, vals



# a = path_finder(a_)
# b = path_finder(b_)
# c = path_finder(c_)
# d = path_finder(d_)
# e = path_finder(e_)
# f = path_finder(f_)
# g = path_finder(g_)
# h = path_finder('9')  # , 0)
# i = path_finder('00\n59')  # , 9)
# j = path_finder('443\n622\n342')  # , 2)
# k = path_finder('1748\n3363\n3280\n0941')  # , 12)
# l = path_finder('09547\n18022\n16498\n35390\n91527')  # , 17)
# m = path_finder('435299\n292595\n494834\n978378\n339644\n015652')  # , 18)
n, vals_n = path_finder('3616870\n4431668\n4523080\n2748996\n8417245\n0953760\n9744257')  # , 20)
# o = path_finder('75364185\n66365903\n81031340\n60071146\n32658917\n15612476\n03512461\n09121077')  # , 22)
# p = path_finder('921512262\n073757004\n591992692\n711729536\n944738532\n740436140\n259226763\n624323214\n085117161')  # , 32)
# q = path_finder('5736466929\n8422663712\n6717662320\n2050556352\n1208418537\n3846948554\n0736303096\n0737050025\n3835791347\n6062559101')  # , 30)
# r = path_finder('45528081661\n88622773986\n17444154736\n11717290525\n47172210354\n09831904008\n60674793342\n56190958822\n80638279343\n55224665968\n60321088764')  # , 24)
# s = path_finder('092158983775\n282369592936\n652460767036\n647041461643\n881083979874\n081990597155\n060078506934\n284703957557\n393772671318\n041581032822\n877612523318\n450481712521')  # , 35)
# t = path_finder('4076390941965\n8838398866436\n1770111200297\n9369375707100\n7347601401344\n3969216683905\n8345069535192\n8051547548370\n1439668837856\n3993915787436\n4755139506265\n4431682647927\n7044750419779')  # , 33)
# u = path_finder('26123923976121\n41230567257124\n56656453868372\n57264482617208\n59487358016952\n79957518597542\n00855390033477\n15756964394626\n62200210535437\n65717734838667\n62363952695719\n84397086821770\n18269568382152\n28766969660573')  # , 37)
# v = path_finder('163524713265638\n671023336692281\n812486815651333\n427879130821023\n627519540045131\n225593570343566\n312238694164715\n579272481215212\n652886046544093\n694392047499170\n972056930148993\n764392039477627\n778566271863140\n219830938415775\n400463109825434')  # , 43)
# w = path_finder('6193202055400530\n2978951088421870\n1728788075740422\n3493353571281571\n5883832600934582\n6764879319684399\n3951323591165362\n8924356397569809\n4337198721574525\n4300839837867718\n5973367290217580\n3615559832783305\n7060237376310028\n6227063147681060\n3808906527826590\n5026928259417646')  # , 52)
# x = path_finder('91496021559669533\n81904367165372127\n76048945740163189\n97886868015673102\n47444790399445531\n76600261325220918\n86056540450767230\n75775683513771778\n15821885439235017\n36381134658388347\n02180477168680494\n29186437643013438\n75509140379701291\n02540851779711001\n66728206731789413\n59495725692790157\n98502239391643830')  # , 133)