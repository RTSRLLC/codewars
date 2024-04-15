"""
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any
digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
"""

# import queue
import collections
print(help(collections.deque))

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
	def break_into_base10(n):
		digits = []
		keys = sorted(RomanNumerals.NUMERAL_ROMANS.keys(), reverse=True)
		for key in keys:
			while n >= key:
				digits.append(key)
				n -= key
		return digits

	@staticmethod
	def to_roman(val: int) -> str:
		return ''.join([RomanNumerals.NUMERAL_ROMANS[i] for i in RomanNumerals.break_into_base10(val)])

	@staticmethod
	def from_roman(roman_num: str) -> int:
		print(f'Roman Num: {roman_num}')
		lis = [i for i in roman_num]
		print(f'List: {lis}')
		print(RomanNumerals.ROMAN_NUMERALS)
		output = 0
		test_string = ''
		for idx, let in enumerate(lis):
			test_string += let
			try:
				test_string += lis[idx + 1]
			except IndexError:
				pass
			if test_string in RomanNumerals.ROMAN_NUMERALS:
				output += RomanNumerals.ROMAN_NUMERALS[test_string]
				test_string = ''
			else:
				keep_next_value = [i for i in test_string]
				for i in keep_next_value:
					if i in RomanNumerals.ROMAN_NUMERALS:
						output += RomanNumerals.ROMAN_NUMERALS[i]
						test_string = ''
						test_string = i
						continue

			# output += sum(map(lambda x: RomanNumerals.ROMAN_NUMERALS[x], keep_next_value))
		return output


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

# running a test on lag
