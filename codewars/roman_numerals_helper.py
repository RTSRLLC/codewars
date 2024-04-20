"""
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any
digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
"""

from itertools import pairwise


class RomanNumerals:
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
		digits = []
		keys = sorted(RomanNumerals.NUMERAL_ROMANS.keys(), reverse=True)
		for key in keys:
			while n >= key:
				digits.append(key)
				n -= key
		return digits
	
	@staticmethod
	def to_roman(val: int) -> str:
		return ''.join([RomanNumerals.NUMERAL_ROMANS[i] for i in RomanNumerals.base10(val)])
	
	@staticmethod
	def from_roman(roman_num: str) -> int:
		lis = [i for i in roman_num]
		lis_copy = lis.copy()
		print(f"RomanNumerals: {RomanNumerals.ROMAN_NUMERALS}")
		pairwise_pairs = pairwise([i for i in roman_num])
		pairwise_pairs_og = list(''.join(i) for i in list(pairwise_pairs))
		paired_copies = list(''.join(i) for i in list(pairwise_pairs_og))
		# answer is 659: d = 500 c = 100, l = 50, i = 1, x = 10, i = 1, x = 10, i = 1
		pairwise_index = 0
		in_roman_numerals = [i for i in pairwise_pairs_og if i in RomanNumerals.ROMAN_NUMERALS]
		split_in_roman_numerals = [char for pair in in_roman_numerals for char in pair]
		# remove items in split_in_ROMAN_NUMERALS from lis_copy
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
