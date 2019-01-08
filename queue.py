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
1. Implementing a queue using two stacks
Resources: https://www.interviewcake.com/concept/java/queue


2. Implementing a queue using a linked list


QUESTIONS on queues
1. https://www.geeksforgeeks.org/category/data-structures/queue/
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

# Implementing the above using oop paradigm

class FindNth():

	def __init__(self):

	 	self.queue_item = 1

	 

 	def findnthodd(self, input):
 		my_queue = Queue()

 		while my_queue.size() < input :
 			odd_flag = self.queue_item % 2

 			if odd_flag == 1:
 				my_queue.enqueue(self.queue_item)

			else: 
				pass

			self.queue_item += 1

		for x in range(1, input+1):
			nth_item = my_queue.dequeue()

			if x == input:
				return nth_item

		
		


print(findNthOdd(10))

the_nthOdd = FindNth()

print(the_nthOdd.findnthodd(10))

