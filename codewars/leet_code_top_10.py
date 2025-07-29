# - **Two Sum (Easy)**
#   - Given an array of integers and a target sum, find two numbers in the array that add up to the target.
#   - Return the indices of the two numbers as an array.
#   - Assume exactly one valid solution exists, and you cannot use the same element twice.
import numpy as np

targ = 5585
arr = [8758, 4423, 7993, 4019, 4421, 1162, 7812]

for idx, val in sorted(list(enumerate(arr.copy()))):
    d = abs(targ - val)
    n = d in arr
    if n:
        loc = arr.index(d)
        print(f"{targ} -> index {arr.index(val)} + index {arr.index(d)} = {arr[idx] + arr[loc]}")
        break


# num_1 = targ - arr_reduced
# num_2 = targ - num_1
# test = num_1 + num_2 == np.array(targ * len(num_1))

# - **Add Two Numbers (Medium)**
#   - Given two non-empty linked lists representing non-negative integers (digits stored in reverse order), add the two numbers and return the sum as a linked list.
#   - Each node contains a single digit, and there are no leading zeros except for the number zero itself.


# - **Longest Substring Without Repeating Characters (Medium)**
#   - Given a string, find the length of the longest substring that contains no repeating characters.
#   - The substring must be contiguous, and you need to track unique characters in each substring.


# - **Longest Palindromic Substring (Medium)**
#   - Given a string, find the longest substring that is a palindrome (reads the same forward and backward).
#   - Return the substring itself, not just its length.
#   - Assume the string length is at most 1000.


# - **Reverse Integer (Medium)**
#   - Given a 32-bit signed integer, reverse its digits and return the result.
#   - If the reversed integer overflows (i.e., is outside the 32-bit signed integer range [-2³¹, 2³¹-1]), return 0.
#   - Handle negative numbers by preserving the sign.


# - **String to Integer (atoi) (Medium)**
#   - Implement a function to convert a string to a 32-bit signed integer (similar to C/C++ atoi).
#   - Handle leading whitespace, optional plus/minus signs, and numerical digits.
#   - Ignore non-numeric characters after the number and return 0 for invalid input.
#   - If the result is out of the 32-bit signed integer range, return the closest bound (INT_MIN or INT_MAX).


# - **Regular Expression Matching (Hard)**
#   - Given a string and a pattern, determine if the string matches the pattern, where the pattern may include '.' (matches any single character) and '*' (matches zero or more of the preceding character).
#   - The entire string must match the pattern (not a partial match).


# - **Container With Most Water (Medium)**
#   - Given an array of non-negative integers representing heights of vertical lines, find two lines that, together with the x-axis, form a container that holds the most water.
#   - The area is calculated as the minimum height of the two lines multiplied by the distance between them.
#   - Return the maximum possible area.


# - **Roman to Integer (Easy)**
#   - Given a Roman numeral string (using symbols I, V, X, L, C, D, M), convert it to an integer.
#   - Roman numerals follow specific rules: symbols are usually additive, but if a smaller value precedes a larger one, subtract the smaller value (e.g., IV = 4, not 6).
#   - Input is guaranteed to be a valid Roman numeral within the range [1, 3999].


# - **Letter Combinations of a Phone Number (Medium)**
#   - Given a string of digits (2-9), return all possible letter combinations that the number could represent based on a phone keypad mapping (e.g., 2 maps to "abc", 3 to "def").
#   - Return the combinations as a list of strings.
#   - The input string length is at most 4, and each digit maps to 3 or 4 letters.