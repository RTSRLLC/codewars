import numpy as np

def rectangle_rotation(a: int, b: int) -> int:
    """
    Calculate the number of integer points inside a 45-degree rotated rectangle.

    Args:
        a (int): The length of the rectangle along the x-axis.
        b (int): The length of the rectangle along the y-axis.

    Returns:
        int: The number of integer points inside the rectangle.
    """
    # Calculate the effective diagonal distances
    diagonal_dist_a = a / np.sqrt(2)
    diagonal_dist_b = b / np.sqrt(2)

    # Determine the range for the grid
    x_max = int(np.ceil(diagonal_dist_a + diagonal_dist_b))
    y_max = x_max

    # Create a grid of points
    x, y = np.meshgrid(np.arange(-x_max, x_max + 1), np.arange(-y_max, y_max + 1))

    # Rotate the points back by -45 degrees
    x_rot = (x - y) / np.sqrt(2)
    y_rot = (x + y) / np.sqrt(2)

    # Check if rotated points are inside the original rectangle
    inside = ((abs(x_rot) <= a / 2) & (abs(y_rot) <= b / 2))

    return np.sum(inside)

# Test the function
a = rectangle_rotation(6, 4)  # Expected: 23
b = rectangle_rotation(30, 2)  # Expected: 65
c = rectangle_rotation(8, 6)  # Expected: 49
d = rectangle_rotation(16, 20)  # Expected: 333

print(a, b, c, d)
