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
		a_sum = 0
		lis = [i for i in roman_num]
		pair_list = []
		print(f'List: {lis}')
		print(f"RomanNumerals: {RomanNumerals.ROMAN_NUMERALS}")
		# {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
		# 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
		pairwise_pairs = pairwise(lis)
		# answer is 659: c = 500, l = 50, i = 1, x = 10, i = 1, x = 10, i = 1
		for pair in pairwise_pairs:  # [('D', 'C'), ('C', 'L'), ('L', 'I'), ('I', 'X')]
			previous_pair = []
			break_apart_value = []
			pair_list.append(''.join(pair))
			print(f"Pair List: {pair_list}")
			# see if the pair is in the dictionary, if yes, add the value to the sum and continue to next value
			if pair_list[0] in RomanNumerals.ROMAN_NUMERALS:
				a_sum += RomanNumerals.ROMAN_NUMERALS[''.join(pair)]
				pair_list.clear()
				print(f"Output List: {a_sum}")
				continue
			else:  # if not, check if the next pairwise value is in the dictionary
				previous_pair.append(
					''.join(pair)
					)  # store precious value in the event that next value NOT in the dictionary
				if ''.join(next(pair)) in RomanNumerals.ROMAN_NUMERALS:  # if yes, split previous value, add first
					# value to
					# sum then add the second value to the sum
					a_sum += RomanNumerals.ROMAN_NUMERALS[previous_pair]
					print(f"Output List: {a_sum}")
					# clear acurrent_value
					previous_pair.clear()
					continue
				else:  # if not add, break up previous available value and add the first value to the sum
					break_apart_value.append(i for i in previous_pair)
		
		# output += sum(map(lambda x: RomanNumerals.ROMAN_NUMERALS[x], keep_next_value))
		return pairwise_pairs


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
