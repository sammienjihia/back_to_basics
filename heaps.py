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

	# remember to pop an item, you have to swap at the top of the heap with the last item in the heap
	# then after poping the item, bubble down the swaped item to it's required place

	def pop(self):
		# if the heap has more than 2 items then swap the first item with the last item

		if len(self.heap) > 2:
			self.__swap(1, len(self.heap)-1)
			max =  self.heap.pop()
			self.__bubbleDown(1)

		# else if there are only two elements in the heap, This includes the element in the 0th index,
		# then pop the last item in that list

		elif len(self.heap) == 2:
			max = self.heap.pop()

		else:
			# there's no item in the heap, only the 0 in the 0th index that we initialised the heap with
			max = False

		return max

	# so let's define those private functions

	def __swap(self, i, j):
		# variable i references the index of the first item in the heap
		# variable j references the index of the last item in the heap

		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):

		parent = index//2

		# if the parent(which is an index) is zero, it means the heap is empty
		# if the parent is one then 
		if parent <=1:
			return

		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index

		"""
		check if the number of elements in the heap is greater 
		index: 0 1 2 3 4  5 6 
		value: 0 1 3 7 12 3 5
		"""
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

my_heap = MaxHeap([1,3,7,12,3,5])

print("aaaa"+str(my_heap.pop()))




########### Creating a MaxHeap again###############

class MaxHeap():
	# constructor that accepts a list of items
	def __init__(self, items=[]):
		# initialise the heap with a 0 element in the 0th index in the array
		self.heap = [0]

		# if class initialised with an array of items, then add the items in the heap strategically
		for item in items:
			self.heap.append(item)
			# floatUP the last element in the heap: NB use the index of the last item in the heap
			self.__floatUp(len(self.heap)-1)

	# insert element in the heap
	def insertElems(self)

	# pop max element in the heap

