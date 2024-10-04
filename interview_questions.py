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


def generate_random_list(n, min_val, max_val):
	the_list = [random.randint(min_val, max_val) for _ in range(n)]
	the_list.append(the_list[0])  # to create a duplicate number in the list
	return [random.randint(min_val, max_val) for _ in range(n)]


int_list = generate_random_list(100, 1, 100)
print(f"int_list\n{'*' * len(int_list)}")
############################################################################################################
def one(the_list: list, x: int) -> str:
	ones = "check if integer x is in a list"
	return f"{ones}\n{x in int_list}\n{'*' * 72}"
print(one(the_list=int_list, x=7))
############################################################################################################
def two(the_list: list) -> str:
	two = "find duplicate number in a integer list"
	return f"{two}\n{set(i for i in the_list if the_list.count(i) > 1)}\n{'*' * 72}"
print(two(the_list=int_list))
############################################################################################################
def three(str1: str, str2: str) -> str:
	three = "check if 2 strings are anagrams"
	return f"{three}\nare {str1} and {str2} anagrams?\n{sorted(list(str1)) == sorted(list(str2))}\n{'*' * 72}"
print(three(str1="listen", str2="silent"))
############################################################################################################
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
print(four(the_list=int_list, target=15))
############################################################################################################
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
print(five(palindrome="racecar"))
############################################################################################################
def six(int_list: list) -> str:
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
	return f"{six}\n{'*' * 72}"
############################################################################################################
a = [1, 2, 2, 3]
b = [1, 3]
set_a = set(a)
set_b = set(b)
print(f"{a} - {b} = {set_a - set_b}")