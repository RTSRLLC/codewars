import numpy as np


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

    # get the equation of the lines that make up the rectangle form lest x to max x
    m1, y_intercept1 = get_line_equation(q1, q4)
    y1 = get_x_y_vals(m1, y_intercept1, q1, q4)

    m2, y_intercept2 = get_line_equation(q2, q1)
    y2 = get_x_y_vals(m2, y_intercept2, q2, q1)

    m3, y_intercept3 = get_line_equation(q2, q3)
    y3 = get_x_y_vals(m3, y_intercept3, q2, q3)

    m4, y_intercept4 = get_line_equation(q3, q4)
    y4 = get_x_y_vals(m4, y_intercept4, q3, q4)

    # from the smallest x value to the largest x value, check for integer y values inside the rectangle

    return 0


def get_x_y_vals(slope: float, y_intercept: float, vec_1: np.array, vec_2: np.array) -> np.array:
    """
    Given the slope and y-intercept of a line, get the x and y values of the line
    Args:
        slope (): slope of the line
        y_intercept (): y-intercept of the line
        vec_1 (): vector 1
        vec_2 (): vector 2

    Returns: the x and y values of the line in a zip object

    """
    print(f"vec_1: {vec_1}, vec_2: {vec_2}")
    print(f"ints for the equation are: {int(vec_1[0]), int(vec_2[0])}")
    x = np.arange(int(vec_1[0]), int(vec_2[0]), 0.1)
    print(f"the x values: {x}")
    y = slope * x + y_intercept
    print(f"the list: {list(iter(zip(x, y)))}\n{'*' * 50}")
    return list(iter(zip(x, y)))


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
    return (np.dot(forty5_degree, q1), np.dot(forty5_degree, q2),
            np.dot(forty5_degree, q3), np.dot(forty5_degree, q4))


def get_line_equation(vec1: np.array, vec2: np.array) -> tuple:
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


# q1 = [0.70710678 3.53553391]
# q2 = [-3.53553391 -0.70710678]
# q3 = [-0.70710678 -3.53553391]
# q4 = [3.53553391 0.70710678]


a = rectangle_rotation(6, 4)  # 23)
# b = rectangle_rotation(30, 2)  # 65)
# c = rectangle_rotation(8, 6)  # 49)
# d = rectangle_rotation(16, 20)  # 333)
