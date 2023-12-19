def solution(a: list) -> int:
    while len(a) > 1:
        a.sort()
        a.append(a.pop() - a.pop())
    return a[0]
    # smallest possible sum of all numbers in Array


a = solution([9])  # , 9)
b = solution([6, 9, 21])  # , 9)
c = solution([1, 21, 55])  # , 3)
