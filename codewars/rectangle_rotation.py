import numpy as np
import pandas as pd


def rectangle_rotation(a: int, b: int) -> int:
    """
    Given a rectangle with sides = a: x-axis, b: y-axis centered at the origin, rotate the rectangle by 45 degrees
    Args:
        a (): x-axis length: divide by 2 to get the x-axis coordinates
        b (): y-axis length: divide by 2 to get the y-axis coordinates

    Returns: the number of points that lie inside the rectangle after rotation

    """
    q1, q2, q3, q4 = get_corners(a, b)
    # print(q1, q2, q3, q4, sep='\n', end='\n\n')

    topx, topy = get_x_and_y_linspace_for_top_line_of_rect(q1, q3)
    # print(type(topx), topx[:5], topx[-5:], topy[:5], topy[-5:], sep='\n', end='\n\n')

    rectangle = get_matrix_of_rectangle_points(topx, topy)
    # print(type(rectangle), rectangle.shape, rectangle[:5], rectangle[-5:], sep='\n', end='\n\n')

    # rotate the rectangle by 45 degrees
    rotation = rotate_rectangle_points(rectangle)

    return pd.DataFrame(rotation.reshape(-1, 2))


def get_corners(a: int, b: int) -> np.array:
    """
    Get the corners of a rectangle
    Args:
        a (): x-axis length: divide by 2 to get the x-axis coordinates
        b (): y-axis length: divide by 2 to get the y-axis coordinates

    Returns: the corners of the rectangle

    """
    # get the four corners of the rectangle: 'q' stands for quadrant in the coordinate system
    q1 = np.array([a / 2, b / 2])
    q2 = np.array([-a / 2, b / 2])
    q3 = np.array([-a / 2, -b / 2])
    q4 = np.array([a / 2, -b / 2])

    return q1, q2, q3, q4


def get_x_and_y_linspace_for_top_line_of_rect(vec1: np.array, vec2: np.array) -> np.array:
    """
    Get a linear space for the whole rectangle
    Args:
        vec1 (): np.array([a / 2, b / 2])
        vec2 (): np.array([-a / 2, b / 2])

    Returns: the linear space for the whole rectangle

    """
    return np.linspace(vec1[0], vec2[0], 1000), np.linspace(vec1[1], vec2[1], 1000)


def get_matrix_of_rectangle_points(topx: np.array, topy: np.array) -> np.array:
    """
    Take in the top x and y values of the rectangle and return the points of the rectangle along each line.
    Args:
        topx (np.array): Array of top x values of the rectangle.
        topy (np.array): Array of top y values of the rectangle.

    Returns:
        np.array: A matrix of the rectangle points where each element is a tuple (x, y).
    """
    # Create a 3D array: the third dimension is of size 2 to hold tuples
    matrix = np.zeros((len(topx), len(topy), 2))

    # Iterate through the arrays and assign tuple values
    for i, x in enumerate(topx):
        for j, y in enumerate(topy):
            matrix[i, j] = (x, y)

    return matrix

def rotate_rectangle_points(matrix: np.array) -> np.array:
    """
    Rotate each point in a rectangle matrix by 45 degrees.
    Args:
        matrix (np.array): A 3D array where each element is a tuple (x, y) representing a point on the rectangle.

    Returns:
        np.array: The rotated rectangle matrix.
    """
    # Define the 2x2 45 degree rotation matrix
    rotation_matrix = np.array([[np.sqrt(2) / 2, -np.sqrt(2) / 2], [np.sqrt(2) / 2, np.sqrt(2) / 2]])

    # Create an empty matrix for the rotated points
    rotated_matrix = np.zeros_like(matrix)

    # Iterate through the matrix and apply the rotation to each point
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            rotated_matrix[i, j] = np.round(np.dot(rotation_matrix, matrix[i, j]), 3)

    return rotated_matrix


a = rectangle_rotation(6, 4)  # 23)
# b = rectangle_rotation(30, 2)  # 65)
# c = rectangle_rotation(8, 6)  # 49)
# d = rectangle_rotation(16, 20)  # 333)


old_code = 'commented out'

#
# def vector_xy_vals(vec1: np.array, vec2: np.array) -> np.array:
#     """
#     Get the x and y values of a line given two points using r = a + t(b−a) where r is the vector, a is the starting
#     point, b is the ending point, and t is a scalar
#     Args:
#         vec1 (): vector 1
#         vec2 (): vector 2
#
#     Returns: the x and y values of the line
#
#     """
#     _, y_intercept = get_slope(vec1, vec2)
#     t_values = np.round(np.arange(0, 1.001, 0.001), 3)
#     x_vals = vec1[0] + t_values * (vec2[0] - vec1[0])
#     y_vals = vec1[1] + t_values * (vec2[1] - vec1[1])
#     return np.round(list(iter(zip(x_vals, y_vals))), 3), y_intercept
#
#
# def boundary_values(xy1: np.array, xy2: np.array, xy3: np.array, xy4: np.array) -> list:
#     # sourcery skip: extract-duplicate-method, inline-immediately-returned-variable
#     """
#     Calculate the boundary values between four points.
#
#     This function computes the boundary lines between two pairs of points.
#     For each pair of points (xy1, xy2) and (xy3, xy4), it creates a list of
#     (x, y) coordinates representing the line between these points.
#
#     Parameters:
#     xy1 (np.array): A numpy array containing the x and y coordinates of the first point.
#     xy2 (np.array): A numpy array containing the x and y coordinates of the second point.
#     xy3 (np.array): A numpy array containing the x and y coordinates of the third point.
#     xy4 (np.array): A numpy array containing the x and y coordinates of the fourth point.
#
#     Returns:
#     list: Two lists of (x, y) tuples representing the boundary lines between (xy1, xy2) and (xy3, xy4).
#     """
#     xy1_x_range = np.round(np.arange(xy2[0], xy1[0], 0.0001)[::-1], 3)
#     xy1_y_range = np.round(np.arange(xy2[1], xy1[1], 0.0001)[::-1], 3)
#     xy1_line = list(zip(xy1_x_range, xy1_y_range))
#     print(xy1_line[:5], end='\n\n')
#     print(xy1_line[-5:], end='\n\n')
#
#     xy4_x_range = np.round(np.arange(xy3[0], xy4[0], 0.0001)[::-1], 3)
#     xy4_y_range = np.round(np.arange(xy3[1], xy4[1], 0.0001)[::-1], 3)
#     xy4_line = list(zip(xy4_x_range, xy4_y_range))
#     print(xy4_line[:5], end='\n\n')
#     print(xy4_line[-5:], end='\n\n')
#
#     return list(zip(xy1_line, xy4_line))
#
#
# def get_slope(vec1: np.array, vec2: np.array) -> tuple:
#     """
#     Get the equation of a line given two points
#     Args:
#         vec1 (): vector 1
#         vec2 (): vector 2
#
#     Returns: the equation of the line
#
#     """
#     # y−y1=m(x−x1) point slope form
#     m = (vec2[1] - vec1[1]) / (vec2[0] - vec1[0])
#
#     # y−y1=m(x−x1) point intercept form
#     y_intercept = vec1[1] - m * vec1[0]
#
#     return m, y_intercept
