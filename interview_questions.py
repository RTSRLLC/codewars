import random
import math
import array
from collections import deque


class Stack:
	"""
	A class used to represent a Stack data structure.

	Attributes
	----------
	stack : list
		A list to store the elements of the stack.

	Methods
	-------
	__init__(self, a_list: list)
		Initializes the stack with a given list.

	push(self, item: any)
		Adds an element to the top of the stack.

	pop(self)
		Removes the top element from the stack.

	peek(self)
		Prints the top element of the stack without removing it.

	size(self)
		Returns the number of elements in the stack.

	__repr__(self)
		Returns a string representation of the stack.
	"""
	
	def __init__(self, a_list: list):
		"""
		Initializes the stack with a given list.

		Parameters
		----------
		a_list : list
			A list of elements to initialize the stack with.
		"""
		self.stack = a_list
	
	def push(self, item: any):
		"""
		Adds an element to the top of the stack.

		Parameters
		----------
		item : any
			The element to be added to the stack.
		"""
		self.stack.append(item)
	
	def pop(self):
		"""
		Removes the top element from the stack.
		"""
		self.stack.pop()
	
	def peek(self):
		"""
		Prints the top element of the stack without removing it.
		"""
		print(self.stack[-1])
	
	def size(self):
		"""
		Returns the number of elements in the stack.

		Returns
		-------
		int
			The number of elements in the stack.
		"""
		return len(self.stack)
	
	def __repr__(self):
		"""
		Returns a string representation of the stack.

		Returns
		-------
		str
			A string representation of the stack.
		"""
		return repr(self.stack)


def one(the_list: list, x: int) -> str:
	ones = "check if integer x is in a list"
	return f"{ones}\n{x in int_list}\n{'*' * 72}"


def two(the_list: list) -> str:
	two = "find duplicate number in a integer list"
	return f"{two}\n{set(i for i in the_list if the_list.count(i) > 1)}\n{'*' * 72}"


def three(str1: str, str2: str) -> str:
	three = "check if 2 strings are anagrams"
	return f"{three}\nare {str1} and {str2} anagrams?\n{sorted(list(str1)) == sorted(list(str2))}\n{'*' * 72}"


def four(the_list: list, target: int) -> str:
	"""
	Finds pairs of numbers in a list that sum to a target value.

	Parameters
	----------
	the_list : list
		A list of integers to search for pairs.
	target : int
		The target sum value for which pairs are to be found.

	Returns
	-------
	str
		A formatted string describing the function's purpose and listing the pairs of numbers
		that sum to the target value.
	"""
	four = "find pairs in a list that sum to a target value"
	set_list = set(int_list)
	return f"{four}\n{(list((i, x) for i in set_list if (x := target - i) in set_list))}\n{'*' * 72}"


def five(palindrome: str) -> str:
	"""
	Checks if a given string is a palindrome.

	Parameters
	----------
	palindrome : str
		The string to be checked for palindrome properties.

	Returns
	-------
	str
		A formatted string indicating whether the input string is a palindrome.
	"""
	five = "check if a string is a palindrome"
	return f"{five}\nis palindrome: {list(palindrome) == list(palindrome)[::-1]}\n{'*' * 72}"


def six(int_list: list) -> str:
	six = "use a list as stack, array, and queue"
	
	stackin = Stack(int_list)
	print(f"stackin docstring:\n{stackin.__doc__}\n{'*' * 72}")
	stackin.push(1_000_000)
	print(f"{stackin.peek()=}")
	print(f"{stackin.size()=}")
	print(f"{stackin.__repr__()=}")
	stackin.pop()
	print(f"{stackin.size()=}")
	
	array_int_list = array.array('i', int_list)
	print(f"{array_int_list[51]=}")
	
	deq_int_list = deque(int_list)
	print(f"{deq_int_list[0]=}")
	deq_int_list.appendleft(1_000_000)
	print(f"{deq_int_list[0]=}")
	deq_int_list.popleft()
	print(f"{deq_int_list[0]=}")
	return f"{six}\n{'*' * 72}"


def seven(int_list: list) -> str:
	"""
	This function identifies and returns the missing numbers in a sequence.

	Parameters:
	int_list (list): A list of integers representing a sequence.

	Returns:
	str: A formatted string containing the missing numbers in the sequence. The string also includes a check to ensure the sum of the found missing numbers
	and the sorted list length equals the length of the complete set.
	"""
	seven = "get missing numbers in a sequence"
	sorted_list = sorted(int_list)
	sorted_set = set(sorted_list)
	complete_set = [i for i in range(sorted_list[0], sorted_list[-1] + 1)]
	complete_set_set = set(complete_set)
	missing_numbers = [j for j in complete_set if j not in sorted_set]
	missing_numbers2 = complete_set_set - sorted_set
	return (f"{seven}\nMissing numbers: {missing_numbers}\nMissing numbers (set): {missing_numbers2}\n{'*' * 72}\nlengths add to complete_set: "
	        f"{len(sorted_set) + len(missing_numbers) == len(complete_set)}")


def eight(int_list: list) -> str:
	eight = "compute the intersection of two lists"
	intersection = set(int_list) & set(generate_random_list(10, 1, 100))
	return f"{eight}\nIntersection: {intersection}\n{'*' * 72}"


