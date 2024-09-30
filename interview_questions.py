import random


def generate_random_list(n, min_val, max_val):
	the_list = [random.randint(min_val, max_val) for _ in range(n)]
	the_list.append(the_list[0])  # to create a duplicate number in the list
	return [random.randint(min_val, max_val) for _ in range(n)]


int_list = generate_random_list(100, 1, 100)

one = "check if integer x is in a list"
integ = 7
print(7 in int_list)

two = "find duplicate number in a integer list"
int_list_sorted = sorted(int_list)