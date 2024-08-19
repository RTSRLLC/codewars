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
	try:
		_ = [i for i in permutations(str(n))]
		_ = sorted(int(''.join(x)) for x in _ if int(''.join(x)) > n)[0]
		return _ if _ else -1
	except IndexError:
		print(f"No larger number found for {n}")
		return -1


start = time.time()

# a = next_bigger(21)  # ,   -1)
print('*' * 72)

b = next_bigger(513)  # ,  531)
print('*' * 72)

c = next_bigger(2017)  # , 2071)
print('*' * 72)

d = next_bigger(414)  # ,  441)
print('*' * 72)

e = next_bigger(144)  # ,  414)
print('*' * 72)

f = next_bigger(1234567890)  # , 1234567908)

end = time.time()
print(f"Time: {(end - start) * 1000:.2f} ms")
