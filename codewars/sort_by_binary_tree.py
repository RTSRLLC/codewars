class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n


def tree_by_levels(node):
	if node is None:
		return []
	print(vars(node))
	print(node.__dict__)
	print(node.__dict__.keys())
	
	print(vars(node.left))
	return 1


a = tree_by_levels(None)  # , [])
# , [1, 2, 3, 4, 5, 6])
b = tree_by_levels(
	Node(
		L=Node(
			L=None,
			R=Node(
				L=None, R=None, n=4
				),
			n=2
			),
		R=Node(
			Node(
				L=None, R=None, n=5
				),
			Node(
				L=None, R=None, n=6
				), n=3
			), n=1  # level one
		)
	)
c = Node(L=1, R=2, n=3)
