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

# Return the top most item in the stack
#arr[len(arr)-1]

# Return the number of items in the stack
len(arr)

"""
Implementing a stack in python: http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html
"""

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

print(some_stack.pop_item())

print(some_stack.len_stack())

"""
Balanced parentheses question:
Resources used:

https://www.youtube.com/watch?v=TC7apM-xGaU

https://www.careercup.com/page?pid=stacks-interview-questions

https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python

http://interactivepython.org/courselib/static/pythonds/BasicDS/SimpleBalancedParentheses.html

https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV


Data strucutures commonly asked questions: https://www.geeksforgeeks.org/commonly-asked-data-structure-interview-questions-set-1/
"""


class Paran_checker():

	def is_matched(self, item1, item2):
		if item1 == '{' and item2 == '}':
			return True

		elif item1 == '(' and item2 == ')':
			return True

		elif item1 == '[' and item2 == ']':
			return True
		else:
			return False


	def balanced_checker(self, my_list):

		is_balanced = True
		index = 0
		s = Stack()

		while index < len(my_list) and is_balanced:

			p_char = my_list[index]

			if p_char in "{[(":
				s.push(p_char)

			else:
				if s.is_empty():
					is_balanced = False

				else:
					top = s.pop_item()

					if not self.is_matched(top, p_char):
						is_balanced = False

			index += 1

		if is_balanced and s.is_empty():
			return True

		else:
			return False

checker = Paran_checker()
print(checker.balanced_checker(')'))


"""
Convert integer to binary
"""

def int_to_bin_converter(integer_item):
	s = Stack()

	# divide interger by 2 and push the remainder to  stack

	while integer_item > 0:
		remainder = integer_item % 2
		s.push(remainder)

		integer_item = integer_item // 2


	bin_num = ""

	while not s.is_empty():
		bin_item = s.pop_item()

		bin_num += str(bin_item)

	return bin_num


print(int_to_bin_converter(242))



