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
    # get the four corners of the rectangle: 'q' stands for quadrant in the coordinate system
    q1 = np.array([a / 2, b / 2])
    q2 = np.array([-a / 2, b / 2])
    q3 = np.array([-a / 2, -b / 2])
    q4 = np.array([a / 2, -b / 2])

    # rotate the rectangle by 45 degrees
    q1, q2, q3, q4 = rotate_by_45(q1, q2, q3, q4)
    print(q1, q2, q3, q4, sep='\n', end='\n\n')

    family_line_boundaries = boundary_values(q1, q2, q3, q4)
    print(
            f"family_line_boundaries head:\n{family_line_boundaries[:5]}\n{family_line_boundaries[-5:]}\nlength: {len(family_line_boundaries)}\n")

    line_points = {}
    for vecs in family_line_boundaries:
        r, intercept = vector_xy_vals(vecs[0], vecs[1])
        # print(f"intercept: {intercept}\n")
        line_points[intercept] = r

    # Create a list to hold the individual DataFrames
    dfs = []

    for key, values in line_points.items():
        # Create a DataFrame for each key
        temp_df = pd.DataFrame(values, columns=[f'{key}_x', f'{key}_y'])
        dfs.append(temp_df)

    # Concatenate all DataFrames at once
    df = pd.concat(dfs, axis=1)
    is_integer = df.map(lambda x: x.is_integer())
    is_integer_sum = is_integer.sum()

    return is_integer_sum.sum()


def vector_xy_vals(vec1: np.array, vec2: np.array) -> np.array:
    """
    Get the x and y values of a line given two points using r = a + t(b−a) where r is the vector, a is the starting
    point, b is the ending point, and t is a scalar
    Args:
        vec1 (): vector 1
        vec2 (): vector 2

    Returns: the x and y values of the line

    """
    _, y_intercept = get_slope(vec1, vec2)
    t_values = np.round(np.arange(0, 1.001, 0.001), 3)
    x_vals = vec1[0] + t_values * (vec2[0] - vec1[0])
    y_vals = vec1[1] + t_values * (vec2[1] - vec1[1])
    return np.round(list(iter(zip(x_vals, y_vals))), 3), y_intercept


def boundary_values(xy1: np.array, xy2: np.array, xy3: np.array, xy4: np.array) -> list:
    # sourcery skip: extract-duplicate-method, inline-immediately-returned-variable
    """
    Calculate the boundary values between four points.

    This function computes the boundary lines between two pairs of points.
    For each pair of points (xy1, xy2) and (xy3, xy4), it creates a list of
    (x, y) coordinates representing the line between these points.

    Parameters:
    xy1 (np.array): A numpy array containing the x and y coordinates of the first point.
    xy2 (np.array): A numpy array containing the x and y coordinates of the second point.
    xy3 (np.array): A numpy array containing the x and y coordinates of the third point.
    xy4 (np.array): A numpy array containing the x and y coordinates of the fourth point.

    Returns:
    list: Two lists of (x, y) tuples representing the boundary lines between (xy1, xy2) and (xy3, xy4).
    """
    xy1_x_range = np.round(np.arange(xy2[0], xy1[0], 0.0001)[::-1], 3)
    xy1_y_range = np.round(np.arange(xy2[1], xy1[1], 0.0001)[::-1], 3)
    xy1_line = list(zip(xy1_x_range, xy1_y_range))
    print(xy1_line[:5], end='\n\n')
    print(xy1_line[-5:], end='\n\n')

    xy4_x_range = np.round(np.arange(xy3[0], xy4[0], 0.0001)[::-1], 3)
    xy4_y_range = np.round(np.arange(xy3[1], xy4[1], 0.0001)[::-1], 3)
    xy4_line = list(zip(xy4_x_range, xy4_y_range))
    print(xy4_line[:5], end='\n\n')
    print(xy4_line[-5:], end='\n\n')

    return list(zip(xy1_line, xy4_line))


def rotate_by_45(q1: np.array, q2: np.array, q3: np.array, q4: np.array) -> np.array:
    """
    Rotate a rectangle by 45 degrees
    Args:
        q1 (): np.array([a / 2, b / 2])
        q2 (): np.array([-a / 2, b / 2])
        q3 (): np.array([-a / 2, -b / 2])
        q4 (): np.array([a/ 2, -b / 2])

    Returns: the rotated rectangle

    """
    # get  2x2 45 degree rotation matrix
    forty5_degree = np.array([[np.sqrt(2) / 2, -np.sqrt(2) / 2], [np.sqrt(2) / 2, np.sqrt(2) / 2]])
    return (np.round(np.dot(forty5_degree, q1), 3), np.round(np.dot(forty5_degree, q2), 3),
            np.round(np.dot(forty5_degree, q3), 3), np.round(np.dot(forty5_degree, q4), 3))


def get_slope(vec1: np.array, vec2: np.array) -> tuple:
    """
    Get the equation of a line given two points
    Args:
        vec1 (): vector 1
        vec2 (): vector 2

    Returns: the equation of the line

    """
    # y−y1=m(x−x1) point slope form
    m = (vec2[1] - vec1[1]) / (vec2[0] - vec1[0])

    # y−y1=m(x−x1) point intercept form
    y_intercept = vec1[1] - m * vec1[0]

    return m, y_intercept


a = rectangle_rotation(6, 4)  # 23)
# b = rectangle_rotation(30, 2)  # 65)
# c = rectangle_rotation(8, 6)  # 49)
# d = rectangle_rotation(16, 20)  # 333)
