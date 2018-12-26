"""
Resources used:

https://medium.freecodecamp.org/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d

https://www.youtube.com/watch?v=6sBsF13n5ig


https://github.com/AtotheY/YoutubeTutorials/blob/master/Introductions/linkedListOnlyNodes.py


"""


"""
In the below code, we've simply created a class that has a value and a nexNode attribute
"""
class LinkedList:
	"""docstring for ClassName"""
	def __init__(self, value, nextNode=None):

		self.value = value
		self.nextNode = nextNode


# To create a node, we simply pass in a value
node1 = LinkedList(3)
node2 = LinkedList(4)
node3 = LinkedList(5)

# Then we connect the nodes together
node1.nextNode = node2
node2.nextNode = node3

print(node3.nextNode)
		