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
a_int_list_sorted = sorted(int_list.copy())
b_int_dup_set = set()
int_list_enum = list(enumerate(a_int_list_sorted))
for i, n in int_list_enum:
	try:
		if a_int_list_sorted[i + 1] == n:
			b_int_dup_set.add(n)
	except IndexError:
		continue
b_int_dup_set_2 = set()
for i in int_list:
	print(f"{i=}\n{int_list.count(i)=}\n{'*'*10}")
	if int_list.count(i) > 1:
		b_int_dup_set_2.add(i)
print(f"{sorted(b_int_dup_set_2) == b_int_dup_set_2}")