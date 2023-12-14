def same_structure_as(original, other):
    pass


a = same_structure_as([1, [1, 1]], [2, [2, 2]])  # , True, "[1,[1,1]] same as [2,[2,2]]")
b = same_structure_as([1, [1, 1]], [[2, 2], 2])  # , False, "[1,[1,1]] not same as [[2,2],2]")

# should return True
c = same_structure_as([1, 1, 1], [2, 2, 2])
d = same_structure_as([1, [1, 1]], [2, [2, 2]])

# should return False
e = same_structure_as([1, [1, 1]], [[2, 2], 2])
f = same_structure_as([1, [1, 1]], [[2], 2])

# should return True
g = same_structure_as([[[], []]], [[[], []]])

# should return False
h = same_structure_as([[[], []]], [[1, 1]])
