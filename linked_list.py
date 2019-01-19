"""
Resources used:

https://medium.freecodecamp.org/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d

https://www.youtube.com/watch?v=6sBsF13n5ig


https://github.com/AtotheY/YoutubeTutorials/blob/master/Introductions/linkedListOnlyNodes.py

doubly linked lists: https://www.youtube.com/watch?v=sDP_pReYNEc

stack abuse linked list: https://stackabuse.com/python-linked-lists/

lucidprogramming doubly linked list: https://www.youtube.com/watch?v=8kptHdreaTA

single linked list: https://dbader.org/blog/python-linked-list


"""


"""
In the below code, we've simply created a class that has a value and a nexNode attribute
"""
class LinkedListNode:
	"""docstring for ClassName"""
	def __init__(self, value, nextNode=None):

		self.value = value
		self.nextNode = nextNode


# To create a node, we simply pass in a value
node1 = LinkedListNode(3)
node2 = LinkedListNode(4)
node3 = LinkedListNode(5)
node4 = LinkedListNode(6)

# Then we connect the nodes together
node1.nextNode = node2
node2.nextNode = node3

print(node1.nextNode.value)

currentNode = node1
while True:
	print(currentNode.value)
	print("-->")

	if currentNode.nextNode == None:
		print("None")
		break

	currentNode = currentNode.nextNode
""" 
Kindly rivist:
Resources used : https://www.youtube.com/watch?v=6sBsF13n5ig
"""

class LinkedList():

	def __init__(self, head=None):
		self.head = head

	def insert(self, value):
		node = LinkedListNode(value)

		if self.head is None:
			self.head = node
			return

		currentNode = self.head

		while True:
			if currentNode.nextNode is None:
				currentNode.nextNode = node
				break
			currentNode = currentNode.nextNode

		


# ******************* LINKED LIST ***********************
"""
Resources used: https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5
"""

class Node():
	# creating a node   new_node = Node(data)

	def __init__(self, data):
		self.data = data
		self.next_node = None


class LinkedList():

	def __init__(self):
		self.head = None

	def print_nodeData(self):

		current_node = self.head

		while current_node != None :
			print(current_node.data)
			current_node = current_node.next_node

		# The head is a pointer to a node in the linke list 



	# adding a node to a the end of the LinkedList// basically appending a new node


	def append_data(self, data):
		new_node = Node(data)

		# first check if the LinkedList is empty, check if the head pointer is pointing to None
		if self.head is None:
			self.head = new_node
			return

		# so move the head pointer to the end of the list until the end of the 
		last_node = self.head

		while last_node.next_node != None:
			last_node = last_node.next_node

		last_node.next_node = new_node

	def prepend_data(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		new_node.next_node = self.head
		self.head = new_node  

	def insert_data(self, data, targetNode):
		new_node = Node(data)

		current_node = self.head

		while current_node.data != targetNode and current_node.next_node != None:
			current_node = current_node.next_node
			# by end of this loop, the current node shall be the target node
		print("current node is {}".format(current_node.data))

		if current_node.data == targetNode:

			targetNode2 = current_node.next_node

			current_node.next_node = new_node

			new_node.next_node = targetNode2

		else:
			print("Taget node {} not in the linked list".format(targetNode))


			






llist = LinkedList()
# llist.append_data(1)
llist.append_data(2)
llist.append_data(3)
llist.append_data(4)
llist.append_data(5)
llist.append_data(6)
llist.insert_data(7, 20)
llist.print_nodeData()
























		