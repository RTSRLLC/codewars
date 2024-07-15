def is_interesting(number: int, awesome_phrases: list[int]) -> int:
    """
    Determines if a number is "interesting" based on specific criteria.

    Parameters:
    number (int): The number to be evaluated.
    awesome_phrases (list): A list of "awesome" numbers that are considered interesting.

    Returns:
    int:
        - 2 if the number is interesting.
        - 1 if an interesting number occurs within the next two miles.
        - 0 if the number is not interesting.

    An "interesting" number is defined as a 3-or-more digit number that meets one or more of the following criteria:
    - Any digit followed by all zeros (e.g., 100, 90000).
    - Every digit is the same number (e.g., 1111).
    - The digits are sequential, incrementing (e.g., 1234).
    - The digits are sequential, decrementing (e.g., 4321).
    - The digits are a palindrome (e.g., 1221, 73837).
    - The number matches one of the values in the awesome_phrases list.
    """
    # get all three numbers needed for evaluation
    a, b, c = number, number + 1, number + 2
    # convert nums to strings for efficient evaluation
    str_a, str_b, str_c = str(a), str(b), str(c)
    
    # not larger than 1,000,000,000
    if a >= 1_000_000_000 and b >= 1_000_000_000 and c >= 1_000_000_000:
        return 0

    # are greater than or equal to 100
    if len(str_a) < 3 and len(str_b) < 3 and len(str_c) < 3:
        return 0

    # is in the awesome_phrases list
    if a in awesome_phrases:
        return 2
    elif b in awesome_phrases or c in awesome_phrases:
        return 1

    # is all zeros or a palindrome
    if a % 100 == 0 or (100 <= a <= 1_000_000_000) and str_a == str_a[::-1]:
        return 2
    elif b % 100 == 0 or c % 100 == 0:
        return 1

    # are the same number
    if (all(list(str_a)) == str(list(str_a)[0]) or
            all(list(str_b)) == str(list(str_b)[0]) or
            all(list(str_c)) == str(list(str_c)[0])):
        return 2 if all(list(str_a)) == str(list(str_a)[0]) else 1

    # are sequential (incrementing or decrementing)
    if ((str_a in '1234567890' or str_a in '9876543210') or
            (str_b in '1234567890' or str_b in '9876543210') or
            (str_c in '1234567890' or str_c in '9876543210')):
        return 2 if str_a in '1234567890' or str_a in '9876543210' else 1

    # is a palindrome
    if (str_a == str_a[::-1] or
            str_b == str_b[::-1] or
            str_c == str_c[::-1]):
        return 2 if str_a == str_a[::-1] else 1

    return 0


# and Operator: If the left operand is false, Python does not evaluate the right operand
# or Operator: If the left operand is true, Python does not evaluate the right operand

a = is_interesting(98, [1337, 256])  # 1
aa = is_interesting(99, [1337, 256])  # 1
aaa = is_interesting(6998, [1337, 256])  # 1
aaaa = is_interesting(799999, [1337, 256])  # 1
aaaaa = is_interesting(999999999, [1337, 256])  # 2
b = is_interesting(654, [1337, 256])  # 1
c = is_interesting(1337, [1337, 256])  # 2
d = is_interesting(11208, [1337, 256])  # 0
e = is_interesting(11209, [1337, 256])  # 1
f = is_interesting(11211, [1337, 256])  # 2
g = is_interesting(1111, [1337, 256])  # 2
h = is_interesting(1234, [1337, 256])  # 2
i = is_interesting(7890, [1337, 256])  # 2
j = is_interesting(4321, [1337, 256])  # 2
k = is_interesting(300, [1337, 256])  # 2
ll = is_interesting(298, [1337, 256])  # 1
m = is_interesting(299, [1337, 256])  # 1

# 2 if the number is "interesting"
# 1 if an interesting number occurs within the next two miles
# 0 if the number is not interesting
# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# † For incrementing sequences, 0 should come after 9, and not before  1, as in 7890.
# The digits are sequential, decrementing‡: 4321
# ‡ For decrementing sequences, 0 should come after 1, and not before  9, as in 3210.
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
#
