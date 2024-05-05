def format_duration(seconds):
	def length_nums(alist, length):
		years = str(nums[0]) + " year" if nums[0] == 1 else str(nums[0]) + " years"
		days = str(nums[1]) + " day" if nums[1] == 1 else str(nums[1]) + " days"
		hours = str(nums[2]) + " hour" if nums[2] == 1 else str(nums[2]) + " hours"
		minutes = str(nums[3]) + " minute" if nums[3] == 1 else str(nums[3]) + " minutes"
		second = str(nums[4]) + " second" if nums[4] == 1 else str(nums[4]) + " seconds"
	
	the_num = 0
	nums = []
	if seconds == 0:
		return "now"
	if seconds >= secs_in_year:
		the_num = seconds // 31536000
		nums.append(the_num)
		seconds -= the_num * 31536000
	if seconds >= secs_in_day:
		the_num = seconds // 86400
		nums.append(the_num)
		seconds -= the_num * 86400
	if seconds >= secs_in_hour:
		the_num = seconds // 3600
		nums.append(the_num)
		seconds -= the_num * 3600
	if seconds >= secs_in_min:
		the_num = seconds // 60
		nums.append(the_num)
		seconds -= the_num * 60
	if seconds > 0:
		nums.append(seconds)
	
	return ", ".join([years, days, hours, minutes, second])


# a = format_duration(0)  # , "now")
# b = format_duration(1)  # , "1 second")
# c = format_duration(62)  # , "1 minute and 2 seconds")
# d = format_duration(120)  # , "2 minutes")
# e = format_duration(3600)  # , "1 hour")
# f = format_duration(3662)  # , "1 hour, 1 minute and 2 seconds")
# g = format_duration(15731080)  # , "182 days, 1 hour, 44 minutes and 40 seconds")
# h = format_duration(132030240)  # , "4 years, 68 days, 3 hours and 4 minutes")
# i = format_duration(205851834)  # , "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
j = format_duration(253374061)  # , "8 years, 12 days, 13 hours, 41 minutes and 1 second")
k = format_duration(242062374)  # , "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
