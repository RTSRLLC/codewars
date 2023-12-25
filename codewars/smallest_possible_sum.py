from typing import Any, Tuple


def subtraction(a_list: list, large: int, small: int) -> tuple[Any, Any]:
    """
    Subtracting the larger index of a_list from the smaller index of a_list.
    The length of the list will prevent IndexError: list index out of range.
    Args:
        a_list (): a list greater than length 1
        large (): the larger index of a_list
        small (): the smaller index of a_list
        previous_num (): the previous number in the list

    Returns: the portion of the larger list with larger index less than smaller index, which is reinserted into the list
    """
    while a_list[large] > a_list[small]:
        a_list[large] = a_list[large] - a_list[small]
        print(f"a_list: {a_list}, large: {a_list[large]}, small: {a_list[small]}")
    return a_list[0], a_list[1]


def solution(a: list) -> int:
    """
    Apply this algorithm, if X[i] > X[j] then X[i] = X[i] - X[j], recursively until it can not be done any more.

    The list [6, 9, 21] iterates as:
        X_1 = [6, 9, 12] # -> X_1[2] = X_1[2] - X_1[1] = 21 - 9
        X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
        X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
        X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
        X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3

        [6, 9, 12] #-> X[2] = 21 - 9
        [6, 9, 6] #-> X[2] = 12 - 6
        [6, 3, 6] #-> X[1] = 9 - 6
        [6, 3, 3] #-> X[2] = 6 - 3
        [3, 3, 3] #-> X[1] = 6 - 3

    There are no further iterations possible, so the algorithm stops and the result is [3, 3, 3].

    Args:
        a (): list of integers

    Returns: the sum of the remaining numbers

        """
    if len(a) == 1:
        return sum(a)
    idx_lg = -1
    idx_sm = -2
    for idx, num in enumerate(a):
        if idx == len(a) - 1:
            return sum(a)
        print(f"a[idx_lg]: {a[idx_lg]}, a[idx_sm]: {a[idx_sm]}")
        if a[idx_lg] > a[idx_sm]:
            x, y = subtraction(a, idx_lg, idx_sm)
            idx_lg -= 1
            idx_sm -= 1
            print(f"a: {a}")
            # if a[idx_lg] < a[idx_lg - 1]:
            #     x, y = subtraction(a, idx_lg, idx_sm)


# a = solution([9])  # , 9)
b = solution([6, 9, 21])  # , 9)
# c = solution([1, 21, 55])  # , 3)
