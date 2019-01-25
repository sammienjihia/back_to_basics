"""
implementing a graph using adjacency list: This a list on neighbbours to a Node
"""

class Node:
	def __init__(self, value):
		# value of the node
		self.value = value

		# the neighbours to the node
		self.neighbours = []

	# adding a neighbour to a list of neighbours to a node

	def add_neighbours(self, nnode):
		# To be included in the neighbors list, don't include the node itslsef, don't repeat a node
		if nnode not in self.neighbours and nnode.value is not self.value:
			self.neighbours.append(nnode)

			return True

		# neighbour already in the list
		return False


class Graph:

	def __init__(self):
		# Key value pairs where the Key is the inserted Node, and the Value is the list of the Node's neighbours
		self.nodes = {}
		self.edges = {}

	# The nodes will be a dictionary where the key is the value of a node and the value will
	# be the list of it's neighbours


	def add_node(self, node):
		# Check if the given node is already represented in the graph dictionary

		if node not in self.nodes :
			self.nodes[node] = node.neighbours

			return True
		else:
			return False



		# if isinstance(node, Node) and node.value not in self.nodes:
		# 	# add the node into the nodes dict with the node value as the key
		# 	self.nodes[node.value] = node

		# 	return True

		# else:
		# 	return False

	def add_edge(self, node1, node2, name):

		if node1 != node2:
			if node1 in self.nodes and node2 in self.nodes:

				node1.add_neighbours(node2)

				node2.add_neighbours(node1)

				self.edges[name] = (node1, node2)
			else:
				return False

			return True
		else:
			return False

	def get_edges(self):
		for key, value in self.edges.items():
			print("Edge {}: {}, {}".format(key, value[0].value, value[1].value))


		

	def print_graph(self):

		for key, value in self.nodes.items():
			print(key.value, [x.value for x in value] )
		
		





	



g = Graph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

print("************* adding a node *******************")
print(g.add_node(node1))
print(g.add_node(node2))
print(g.add_node(node3))
print(g.add_node(node4))
print(g.add_node(node5))
print("***************** adding a node")
print(" ")
print("############# adding an edge ##########")
print(g.add_edge(node1, node2, "A"))
print(g.add_edge(node1, node3, "B"))
print(g.add_edge(node3, node2, "C"))
print(g.add_edge(node2, node4, "D"))
print(g.add_edge(node4, node3, "E"))
print(g.add_edge(node5, node3, "F"))
print("########### adding an edge ###########3")

(g.print_graph())

(g.get_edges())



"""
Graph data structure from: Data Structures and Algorithms in Python [Goodrich, Tamassia & Goldwasser 2013-03-18] 
"""

class Vertex:
	def __init__(self, x):
		self._name = x

	def name(self):
		# Return the name associated with this vertex.(The name of this vertex)
		return self._name

class Edge:
	def __init__(self, origin, destination):
		self.origin = origin
		self.destination = destination

	def edges(self):
		# return a tuple of vertices representing an edge
		return(self.origin, self.destination)

	def opposite(self, v):
		# Return the vertex that is opposite v on tthis edge
		return self.destination if v is self.origin else self.origin

class Graph:

	def __init__(self, directed=False):

		self.origin = {}

	def vertex_count(self):
		return len(self.origin)




