"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
For example:
  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
  9 ==> -1
111 ==> -1
531 ==> -1
"""

from itertools import permutations
import time


def next_bigger(n):
    digits = list(str(n))
    length = len(digits)
    
    # Step 1: Find the rightmost digit that is smaller than the digit next to it
    a = list(range(length - 2, -1, -1))
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1
    
    # Step 2: Find the smallest digit on the right side of the found digit that is larger than it
    b = list(range(length - 1, i, -1))
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break
    
    # Step 3: Swap the found digits
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the digits after the position i
    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    return int(''.join(digits))


start = time.time()

# a = next_bigger(21)  # ,   -1)
# # print('*' * 72)
# #
# b = next_bigger(513)  # ,  531)
# print('*' * 72)

c = next_bigger(2017)  # , 2071)
print('*' * 72)

d = next_bigger(414)  # ,  441)
print('*' * 72)

e = next_bigger(144)  # ,  414)
print('*' * 72)

f = next_bigger(1234567890)  # , 1234567908)

end = time.time()
print(f"Time: {(end - start) * 1000:.2f} ms")
