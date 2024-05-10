def final_item_in_list(lst: list) -> list:
	"""
	Modifies the last item of a list to include 'and' before it, formatting it for grammatical correctness in a sentence.

	This function checks if the list contains only one item, in which case it returns the list unchanged. If the list
	contains more than one item, it removes the last item, appends a new string that combines 'and' with the removed
	item, and returns the modified list. This is particularly useful for formatting lists of items in written text.

	Parameters:
	- lst (list): The list to be modified.

	Returns:
	- list: The modified list with 'and' added before the last item.
	"""
	if len(lst) == 1:
		return lst
	final = lst.pop()
	lst.append(f"and {final}")
	return lst


def commas(lst: list) -> list:
	"""
	Adds commas to each element in a list except for the last two elements.

	This function iterates through the list and appends a comma to each element, except for the last two elements,
	to facilitate proper grammar in a list format when converted to a string. This is particularly useful for
	formatting lists of items in a sentence where commas are needed between items except before the last item,
	which is typically preceded by "and".

	Parameters:
	- lst (list): A list of strings to be modified with commas.

	Returns:
	- list: The modified list with commas added to each element except for the last two.
	"""
	for i, s in enumerate(lst[:-2]):
		lst[i] += ","
	return lst


def plural_or_not(lst: list) -> list:
	"""
	Adjusts the pluralization of time units in a list based on their quantities.

	This function iterates through a list of strings, each representing a quantity and its corresponding time unit
	(e.g., "1 year", "2 minutes"). It ensures that the time unit is correctly pluralized (or not) based on its quantity.
	Specifically, it singularizes units that are preceded by the number 1, except in cases where the "1" is part of a
	larger number (e.g., "11 years" remains unchanged).

	Parameters:
	- lst (list): A list of strings, where each string contains a numerical quantity followed by a time unit.

	Returns:
	- list: The modified list with correctly pluralized (or singularized) time units.
	"""
	for i, s in enumerate(lst):
		if int(s[0]) == 1 and s[1].isnumeric():
			continue
		elif int(s[0]) == 1 and not s[1].isnumeric():
			lst[i] = s[:-1]
	return lst


def division(seconds: int) -> list:
	"""
	Breaks down a duration in seconds into larger time units such as years, days, hours, minutes, and seconds.

	This function iterates through predefined time units, calculating how many full units fit into the total
	duration specified by `seconds`. It accumulates these calculations as tuples of (quantity, unit) in a list,
	which it returns. The function ensures that only non-zero quantities are included, effectively omitting
	units that do not contribute to the total duration.

	Parameters:
	- seconds (int): The total duration in seconds to be broken down into larger time units.

	Returns:
	- list: A list of tuples, where each tuple contains two elements:
		1. An integer representing the quantity of the time unit.
		2. A string representing the name of the time unit (e.g., 'years', 'days').
	"""
	times = [(31536000, 'years'), (86400, 'days'), (3600, 'hours'), (60, 'minutes'), (1, 'seconds')]
	nums = []
	for time in times:
		division = seconds // time[0]
		if division < 0:
			continue
		nums.append((division, time[1]))
		seconds -= division * time[0]
	return nums


def format_duration(seconds):
	"""
	Formats a duration given in seconds into a human-readable string that represents
	the equivalent time in years, days, hours, minutes, and seconds.

	The function breaks down the total seconds into larger time units where applicable,
	and formats the result as a string in a readable format, such as "1 hour, 1 minute and 2 seconds".
	It handles pluralization correctly, ensuring that units are pluralized only when the quantity is not one.
	The function also correctly formats the string with commas and the word "and" as necessary.

	Parameters:
	- seconds (int): The total duration in seconds to be formatted.

	Returns:
	- str: A human-readable string representing the duration in years, days, hours, minutes, and seconds.
		   Returns "now" if the duration is 0 seconds.
	"""
	if seconds == 0:
		return "now"
	nums = division(seconds)
	nums = [f"{str(n[0])} {n[1]}" for n in nums if n[0] != 0]
	nums = plural_or_not(nums)
	nums = final_item_in_list(nums)
	nums = commas(nums)
	return " ".join(nums)


a = format_duration(0)  # , "now")
b = format_duration(1)  # , "1 second")
c = format_duration(62)  # , "1 minute and 2 seconds")
d = format_duration(120)  # , "2 minutes")
e = format_duration(3600)  # , "1 hour")
f = format_duration(3662)  # , "1 hour, 1 minute and 2 seconds")
g = format_duration(15731080)  # , "182 days, 1 hour, 44 minutes and 40 seconds")
h = format_duration(132030240)  # , "4 years, 68 days, 3 hours and 4 minutes")  #'4 years, 68 days, 3 hours, 4 minutes'
i = format_duration(205851834)  # , "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
j = format_duration(253374061)  # , "8 years, 12 days, 13 hours, 41 minutes and 1 second")
k = format_duration(242062374)  # , "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
