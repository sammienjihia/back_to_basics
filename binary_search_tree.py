

class Node:
	def __init__(self, data):

		self.data = data
		self.left = None
		self.right= None


class BsTree:
	def __init__(self):
		self.root = None


	def insert(self, data):

		# if the there's no root node then this means the bst is empty so make this first node the root node, no
		# need for our recursive __insert() function
		if self.root is None:
			self.root = Node(data)
		else:
			# write a recursive insert function that checks the value of the current node and if the data of the 
			# node to be inserted is greater than that of the current node, then it should be the right child
			# of that current node, else if it is less then it should be the current node's left child
			# the arguments of the recursive __insert() function is data, current_node. The data shall be same 
			# as the function runs recussively during an insertion, the current_node shall change as the function
			# tries to search for the right position   
			self.__insert(data, self.root)

	def __insert(self, data, current_node):
		# Nb, the property of a bst is that the value of the left child should be less than the value of the parent node,
		# while the value of the right node should be greater than the value of the parent node

		# if data to be inserted is less than the value of the current node, move to it's left child
		if data < current_node.data:
			# if the current node does not have a left child then create a node with the given data and make it the 
			# left child of the current node
			if current_node.left is None:
				current_node.left = Node(data)
			else:
				# else if the current node has a left child then call the recursive __insert() function, with that child
				# now becoming the current node
				self.__insert(data, current_node.left)

		# if the data to insert is greater than the value of the current node, then move to it's right child
		elif data> current_node.data:
			# if there's no right child, then use that data to make a Node and make it the right child
			if current_node.right is None:
				current_node.right = Node(data)

			else:
				# else call the recursive __insert() function 
				self.__insert(data, current_node.right)

		# we do not want duplicates so if the value of the current node equals the data to insert then pass
		else:
			pass


	def find(self, data):
		if self.root is None:
			return None

		else:
			return self.__find(data, self.root)

	def __find(self, data, current_node):


		if data > current_node.data:

			if current_node.right is None:
				print("v")
				return False

			else:
				return self.__find(data, current_node.right)

		elif data < current_node.data:
			if current_node.left is None:
				return False

			else: 
				return self.__find(data, current_node.left)

		else:
			return True
			

	


bst  = BsTree()

bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(2)
bst.insert(1)
bst.insert(10)
bst.insert(9)


print(bst.find(6))
