import time


def get_random_points(n: int) -> tuple:
	import random
	random.seed(911)
	return tuple((random.randint(1, 100), random.randint(1, 100)) for _ in range(n))


def closest_pair(points: tuple) -> tuple:
	"""
	Finds the closest pair of points from a given set of points using a divide and conquer approach.

	Parameters:
	points (tuple): A tuple of points where each point is represented as a tuple of two integers (x, y).

	Returns:
	tuple: A tuple containing the two closest points.
	"""
	
	# calc the dist between 2 points
	def distance(p1, p2):
		return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
	
	def closest_pair_rec(points_sorted_by_x: list, points_sorted_by_y: list) -> tuple:
		n = len(points_sorted_by_x)
		
		# brute it for a small number
		if n <= 20:
			return min(
				(distance(p1, p2), p1, p2)
				for i, p1 in enumerate(points_sorted_by_x)
				for p2 in points_sorted_by_x[i + 1:]
				)
		
		# Divide into two halves
		mid = n // 2
		mid_x = points_sorted_by_x[mid][0]
		
		left_half = points_sorted_by_x[:mid]
		right_half = points_sorted_by_x[mid:]
		
		# Recursively call for each half
		closest_left = closest_pair_rec(left_half, [p for p in points_sorted_by_y if p[0] <= mid_x])
		closest_right = closest_pair_rec(right_half, [p for p in points_sorted_by_y if p[0] > mid_x])
		
		# Find the smallest distance
		d = min(closest_left[0], closest_right[0])
		closest = closest_left if closest_left[0] < closest_right[0] else closest_right
		
		# Build points close to dividing line
		strip = [p for p in points_sorted_by_y if abs(p[0] - mid_x) < d]
		
		# Check the strip for closer pairs
		for i in range(len(strip)):
			for j in range(i + 1, min(i + 7, len(strip))):  # Compare at most 6 neighbors
				dist = distance(strip[i], strip[j])
				if dist < closest[0]:
					closest = (dist, strip[i], strip[j])
		
		return closest
	
	# Sort by x/y coord
	points_sorted_by_x = sorted(points, key=lambda p: p[0])
	points_sorted_by_y = sorted(points, key=lambda p: p[1])
	
	return closest_pair_rec(points_sorted_by_x, points_sorted_by_y)[1:]


start_time = time.time()

rand_points = get_random_points(22)
a = closest_pair(get_random_points(22))

end_time = time.time()
print("Time taken: ", (end_time - start_time) * 1000)