def nine(int_list: list) -> str:
	nine = "find max and min in an unsorted list"
	return f"{nine}\nMax: {max(int_list)}, Min: {min(int_list)}\n{'*' * 72}"


def ten(s: str) -> str:
	"""
	This function reverses a given string using recursion.

	Parameters:
	s (str): The string to be reversed.

	Returns:
	str: A string that is the reverse of the input string. The returned string includes a brief description of the function's purpose, the reversed string
	using Python's built-in reversed function, and the reversed string using recursion.
	"""
	ten = "reverse string using recursion"
	
	def reverse_string_with_recursion(s: str, t=None) -> str:
		"""
		A helper function that reverses a string using recursion.

		Parameters:
		s (str): The string to be reversed.
		t (str, optional): An accumulator string used to build the reversed string. Defaults to None.

		Returns:
		str: The reversed string.
		"""
		if not t:
			t = ''
		t += list(s).pop() if len(list(s)) >= 1 else ''
		return reverse_string_with_recursion(s[:-1], t=t) if list(s) else t
	
	run_it = reverse_string_with_recursion(s=s, t=None)
	return f"{ten}\nthe str reversed: {''.join(list(reversed(s)))}\nRev str recursed: {run_it}\n{'*' * 72}"


def eleven_(n: int) -> str:
	"""
	Computes the first n Fibonacci numbers.

	Parameters:
	----------
	n : int
		The number of Fibonacci numbers to compute. Must be a positive integer.

	Returns:
	-------
	str
		A string containing the first n Fibonacci numbers. The string is formatted with a brief description of the function's purpose,
		the computed Fibonacci numbers, and a horizontal rule for readability.
	"""
	eleven = "compute the first n fibonacci numbers"
	
	def fibonacci(n: int = None, n_list: list = None, og: int = None) -> list:
		"""
		A helper function to compute the Fibonacci numbers.

		Parameters:
		----------
		n : int
			The number of Fibonacci numbers to compute. Must be a positive integer.
		n_list : list
			A list to store the computed Fibonacci numbers. Defaults to [0, 1].
		og : int
			The original value of n passed to the main function. Used to determine when to stop recursion.

		Returns:
		-------
		list
			A list containing the first n Fibonacci numbers.
		"""
		if not n_list:
			n_list = [0, 1]
		da_sum = sum(n_list[-2:])
		n_list.append(da_sum)
		return fibonacci(n - 1, n_list, og=og) if len(n_list) < og else n_list
	
	out = fibonacci(n=n, n_list=None, og=10)
	return f"{eleven}\nFirst {n} Fibonacci numbers: {out}\n{'*' * 72}"


def twelve_(the_list: list) -> str:
	twelve = 'sort list with quicksort algorithm'
	
	def quick_sort(a_list: list = None):
		if a_list:
			pivot = a_list.pop()
			greater = [x for x in a_list if x > pivot]
			lesser = [x for x in a_list if x <= pivot]
			return quick_sort(lesser) + [pivot] + quick_sort(greater)
		else:
			return []
	
	my_list = quick_sort(the_list)
	return f"{twelve}\nSorted list: {my_list}\n{'*' * 72}"


def thirteen_permutations(s: str) -> list:
	"""
	Generates all possible permutations of a given string.

	Parameters:
	----------
	s : str
		The input string for which to generate permutations.

	Returns:
	-------
	list
		A list of strings, where each string is a unique permutation of the input string.
		The order of the permutations in the list is not guaranteed to be consistent.

	Notes:
	-----
	This function removes any whitespace characters from the input string before generating permutations.
	The function uses a simple algorithm that repeatedly rotates the characters in the string to generate permutations.
	"""
	lis = [i for i in s if i != ' ']
	out = []
	count = len(lis)
	while count > 0:
		out.append("".join(lis))
		da_pop = lis.pop(0)
		lis.append(da_pop)
		count -= 1
	return out


def generate_random_list(n, min_val, max_val):
	the_list = [random.randint(min_val, max_val) for _ in range(n)]
	the_list.append(the_list[0])  # to create a duplicate number in the list
	return [random.randint(min_val, max_val) for _ in range(n)]


int_list = generate_random_list(100, 1, 100)
############################################################################################################
print(one(the_list=int_list, x=7))
############################################################################################################
print(two(the_list=int_list))
############################################################################################################
print(three(str1="listen", str2="silent"))
############################################################################################################
print(four(the_list=int_list, target=15))
############################################################################################################
print(five(palindrome="racecar"))
############################################################################################################
print(six(int_list))
###########################################################################################################
print(seven(int_list))
###########################################################################################################
print(eight(int_list))
############################################################################################################
print(nine(int_list))
#################################################################################################
print(ten(s="".join(str(i) for i in sorted(set(int_list))[:20])))
############################################################################################
print(eleven_(n=10))
#########################################################################################
print(twelve_(the_list=int_list))
#########################################################################################
thirteen = "for all possible permutations of a string"
print(
	f"{thirteen}\n"
	f"number perms should be:"
	f"{math.prod(i for i in range(1, len([i for i in thirteen if i != ' ']) + 1)) / math.prod(i for i in range(1, len([i for i in thirteen if i != ' '])))}\n"
	f"{(the_function := thirteen_permutations(thirteen))}\n{len(the_function)=}\n{'*' * 72}"
	)
#########################################################################################
