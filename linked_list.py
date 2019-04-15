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

Resources used: https://bradfieldcs.com/algos/lists/implementing-an-ordered-list/
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


	# The problem to this solution is that, swapping consequtive nodes will run forever

	def NodeSwap(self, node1, node2):

		# initialize the target nodes

		target1 = None
		target2 = None

		# if the inputs are simillar, then exit, cannot swap simillar objects

		if node1 == node2:
			msg = "Inputs are simillar, cannot swap"
			return msg

		
		current_node = self.head

		# check if linked list is empty
		if current_node is None:
			msg = "Linked list is empty"
			return msg

		# Check if there's only one node in the linked list
		if current_node.next_node is None:
			msg = "Linked list has only one node"
			return msg

		# check if the head node's data is either node1 or node2
		if current_node.data == node1:
			prev1 = None
			target1 = current_node
			

		if current_node.data == node2:
			prev2 = None
			target2 = current_node
			


		while current_node.next_node is not None:
			print("$$$$$$$$$$$$$$$$$$$")

			if current_node.next_node.data == node1:
				prev1 = current_node
				target1 = current_node.next_node
				
			if current_node.next_node.data == node2:
				prev2 = current_node
				target2 = current_node.next_node
				

			current_node = current_node.next_node

		# check if the inputs are present in the linked list
		if target1 and target2:
			# print(prev1, target1.data, next1.data, prev2.data, target2.data, next2.data)
			# prev1 to point to target2

			if prev1 == None:
				self.head = target2
			else:
				prev1.next_node = target2
			# target2 to point to next1
			# target2.next_node = next1
			# prev2 to point to target1
			if prev2 ==None:
				self.head = target1
			else:
				prev2.next_node = target1
			# target1 to point to next2
			# target1.next_node = next2
			
			target1.next_node, target2.next_node = target2.next_node, target1.next_node
			
		else:
			msg = "One or both inputs are not present in the linked list"
			return msg

	# iterative method
	def reverseLinkedList(self):

		# check if linke dlist is empty
		current_node = self.head
		if current_node is None:
			msg = "Linked list is empty"
			return msg

		#check if linked list has only one node
		if current_node.next_node is None:
			msg="Cannot reverse a linked list with a single node"
			return msg

		prev = None


		while current_node.next_node is not None:
			nxt = current_node.next_node
			current_node.next_node = prev
			prev = current_node
			current_node = nxt
			
		current_node.next_node = prev
		self.head = current_node

	def reversedLinked2(self):

		#check if linked list is empty
		current_node = self.head

		if current_node is None:
			msg="Linked list is empty"
			return msg

		# check if linked list has more than one node
		if current_node.next_node is None:
			msg="Linked list has only one node"
			return msg

		prev = None

		while current_node.next_node is not None:
			nxt = current_node.next_node
			current_node.next_node = prev
			
			#increament previous pointer
			prev = current_node
			#increament linked list pointer
			current_node = nxt

		self.head = current_node
		current_node.next_node = prev

	# REVERSED SINGLY LINKED LIST AS A RECURSIVE FUNCTION
	def reverseLinkedListRecursive(self):

		#check if linked list is empty
		if self.head is None:
			msg = "Canot reverse an empty linked list"
			return msg

		current_node = self.head
		if current_node.next_node is None:
		 	msg = "This linked list has only one node. Cannot reverse"
		 	return msg

	 	prev = None

	 	# call recursive function here

	 	current_node, prev = self._recursiveFunction(current_node, prev)
	 	self.head = current_node
	 	current_node.next_node = prev
	 	
	 	



 	def _recursiveFunction(self, current_node, prev):

 		if current_node.next_node is None:
 			return (current_node, prev)
 		else:
 			# capture next node on a temp variable
 			nxt = current_node.next_node

 			# convert the next pointer to point to the previous node
 			current_node.next_node = prev

 			# move prev pointer and current node pointer to their next respective positions
 			prev = current_node
 			current_node = nxt
 			return self._recursiveFunction(current_node, prev)





 		




			


	

			






llist = LinkedList()
llist.append_data(1)
llist.append_data(2)
llist.append_data(3)
llist.append_data(4)
llist.append_data(5)
llist.append_data(6)
# print(llist.print_nodeData())
# print(llist.NodeSwap(6,7))
# print(llist.insert_data(7, 4))
# llist.reverseLinkedList()
# llist.reversedLinked2()
llist.reverseLinkedListRecursive()
print(llist.print_nodeData())






# Insert code to merge the linked lists

















		
