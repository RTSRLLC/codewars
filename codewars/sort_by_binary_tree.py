import inspect


class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n


def branch(current_node: dict):
	return dict(list(current_node.items()))


def tree_by_levels(node):
	# Get the current frame
	frame = inspect.currentframe()
	# Get the function arguments and their values
	args, _, _, values = inspect.getargvalues(frame)
	
	# Use the function signature to get argument names in the correct order
	func_name = inspect.currentframe().f_code.co_name
	func = globals()[func_name]
	sig = inspect.signature(func)
	params = sig.parameters
	
	# Create a string with the arguments and their values
	args_str = ', '.join(f"{param}={values[param]!r}" for param in params)
	
	# Print the arguments string
	print(f"Arguments: {args_str}")
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
