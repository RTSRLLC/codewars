def solution(number: int) -> int:
    """
    Calculates the sum of all the multiples of 3 or 5 below a given number.

    This function iterates over a range of numbers from 0 up to but not including
    the given number. It checks if each number is a multiple of 3 or 5 and, if so,
    adds it to a sum. The function returns the total sum of these multiples.

    Args:
    number (int): The upper limit to check for multiples of 3 or 5.

    Returns:
    int: The sum of all multiples of 3 or 5 below the given number.

    Examples:
    >>> solution(10)
    23
    >>> solution(20)
    78
    """
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])



a = solution(6) # 8)
b = solution(16) # 60)
c = solution(3) # 0)
d = solution(5) # 3)
e = solution(15) # 45)
f = solution(0) # 0)
g = solution(-1) # 0)
h = solution(10) # 23)
i = solution(20) # 78)
j = solution(200) # 9168)
k = solution(4) # 3)
