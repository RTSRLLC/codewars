def plural_or_not(num, word):
	if num == 0:
		return "now"
	if num == 1:
		return str(num) + " " + word
	return str(num) + " " + word + "s"


def format_duration(seconds):
	# nums.append(str(the_num) + " year," if the_num == 1 else str(the_num) + " years,")
	times = [(31536000, 'year'), (86400, 'day'), (3600, 'hour'), (60, 'minute'), (1, 'second')]
	nums = []  # [6, 192, 13, 3, 54]
	for time in times:
		division = seconds // time[0]
		if division < 0:
			continue
		nums.append((division, time[1]))
		seconds -= division * time[0]
	print(nums)
	nums = [n for n in nums if n[0] != 0]
	for n in nums_copy[::-1]:
		if n[0] == 0:
			nums.remove(n)
	nums2_copy = nums.copy()[::-1]
	for n in nums2_copy:
		print(n)
		if n[0] > 1:
			new_word = list(n[1])
			new_word.append("s")
			nums[n[1]].replace(n[1], "".join(new_word))
	
	print(nums2_copy)


# a = format_duration(0)  # , "now")
# b = format_duration(1)  # , "1 second")
# c = format_duration(62)  # , "1 minute and 2 seconds")
# d = format_duration(120)  # , "2 minutes")
# e = format_duration(3600)  # , "1 hour")
# f = format_duration(3662)  # , "1 hour, 1 minute and 2 seconds")
# g = format_duration(15731080)  # , "182 days, 1 hour, 44 minutes and 40 seconds")
h = format_duration(132030240)  # , "4 years, 68 days, 3 hours and 4 minutes")  #'4 years, 68 days, 3 hours, 4 minutes'
# i = format_duration(205851834)  # , "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
# j = format_duration(253374061)  # , "8 years, 12 days, 13 hours, 41 minutes and 1 second")
# k = format_duration(242062374)  # , "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
