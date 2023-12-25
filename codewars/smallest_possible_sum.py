from math import gcd
from typing import List

def solution(a: List[int]) -> int:
    """
    Calculate the sum of an array after repeatedly applying the operation:
    if X[i] > X[j] then X[i] = X[i] - X[j] until all elements are equal.
    The result is the greatest common divisor (GCD) of all elements multiplied by the length of the array.

    Args:
        a (List[int]): A list of integers to transform.

    Returns:
        int: The sum of the elements after transformation.
    """
    # Calculate the GCD for all elements and multiply by length of the array.
    return gcd(*a) * len(a)
