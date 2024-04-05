"""
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any
digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
"""


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

	@staticmethod
	def to_roman(val: int) -> str:
		return ''

	@staticmethod
	def from_roman(roman_num: str) -> int:
		return 0


a = RomanNumerals()
print(a.to_roman(1000))  # 'M'
# To Roman
print(a.to_roman(2000))  # 'MM'
print(a.to_roman(1666))  # 'MDCLXVI'
print(a.to_roman(86))  # 'LXXXVI'
print(a.to_roman(1))  # 'I'

# From Roman
print(a.from_roman("MM"))  # 2000
print(a.from_roman("MDCLXVI"))  # 1666
print(a.from_roman("LXXXVI"))  # 86
print(a.from_roman("I"))  # 1
