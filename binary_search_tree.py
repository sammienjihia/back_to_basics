

class Node:
	def __init__(self, data):

		self.data = data
		self.lef_child = None
		self.right_child= None


class BsTree:
	def __init__(self, ):
		self.root = None


	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self.__insert(data, self.root)

	def __insert(self, data, current_node):
		if data < current_node.data:
			if current_node.left is None:
				current_node.left = Node(data)
			else:
				self.__insert(data, current_node.left)

		elif data> current_node.data:
			if current_node.right is None:
				current_node.right = Node(data)

			else:
				self.__insert(data, current_node.right)

		else:
			pass

	def search(self, data):
		pass

	def find(self, data):
		pass

	