def format_duration(seconds):
	
	the_num = 0
	nums = []
	if seconds == 0:
		return "now"
	if seconds == 1:
		return "1 second"
	if seconds >= 31536000:
		the_num = seconds // 31536000
		seconds -= the_num * 31536000
		if seconds == 0:
			nums.append(str(the_num) + " year" if the_num == 1 else str(the_num) + " years")
			nums[-1].replace(" and ", "")
			return " and ".join(i for i in nums)
		nums.append(str(the_num) + " year," if the_num == 1 else str(the_num) + " years,")
	if seconds >= 86400:
		the_num = seconds // 86400
		seconds -= the_num * 86400
		if seconds == 0:
			nums.append(str(the_num) + " day" if the_num == 1 else str(the_num) + " days")
			nums[-1].replace(" and ", "")
			return " and ".join(i for i in nums)
		nums.append(str(the_num) + " day," if the_num == 1 else str(the_num) + " days,")
	if seconds >= 3600:
		the_num = seconds // 3600
		seconds -= the_num * 3600
		if seconds == 0:
			nums.append(str(the_num) + " hour" if the_num == 1 else str(the_num) + " hours")
			nums[-1].replace(" and ", "")
			return "".join(i for i in nums)
		nums.append(str(the_num) + " hour," if the_num == 1 else str(the_num) + " hours,")
	if seconds >= 60:
		the_num = seconds // 60
		seconds -= the_num * 60
		if seconds == 0:
			if len(nums) == 0:
				nums.append(str(the_num) + " minute" if the_num == 1 else str(the_num) + " minutes")
				return " ".join(i for i in nums)
			nums.append(" and " + str(the_num) + " minute" if the_num == 1 else " and " + str(the_num) + " minutes")
			return " ".join(i for i in nums)
		nums.append(str(the_num) + " minute" if the_num == 1 else str(the_num) + " minutes")
	if 1 <= seconds < 60:
		if seconds == 1:
			nums.append(" and " + str(seconds) + " second")
			nums[-1].replace(" and ", "")
			return " ".join(i for i in nums)
		the_num = seconds
		nums.append(" and " + str(the_num) + " second" if the_num == 1 else " and " + str(the_num) + " seconds")
		return " ".join(i for i in nums)


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
