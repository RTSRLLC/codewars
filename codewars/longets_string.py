def longest(a1: str, a2: str) -> str:
    out = sorted(set(a1 + a2))
    return ''.join(out)


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
c = "abcdefghijklmnopqrstuvwxyz"

a_b = longest(a, b)  # returns "abcdefklmopqwxy"

a_ony = longest(c, c)  # returns "abcdefghijklmnopqrstuvwxyz"
