import numpy as np

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


a, b, c, d, e, f, g = basic_test_cases()
# Target Location


def path_finder(area):
    b = area
    bs = [list(i) for i in area.split("\n")]
    arr = np.array(bs, dtype=int).reshape(len(bs), len(bs))
    # print(arr)
    climbs = 0
    # going along the edges = step-wise


    return arr  # total levels climbed

aa = path_finder(a)
print(f"a: 0\n{aa}\n{'*' * 72}")
bb = path_finder(b)
print(f"b: 2\n{bb}\n{'*' * 72}")
cc = path_finder(c)
print(f"c: 4\n{cc}\n{'*' * 72}")
dd = path_finder(d)
print(f"d: 42\n{dd}\n{'*' * 72}")
ee = path_finder(e)
print(f"e: 14\n{ee}\n{'*' * 72}")
ff = path_finder(f)
print(f"f: 0\n{ff}\n{'*' * 72}")
gg = path_finder(g)
print(f"g: 4\n{gg}\n{'*' * 72}")