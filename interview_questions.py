import random
import array
import queue
from collections import deque


def generate_random_list(n, min_val, max_val):
	the_list = [random.randint(min_val, max_val) for _ in range(n)]
	the_list.append(the_list[0])  # to create a duplicate number in the list
	return [random.randint(min_val, max_val) for _ in range(n)]


int_list = generate_random_list(100, 1, 100)

one = "check if integer x is in a list"
integ = 7
print(f"7 is in list: {7 in int_list}")

two = "find duplicate number in a integer list"
b_int_dup_set_2 = set(i for i in int_list if int_list.count(i) > 1)

three = "check if 2 strings are anagrams"
str1 = "listen"
str2 = "silent"
print(f"are {str1} and {str2} anagrams?: {sorted(list(str1)) == sorted(list(str2))}")

four = "find pairs in a list that sum to a target value"
target = 15
set_list = set(int_list)
sum_pair_set = {(i, x) for i in set_list if (x := target - i) in set_list}
print(f"unique pairs: {sum_pair_set}")

five = "check if a string is a palindrome"
palindrome = "racecar"
print(f"is palindrome: {list(palindrome) == list(palindrome)[::-1]}")

six = "use a list as stack, array, and queue"
# Here are the definitions:
# 1. **Stack**:
#    - A stack is a data structure that follows the Last In, First Out (LIFO) principle. The most recently added element is the one that is removed first.
#    - Operations:
#      - **Push**: Add an element to the top.
#      - **Pop**: Remove the element from the top.
#      - **Peek/Top**: View the top element without removing it.
# 2. **Array**:
#    - An array is a collection of elements, all of the same type, stored in contiguous memory locations. Each element can be accessed using an index.
#    - Operations:
#      - Accessing elements by index (e.g., `arr[0]`).
#      - Inserting and deleting elements (though this can be inefficient if not handled carefully).
# 3. **Queue**:
#    - A queue is a data structure that follows the First In, First Out (FIFO) principle. The first element added is the first one to be removed.
#    - Operations:
#      - **Enqueue**: Add an element to the back.
#      - **Dequeue**: Remove an element from the front.
#      - **Peek/Front**: View the front element without removing it.
# Each has different use cases depending on how you want to manage data.
array_int_list = array.array('i', int_list)

