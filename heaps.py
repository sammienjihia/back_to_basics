"""
Resources used : https://www.techiedelight.com/heap-interview-questions/
"""

class MaxHeap():
	# initialize the class with a list of items

	def __init__(self, items=[]):
		self.heap = [0]


		# if you have initialised the class with a list of items, whenever you append a new item, then sort 
		# it to it's required place
		# private function float up takes the index of the last item in the list
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap)-1)

	# the push function also uses the private function floatUp() to sort the insert item to its required place

	def push(self, item):
		self.heap.append(item)
		self.__floatUp(len(self.heap)-1)


	def peek(self):
		# Check if atleast there's an item in the heap, else return None
		if self.heap[1]:
			return self.heap[1]
		else:
			return None

