def basic_test_cases():
    a = ("\n".join([
      "000",
      "000",
      "000"
    ]), 0)  # test.assert_equals(path_finder(a), 0)

    b = ("\n".join([
      "010",
      "010",
      "010"
    ]), 2)  # test.assert_equals(path_finder(b), 2)

    c = ("\n".join([
      "010",
      "101",
      "010"
    ]), 4)  # test.assert_equals(path_finder(c), 4)

    d = ("\n".join([
      "0707",
      "7070",
      "0707",
      "7070"
    ]), 42)  # test.assert_equals(path_finder(d), 42)

    e = ("\n".join([
      "700000",
      "077770",
      "077770",
      "077770",
      "077770",
      "000007"
    ]), 14)  #  test.assert_equals(path_finder(e), 14)

    f = ("\n".join([
      "777000",
      "007000",
      "007000",
      "007000",
      "007000",
      "007777"
    ]), 0)  # test.assert_equals(path_finder(f), 0)

    g = ("\n".join([
      "000000",
      "000000",
      "000000",
      "000010",
      "000109",
      "001010"
    ]), 4)  # test.assert_equals(path_finder(g), 4)

    return a, b, c, d, e, f, g


a, b, c, d, e, f, g = basic_test_cases()
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")








def path_finder(area):
    return 0 # total levels climbed