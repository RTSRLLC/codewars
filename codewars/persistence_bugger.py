from math import prod

def persistence(n: int) -> int:
    """
    Calculate the multiplicative persistence of a number.

    The multiplicative persistence of a number is the number of times you must
    multiply the digits in num together until you reach a single digit.

    Args:
        n (int): A non-negative integer whose multiplicative persistence is to be found.

    Returns:
        int: The multiplicative persistence of the number.

    Examples:
        >>> persistence(39)
        3
        >>> persistence(999)
        4
        >>> persistence(4)
        0
    """
    counter = 0
    while n >= 10:
        n = prod(map(int, str(n)))
        counter += 1
    return counter




a = persistence(39) # 3)
b = persistence(4) # 0)
c = persistence(25) # 2)
d = persistence(999)  # 4)
