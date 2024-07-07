def is_interesting(number, awesome_phrases):
	a, b, c = number, number + 1, number + 2
	awesome = awesome_phrases
	print(f"a, b, c: {a, b, c}   awesome_phrases: {awesome_phrases}")
	
	if a > 1_000_000_000 and b > 1_000_000_000 and c > 1_000_000_000:
		print(0)
		return 0
	
	elif len(str(a)) < 3 and len(str(b)) < 3 and len(str(c)) < 3:
		return 0
	
	elif a in awesome_phrases:
		return 2 if a in awesome_phrases else 1
	elif b in awesome_phrases:
		return 2 if b in awesome_phrases else 1
	elif c in awesome_phrases:
		return 2 if c in awesome_phrases else 1
	
	elif (a % 100 == 0 or
	      b % 100 == 0 or
	      c % 100 == 0):
		print(a % 100, b % 100, c % 100)
		print(2 if (a and b and c) % 100 == 0 else 1)
		return 2 if (a % 100 == 0 and b % 100 == 0 and c % 100 == 0) else 1
	
	elif (all(list(str(a))) == str(list(str(a))[0]) or
	      all(list(str(b))) == str(list(str(b))[0]) or
	      all(list(str(c))) == str(list(str(c))[0])):
		print(2 if all(list(str(a))) == str(list(str(a))[0]) else 1)
		return 2 if all(list(str(a))) == str(list(str(a))[0]) else 1
	
	elif ((str(a) in '1234567890' or str(a) in '9876543210') or
	      (str(b) in '1234567890' or str(b) in '9876543210') or
	      (str(c) in '1234567890' or str(c) in '9876543210')):
		print(2 if str(a) in '1234567890' or str(a) in '9876543210' else 1)
		return 2 if str(a) in '1234567890' or str(a) in '9876543210' else 1
	
	elif (str(a) == str(a)[::-1] or
	      str(b) == str(b)[::-1] or
	      s
		print(2 if str(a) == str(a)[::-1] else 1)
		return 2 if str(a) == str(a)[::-1] else 1
	else:
		return 0


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
