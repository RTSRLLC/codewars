import numpy as np
from typing import Tuple

def rotate_by_45(x: float, y: float) -> Tuple[float, float]:
    """
    Rotate a point by 45 degrees around the origin.

    Args:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Returns:
        Tuple[float, float]: The rotated point's coordinates.
    """
    cos_45 = np.cos(np.radians(45))
    sin_45 = np.sin(np.radians(45))
    return x * cos_45 - y * sin_45, x * sin_45 + y * cos_45

def rectangle_rotation(a: int, b: int) -> int:
    """
    Calculate the number of integer points inside a rotated rectangle.

    The rectangle has sides of lengths 'a' and 'b', is centered at the origin,
    and is rotated 45 degrees around the origin.

    Args:
        a (int): The length of the rectangle along the x-axis.
        b (int): The length of the rectangle along the y-axis.

    Returns:
        int: The number of integer points inside the rectangle.
    """
    # Find the corners of the rectangle after rotation
    corners = [rotate_by_45(x, y) for x, y in [(a/2, b/2), (-a/2, b/2), (-a/2, -b/2), (a/2, -b/2)]]

    # Determine the bounds for checking points
    max_x = max([x for x, _ in corners])
    min_x = min([x for x, _ in corners])
    max_y = max([y for _, y in corners])
    min_y = min([y for _, y in corners])

    count = 0
    for x in range(int(min_x), int(max_x) + 1):
        for y in range(int(min_y), int(max_y) + 1):
            # Check if the point is inside the rotated rectangle
            if all((x - corner_x) * (next_corner_y - corner_y) - (y - corner_y) * (next_corner_x - corner_x) < 0
                   for (corner_x, corner_y), (next_corner_x, next_corner_y) in zip(corners, corners[1:] + corners[:1])):
                count += 1

    return count


a = rectangle_rotation(6, 4)  # 23)
b = rectangle_rotation(30, 2)  # 65)
c = rectangle_rotation(8, 6)  # 49)
d = rectangle_rotation(16, 20)  # 333)
