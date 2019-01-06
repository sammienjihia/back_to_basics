"""
This is a really simple implementation of a stack
NB: A stack has a LIFO implementation, this means the last item into the stack is the first item to be removed 
from the stack

"""

arr = []

# Add item to a stack
arr.append('x')

# Remove item from stack
arr.pop()

class Stack():
	def __init__(self):
		self.items = []

	# Check if the stack is empty, return true if stack doesn't have any elements, and false if it has elements
	def is_empty(self):
		if self.items == []:
			return True

		else:
			return False


	# Add an item to the stack
	def push(self, item):
		self.items.append(item)

	# Remove and return the top most item in the stack
	def pop_item(self):
		return self.items.pop()

	# Return a reference of the top most item in the stack without removing it
	def peek(self):
		return self.items[len(self.items)-1]

	# Return the number of elements in the stack
	def len_stack(self):
		return len(self.items)
			

some_stack = Stack()

print(some_stack.is_empty())

some_stack.push('24')

print(some_stack.peek())

print(some_stack.len_stack())
