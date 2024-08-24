"""
subtract each vector, take the ||v|| = sqrt(v1^2 + v2^2) then get minimum distance and those two points are the closest
"""


def closest_pair(points):
	# Your code here!
	pass


a = closest_pair(
	((2, 2),  # A
	 (2, 8),  # B
	 (5, 5),  # C
	 (6, 3),  # D
	 (6, 7),  # E
	 (7, 4),  # F
	 (7, 9)  # G
	 )
	)  # ((6, 3), (7, 4))

b = closest_pair(
	((2, 2),  # A
	 (2, 8),  # B
	 (5, 5),  # C
	 (5, 5),  # C
	 (6, 3),  # D
	 (6, 7),  # E
	 (7, 4),  # F
	 (7, 9)  # G
	 )
	)  # ((5, 5), (5, 5))
