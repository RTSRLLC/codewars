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


def next_bigger(n):
	print(n)
	sorted_perms = sorted(list(set(int(''.join(x)) for x in list(permutations(list(str(n)))))))
	try:
		next_num = sorted_perms[sorted_perms.index(n) + 1]
		return next_num
	except IndexError as e:
		return -1


def next_bigger_(n):
	list_n = list(str(n))
	print(f"list_n:\n{list_n}")
	perm = list(permutations(list_n))
	print(f"perm:\n{perm}")
	perms_ = sorted(int(''.join(x)) for x in perm)
	print(f"perms_:\n{perms_}")
	set_perms = set(perms_)
	print(f"set_perms:\n{set_perms}")
	list_perms = list(set_perms)
	print(f"list_perms:\n{list_perms}")
	sorted_perms = sorted(list_perms)
	print(f"sorted_perms:\n{sorted_perms}")
	loc = sorted_perms.index(n)
	print(f"loc:\n{loc}")
	try:
		next_num = sorted_perms[loc + 1]
		return next_num
	except IndexError as e:
		return -1


a = next_bigger(21)  # ,   -1)
aa = next_bigger_(21)  # ,   -1)
print('*' * 72)

b = next_bigger(513)  # ,  531)
bb = next_bigger_(513)  # ,  531)
print('*' * 72)

c = next_bigger(2017)  # , 2071)
cc = next_bigger_(2017)  # , 2071)
print('*' * 72)

d = next_bigger(414)  # ,  441)
dd = next_bigger_(414)  # ,  441)
print('*' * 72)

e = next_bigger(144)  # ,  414)
ee = next_bigger_(144)  # ,  414)
print('*' * 72)
