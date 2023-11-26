def dig_pow(n: int, p: int) -> int:
    """
    Calculate if there exists a positive integer k such that the sum of the digits of n
    raised to consecutive powers starting from p is equal to k * n.

    Args:
        n (int): The positive integer to be checked.
        p (int): The starting power for raising digits.

    Returns:
        int: If there exists a positive integer k, return k. If not, return -1.
    """
    brk = list(str(n))
    ints = [int(i) for i in brk]
    mods = divmod(sum(digit ** (p + idx) for idx, digit in enumerate(ints)), n)
    return mods[0] if mods[1] == 0 else -1



a = dig_pow(89, 1) #, 1)
b = dig_pow(92, 1) #, -1)
c = dig_pow(46288, 3)# , 51)
d = dig_pow(41, 5)# , 25)
e = dig_pow(114, 3)# , 9)
f = dig_pow(8, 3)# , 64)
g = dig_pow(695, 2)# , 2)

