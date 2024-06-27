from typing import Optional, List


class Node:
	def __init__(self, L, R, n):
		self.left = L
		self.right = R
		self.value = n


def tree_by_levels(node: Optional[Node]) -> List[int]:
	"""
	Traverse a binary tree by levels and return a list of node values.

	This function performs a level-order traversal (breadth-first traversal) of a binary tree.
	It returns a list of node values in the order they are visited.

	Parameters:
	node (Optional[Node]): The root node of the binary tree.

	Returns:
	list: A list of integers representing the node values in level-order.
	"""
	
	def branch(current_node: dict):
		"""
		Extract the values of the current node's attributes.

		This helper function takes a dictionary representation of a node and returns a list
		of its attribute values (left child, right child, and node value).

		Parameters:
		current_node (dict): A dictionary representation of a node.

		Returns:
		list: A list of the node's attribute values.
		"""
		return [i[1] for i in list(list(current_node.items()))]
	
	if node is None:
		return []
	
	the_tree = list()
	the_tree.append(branch(vars(node)))
	
	for i in the_tree:
		for j in i:
			if isinstance(j, int):
				continue
			if not j:
				continue
			else:
				the_tree.append(branch(vars(j)))
	
	flattened_tree = [item for sublist in the_tree for item in sublist]
	
	return [i for i in flattened_tree if isinstance(i, int)]


a = tree_by_levels(None)  # , [])
# , [1, 2, 3, 4, 5, 6])
b = tree_by_levels(
	Node(
		L=Node(
			L=None,
			R=Node(
				L=None, R=None, n=4  # level three
				),
			n=2  # level two
			),
		R=Node(
			L=Node(
				L=None, R=None, n=5  # level three
				),
			R=Node(
				L=None, R=None, n=6
				), n=3  # level two
			), n=1  # level one
		)
	)