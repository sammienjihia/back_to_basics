"""

http://interactivepython.org/runestone/static/pythonds/BasicDS/TheQueueAbstractDataType.html

Implementing a queue in python: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html

enqueue
dequeue
is_empty

"""

class Queue():

	def __init__(self):
		self.items = []

	def is_empty(self):

		if self.items == []:
			return True
		else:
			return False

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

my_queue = Queue()
for x in range(0, 10):
	my_queue.enqueue(x)

print(my_queue.size())

"""
1. Implementing a queue using stacks
2. Implementing a queue using a linked list
"""



"""
Given an input n, find the nth odd number
"""
# queue first in first out. 

def findNthOdd(input):
	my_queue = Queue()
	queue_item = 1

	while my_queue.size() < input:
		counter = queue_item % 2

		if counter == 1:
			my_queue.enqueue(queue_item)

		else:
			pass

		queue_item += 1

	for x in range(1, input+1):

		nth = my_queue.dequeue()

		if x == input:
			return nth

		
		


print(findNthOdd(10))

