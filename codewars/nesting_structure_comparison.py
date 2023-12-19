def same_structure_as(original: list, other: list) -> bool:
    """
    Compares two lists to see if they have the same structure.

    Args:
        original (list): The original list to compare.
        other (list): The other list to compare.

    Returns:
        bool: True if the lists have the same structure, False otherwise.
    """

    # Are both lists
    if not (isinstance(original, list) and isinstance(other, list)):
        return False

    # Are lengths equal
    if len(original) != len(other):
        return False

    # Iterate through both
    for orig_item, other_item in zip(original, other):
        # Are both lists
        if isinstance(orig_item, list) and isinstance(other_item, list):
            # Compare the nested lists via recursion
            if not same_structure_as(orig_item, other_item):
                return False
        # Are both lists
        elif isinstance(orig_item, list) or isinstance(other_item, list):
            return False

    return True


print("c = true")
c = same_structure_as([1, 1, 1], [2, 2, 2])
print(c)
print('*' * 50)

print("d = true")
d = same_structure_as([1, [1, 1]], [2, [2, 2]])
print(d)
print('*' * 50)

print("e = false")
e = same_structure_as([1, [1, 1]], [[2, 2], 2])
print(e)
print('*' * 50)

print("f = false")
f = same_structure_as([1, [1, 1]], [[2], 2])
print(f)
print('*' * 50)

print("g = true")
g = same_structure_as([[[], []]], [[[], []]])
print(g)
print('*' * 50)

print("h = false")
h = same_structure_as([[[], []]], [[1, 1]])
print(h)
print('*' * 50)

print("i = false")
i = same_structure_as([], 1)
print(i)
print('*' * 50)
