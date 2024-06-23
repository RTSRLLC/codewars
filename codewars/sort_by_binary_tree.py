class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n


def branch(current_node: dict):
	return dict(list(current_node.items()))


def tree_by_levels(node):
	if node is None:
		return []
	out = []
	current_branch = {}
	print(repr(vars(node)))
	the_node = branch(vars(node))
	for k, v in vars(node).items():
		if k == 'left':
			print(type(v))
			if type(v) == Node:
				current_branch[1] = [v]
		elif k == 'right':
			if type(v) == Node:
				current_branch[1].append(v)
		elif k == 'value':
			out.append(v)
	return out


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
