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
    for i in range(length_indices):
        vals = indices[i]
        if i == 0:
            k = 'start'
        elif i == length_indices - 1:
            k = 'end'
        else:
            k = str(vals[0]) + str(vals[1])
        v = arr[vals[0], vals[1]]
        arr_values.append((k, v))
    return arr_values


def path_finder(area):
    b = area
    bs = [list(i) for i in area.split("\n")]
    bs_len = len(bs)
    arr = np.array(bs, dtype=int).reshape(bs_len, bs_len)
    arr_flat = list(arr.flatten())
    # test = get_og_string(arr, bs_len)
    if np.sum(arr) == 0:
        return 0

    addresses = get_arr_addresses(arr, bs_len)

    class Node:
        def __init__(self, value, position):
            self.value = value
            self.position = position
            # self.north = north
            # self.east = position
            # self.south = south
            # self.west = west
            self.choices = []

        def available_directions(self):
            pass

    tree = {}
    for add in addresses:
        tree[add[0]] = Node(add[1], add[0])

    climbs = 0
    score = 0
    current_location = None
    previous_location = None
    next_loc_choices = None

    stop = ''

    return arr


# a = path_finder(a_)
# b = path_finder(b_)
c = path_finder(c_)
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
# n = path_finder('3616870\n4431668\n4523080\n2748996\n8417245\n0953760\n9744257')  # , 20)
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

directions = [
    # 'start',
    'left+1, right=uc',
    'left=uc, right+1',
    # 01=
    'left=uc, right-1',
    'left+1, right=uc',
    'left=uc, right+1',
    # 02=
    'left=uc, right-1',
    'left=uc, right+1',
    # 1,0=
    'left-1, right=uc',
    'left+1, right=uc',
    'left=uc, right+1',
    # 1,1=
    'left-1, right=uc',
    'left=uc, right-1',
    'left=uc, right+1',
    'left=1, right=uc',
    # 1,2=
    'left-1, right=uc',
    'left=uc, right-1',
    'left+1, right=uc',
    # 2,0=
    'left-1, right=uc',
    'left=uc, right+1',
    # 2,1=
    'left-1, right=uc',
    'left=uc, right-1',
    'left=uc, right+1'
]

set_directions = set(directions)

moves_possible = [('uc', 0), ('-1', lambda x: x - 1), ('+1', lambda x: x + 1)]











    stopp = ''