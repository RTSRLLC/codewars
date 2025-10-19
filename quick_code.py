# what combination of 3 nums completes: _ + _ + _ = 30
nums = [1, 3, 5, 7, 9, 11, 13, 15]
copy = nums.copy()

sums = [i * 2 for i in nums]
triple_sums = [i * 3 for i in nums]

reverse_copy = nums[::-1]
sums_dict = {}
for i in range(len(nums)):
    vals = []
    while reverse_copy:
        v = reverse_copy.pop() + nums[i]
        vals.append(v)
    sums_dict[nums[i]] = vals
    reverse_copy = nums[::-1]

subtraction_dict = {}
for i in range(len(nums)):
    vals = []
    while reverse_copy:
        v = reverse_copy.pop() - nums[i]
        vals.append(v)
    subtraction_dict[nums[i]] = vals
    reverse_copy = nums[::-1]