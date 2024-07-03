def is_interesting(number, awesome_phrases):
	if len(str(number)) < 3:
		return 0
	if number in awesome_phrases:
		return 2
	if number % 100 == 0:
		return 2
	if str(number) == str(number)[::-1]:
		return 2
	if all(list(str(number))) == str(list(str(number))[0]):
		return 2
	# The digits are sequential, incrementing†: 1234
	a = str(number)
	if str(number) in '1234567890':
		return 2
	# The digits are sequential, decrementing‡: 4321
	if str(number) in '0987654321':
		return 2


# a = is_interesting(3, [1337, 256])  # 0
# b = is_interesting(1336, [1337, 256])  # 1
# c = is_interesting(1337, [1337, 256])  # 2
# d = is_interesting(11208, [1337, 256])  # 0
# e = is_interesting(11209, [1337, 256])  # 1
# f = is_interesting(11211, [1337, 256])  # 2
# g = is_interesting(1111, [1337, 256])  # 2
h = is_interesting(1234, [1337, 256])  # 2ih = is_interesting(7890, [1337, 256])  # 2
i = is_interesting(7890, [1337, 256])  # 2
j = is_interesting(4321, [1337, 256])  # 2

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
