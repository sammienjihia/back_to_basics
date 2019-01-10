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

		
		