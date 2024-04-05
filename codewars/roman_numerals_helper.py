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
