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
print(f"a: {a}")  # test.assert_equals(path_finder(a), 0)
print(f"b: {b}")  # test.assert_equals(path_finder(b), 2)
print(f"c: {c}")  # test.assert_equals(path_finder(c), 4)
print(f"d: {d}")  # test.assert_equals(path_finder(d), 42)
print(f"e: {e}")  # test.assert_equals(path_finder(e), 14)
print(f"f: {f}")  # test.assert_equals(path_finder(f), 0)
print(f"g: {g}")  # test.assert_equals(path_finder(g), 4)


def path_finder(area):
    return 0  # total levels climbed