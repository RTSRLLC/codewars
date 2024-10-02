import random
import array
from collections import deque


class Stack:
	"""
	A class used to represent a Stack data structure.

	Attributes
	----------
	stack : list
		A list to store the elements of the stack.
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
	
	def push(self, item):
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


def generate_random_list(n, min_val, max_val):
	the_list = [random.randint(min_val, max_val) for _ in range(n)]
	the_list.append(the_list[0])  # to create a duplicate number in the list
	return [random.randint(min_val, max_val) for _ in range(n)]


int_list = generate_random_list(100, 1, 100)
print(f"int_list\n{'*' * len(int_list)}")
############################################################################################################

one = "check if integer x is in a list"
integ = 7
print(f"7 is in list: {7 in int_list}")
print(f"{one=}\n{'*' * len(one)}")
############################################################################################################

two = "find duplicate number in a integer list"
b_int_dup_set_2 = set(i for i in int_list if int_list.count(i) > 1)
print(f"{two=}\n{'*' * len(two)}")
############################################################################################################

three = "check if 2 strings are anagrams"
str1 = "listen"
str2 = "silent"
print(f"are {str1} and {str2} anagrams?: {sorted(list(str1)) == sorted(list(str2))}")
print(f"{three=}\n{'*' * len(three)}")
############################################################################################################

four = "find pairs in a list that sum to a target value"
target = 15
set_list = set(int_list)
sum_pair_set = {(i, x) for i in set_list if (x := target - i) in set_list}
print(f"unique pairs: {sum_pair_set}")
print(f"{four=}\n{'*' * len(four)}")
############################################################################################################

five = "check if a string is a palindrome"
palindrome = "racecar"
print(f"is palindrome: {list(palindrome) == list(palindrome)[::-1]}")
print(f"{five=}\n{'*' * len(five)}")
############################################################################################################
six = "use a list as stack, array, and queue"
print(f"{six=}\n{'*' * len(six)}")

stackin = Stack(int_list)
stackin.push(1_000_000)
the_peek = stackin.peek()
print(stackin.size())
print(stackin.__repr__())
stackin.pop()

array_int_list = array.array('i', int_list)
print(array_int_list.buffer_info())
item_51 = array_int_list[51]

deq_int_list = deque(int_list)
print(f"{[i for i in dir(deq_int_list) if not i.startswith('_')]=}")
print(deq_int_list[0])
deq_int_list.appendleft(1_000_000)
print(deq_int_list[0])
deq_first = deq_int_list.popleft()
print(deq_int_list[0])
print(f"{six=}\n{'*' * len(six)}")
############################################################################################################
