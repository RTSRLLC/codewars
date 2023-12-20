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
        return a[0]
    if len(a) == 2:
        while a[1] > a[0]:
            a[1] -= a[0]
        return sum(a)
    a_reverse = a[::-1]
    for i, num in enumerate(a_reverse):
        print(f"In the for loop and a_reverse: {a_reverse}")
        T_or_F = True
        idx = i
        while T_or_F:
            print("In the while loop")
            print(f"    idx: {idx}, num: {num}")
            print(f"idx + 1: {idx + 1}, num: {a_reverse[idx + 1]}")
            print(f"is greater than: {a_reverse[idx] > a_reverse[idx + 1]}")
            if idx == len(a_reverse) - 1:
                print("Breaking")
                break
            if a_reverse[idx] > a_reverse[idx + 1]:
                print("Still needing to subtract")
                a_reverse[idx] = num - a_reverse[idx + 1]
            if idx + 1 < a_reverse[idx + 1]:
                print("Going to False")
                T_or_F = False
            print(f"a_reverse: {a_reverse}")
        T_or_F = True
    return sum(a_reverse)


# a = solution([9])  # , 9)
# b = solution([6, 9, 21])  # , 9)
c = solution([1, 21, 55])  # , 3)
