def subtraction(a_list: list, larger: int, smaller: int) -> list:
    while a_list[larger] > a_list[smaller]:
        print(f"subtraction: {a_list}, larger = {larger} : {a_list[larger]}, smaller = {smaller} : {a_list[smaller]}")
        if a_list[larger] < a_list[smaller + 2]:
            print(f"subtraction: {a_list}, larger: {a_list[larger + 1]}, smaller: {a_list[smaller + 1]}")
            a_list = subtraction(a_list, larger + 1, smaller + 1)
            larger -= 1
            smaller -= 1
            a_list = subtraction(a_list, larger + 1, smaller + 1)
        try:
            print(f"subtraction: {a_list}, larger = {larger} : {a_list[larger]}, smaller = {smaller} : {a_list[smaller]}")
            a_list[larger] = a_list[larger] - a_list[smaller]
        except IndexError:
            break

    return a_list


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
    print(f"input: {a}")
    if len(a) == 1:
        return sum(a)
    length = len(a)
    idx = -1
    while length > 1:
        b = subtraction(a_list=a, larger=idx, smaller=idx - 1)
        a = b
        length -= 1
        idx -= 1

    return sum(a)


a = solution([9])  # , 9)
b = solution([6, 9, 21])  # , 9)
c = solution([1, 21, 55])  # , 3)
