"""
implementing a graph using adjacency list: This a list on neighbbours to a Node
"""

class Node:
	def __init__(self, value):
		# value of the node
		self.value = value

		# the neighbours to the node
		self.neighbours = list()

	# adding a neighbour to a list of neighbours to a node

	def add_neighbours(self, nnode):

		if nnode not in self.neighbours:
			self.neighbours.append(nnode)

			# sort the list of neigbours
			self.neighbours.sort()

			return True

		# neighbour already in the list
		return False


class Graph:

	# The nodes will be a dictionary where the key is the value of a node and the value will
	# be the list of it's neighbours

	nodes = {}

	def add_node(self, node):
		# Check if the given node is an insatnce of the Node 

		if isinstance(node, Node) and node.value not in self.nodes:
			# add the node into the nodes dict with the node value as the key
			self.nodes[node.value] = node

			return True

		else:
			return False


	# an edge is a connection between two nodes
	def add_edge(self, node1, node2):
		# first check if both nodes are in the nodes dictionary

		if node1 in self.nodes and node2 in self.nodes:
			for key, value in self.nodes.items():
				if key == node1.value:
					value.add_neighbours(node1)

				if key == node2.value:
					value.add_neighbours(node2)

			return True

		else:
			return False


	def print_graph(self):
		for key in sorted(list(self.nodes.keys())):
			print(str(key) + str(self.nodes[key].neighbours))



g = Graph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(2)

node1.add_neighbours(node2)

node1.add_neighbours(node3)

node2.add_neighbours(node1)

node2.add_neighbours(node1)

node3.add_neighbours(node2)

node3.add_neighbours(node1)

print(g.add_node(node1))
print(g.add_node(node2))
print(g.add_node(node3))

print(g.add_edge(node1, node2))
print(g.add_edge(node1, node3))
print(g.add_edge(node3, node2))

print(g.print_graph())



