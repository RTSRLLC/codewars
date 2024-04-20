from itertools import pairwise


class RomanNumerals:
	# Dictionary mapping Roman numerals to their base-10 values.
	ROMAN_NUMERALS = {
		"M": 1000,
		"CM": 900,
		"D": 500,
		"CD": 400,
		"C": 100,
		"XC": 90,
		"L": 50,
		"XL": 40,
		"X": 10,
		"IX": 9,
		"V": 5,
		"IV": 4,
		"I": 1
		}
	
	NUMERAL_ROMANS = {v: k for k, v in ROMAN_NUMERALS.items()}
	
	@staticmethod
	def base10(n):
		"""
		Converts a base-10 number into a list of its Roman numeral components.

		:param n: The base-10 number to be converted.
		:return: A list of integers representing the base-10 values of the Roman numeral components.
		"""
		digits = []
		keys = sorted(RomanNumerals.NUMERAL_ROMANS.keys(), reverse=True)
		for key in keys:
			while n >= key:
				digits.append(key)
				n -= key
		return digits
	
	@staticmethod
	def to_roman(val: int) -> str:
		"""
		Converts a base-10 number to its Roman numeral representation.

		:param val: The base-10 number to be converted.
		:return: A string representing the Roman numeral equivalent of the input number.
		"""
		return ''.join([RomanNumerals.NUMERAL_ROMANS[i] for i in RomanNumerals.base10(val)])
	
	@staticmethod
	def from_roman(roman_num: str) -> int:
		"""
		Converts a Roman numeral to its base-10 representation.

		:param roman_num: The Roman numeral string to be converted.
		:return: An integer representing the base-10 equivalent of the Roman numeral.
		"""
		lis = [i for i in roman_num]
		lis_copy = lis.copy()
		pairwise_pairs = pairwise([i for i in roman_num])
		pairwise_pairs_og = list(''.join(i) for i in list(pairwise_pairs))
		in_roman_numerals = [i for i in pairwise_pairs_og if i in RomanNumerals.ROMAN_NUMERALS]
		split_in_roman_numerals = [char for pair in in_roman_numerals for char in pair]
		for i in split_in_roman_numerals:
			lis_copy.remove(i)
		a_sum = sum([RomanNumerals.ROMAN_NUMERALS[i] for i in lis_copy]) + sum(
			[RomanNumerals.ROMAN_NUMERALS[i] for i in in_roman_numerals]
			)
		return a_sum


a = RomanNumerals()
# To Roman
# print(a.ROMAN_NUMERALS, a.NUMERAL_ROMANS, sep='\n\n')
# print(a.to_roman(1000))  # 'M'
# print(a.to_roman(2000))  # 'MM''
# print(a.to_roman(1666))  # 'MDCLXVI'
# print(a.to_roman(86))  # 'LXXXVI'
# print(a.to_roman(1))  # 'I'

# From Roman
# print(a.from_roman("MM"))  # 2000
# print(a.from_roman("MDCLXVI"))  # 1666
# print(a.from_roman("LXXXVI"))  # 86
# print(a.from_roman("I"))  # 1
print(a.from_roman("DCLIX"))  # 659
