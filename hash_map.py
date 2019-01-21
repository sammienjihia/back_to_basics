"""
A hash map is a data structure that stores a key, value pair.

In python, a dictionary is a hash map. Can be defined by the dict() function

***** Components of the manual hash map ******

1. Array: Shall hold our data structure
2. Hash function: to convert our key to an index for storage in our array 
2. Collision: This is when we have duplicate indeces from our hash function
"""

class HashMap():

	# initialise the class with a pre-defined array, with a predefined length

	def __init__(self, size):
		self.size = size
		self.map = [None] * self.size

	# convert our key to an integer that will map to the index in our array
	def __HashFun(self, key):
		hash_data = 0

		for char in key:
			hash_data += ord(char)

		return hash_data % self.size

	def addItem(self, key, value):

		index = self.__HashFun(key)
		# the key_value variable is what we want to insert into that cell
		key_value = [key, value]

		if self.map[index] is not None:
			# two scenarion here, either we want to modify our data, or we want to add new data

			# modify our data
			for pair in self.map[index]:
				if pair[0] == key:
					pair[1] = value
					return True

			# add the new item
			self.map[index].append(key_value)

		else:
			# Add our key value to the given index in our array. Remember the element in that index should be a list of lists
			self.map[index] = [key_value]




	def getItem(self, key):

		# convert the key to an index
		index = self.__HashFun(key)


		# get the array element from that index. Should be a list of lists if not none
		data = self.map[index]

		if data is not None:

			# if not None then iterate through the list of lists looking for the given key
			for pair in data :
				if pair[0] == key:

					return pair[1]
				else:
					return("Key not found")

		return None

	def deleteItem(self, key):
		index = self.__HashFun(key)

		if self.map[index] is not None:

			for pair in self.map[index]:
				if pair[0] == key:
					self.map[index].remove([pair[0], pair[1]])
					return True

			return("Item not in List")

		else:
			return None


	def printMap(self):
		return self.map

hash_map = HashMap(10)

hash_map.addItem('Mango', 3.5)

hash_map.addItem('beans', 4.8)

hash_map.addItem('bread', 10)

print(hash_map.printMap())

print(hash_map.getItem('bread'))



