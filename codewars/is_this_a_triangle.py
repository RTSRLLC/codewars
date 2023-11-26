def is_triangle(a: int, b: int, c: int) -> bool:
    """
    Check if three sides can form a triangle.

    This function determines whether three given side lengths can form a triangle
    based on the Triangle Inequality Theorem. The theorem states that the sum of
    the lengths of any two sides of a triangle must be greater than the length
    of the third side. Additionally, it checks that all side lengths are positive.

    Args:
        a (int): The length of the first side of a potential triangle.
        b (int): The length of the second side of a potential triangle.
        c (int): The length of the third side of a potential triangle.

    Returns:
        bool: True if the sides can form a triangle, False otherwise.

    Examples:
        >>> is_triangle(3, 4, 5)
        True
        >>> is_triangle(1, 2, 3)
        False
        >>> is_triangle(-1, 2, 3)
        False
    """
    return all([a > 0, b > 0, c > 0]) and (a + b > c) and (a + c > b) and (b + c > a)




a = is_triangle(1, 2, 2)  # , True, "didn't work when sides were 1, 2, 2")
b = is_triangle(7, 2, 2)  # , False, "didn't work when sides were 7, 2, 2")
c = is_triangle(1, 2, 3)  # ,, False, "didn't work when sides were 1, 2, 3")
d = is_triangle(1, 3, 2)  # ,, False, "didn't work when sides were 1, 3, 2")
e = is_triangle(3, 1, 2)  # ,, False, "didn't work when sides were 3, 1, 2")
f = is_triangle(5, 1, 2)  # ,, False, "didn't work when sides were 5, 1, 2")
g = is_triangle(1, 2, 5)  # ,, False, "didn't work when sides were 1, 2, 5")
h = is_triangle(4, 2, 3)  # , True, "didn't work when sides were 4, 2, 3")
i = is_triangle(5, 1, 5)  # , True, "didn't work when sides were 5, 1, 5")
j = is_triangle(2, 2, 2)  # , True, "didn't work when sides were 2, 2, 2")
k = is_triangle(-1, 2, 3)  # , False, "didn't work when sides were -1, 2, 3")
l = is_triangle(1, -2, 3)  # , False, "didn't work when sides were 1, -2, 3")
m = is_triangle(1, 2, -3)  # , False, "didn't work when sides were 1, 2, -3")
n = is_triangle(0, 2, 3)  # , False, "didn't work when sides were 0, 2, 3")
