import numpy as np


def rectangle_rotation(a: int, b: int) -> int:
    """
    Given a rectangle with sides = a: x-axis, b: y-axis centered at the origin, rotate the rectangle by 45 degrees
    Args:
        a (): x-axis length: divide by 2 to get the x-axis coordinates
        b (): y-axis length: divide by 2 to get the y-axis coordinates

    Returns: the number of points that lie inside the rectangle after rotation

    """
    # get the four corners of the rectangle
    q1 = np.array([a / 2, b / 2])
    q2 = np.array([-a / 2, b / 2])
    q3 = np.array([-a / 2, -b / 2])
    q4 = np.array([a / 2, -b / 2])

    # rotate the rectangle by 45 degrees
    q1, q2, q3, q4 = rotate_by_45(q1, q2, q3, q4)
    print(q1, q2, q3, q4, sep='\n', end='\n\n')

    # get the equation of the lines that make up the rectangle
    m1, y_intercept1 = get_line_equation(q1, q4)
    y1 = m1 * x + y_intercept1
    print(f"y1 = {m1}x + {y_intercept1}")
    m2, y_intercept2 = get_line_equation(q2, q1)
    y2 = m2 * x + y_intercept2
    print(f"y2 = {m2}x + {y_intercept2}")
    m3, y_intercept3 = get_line_equation(q3, q2)
    y3 = m3 * x + y_intercept3
    print(f"y3 = {m3}x + {y_intercept3}")
    m4, y_intercept4 = get_line_equation(q3, q4)
    y4 = m4 * x + y_intercept4
    print(f"y4 = {m4}x + {y_intercept4}")

    # plugging in the integer x values from -x to x that lie inside the rectangle's line equations that are less than y1 and than y2 and greater than y3 and less than y4, get the cooresponding y values iff they are integers then count and return them
    count = 0
    for x in range(int(-a / 2), a // 2):
        print(f"x = {x}")
    return count



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
