import math

def jumpSearch(arr, searchKey):

	jumpSize = int(math.sqrt(len(arr)))


	# search for the the block where the search key can be found in by increamenting the jumpSize untill the point where
	# arr[jumpSize] is greater than the search key. This is where your search key is 
	while arr[jumpSize]<= searchKey:
		if arr[jumpSize]== searchKey:
			return jumpSize
		jumpSize  += jumpSize
		jump_count = jumpSize
		# if jump count is greater than or equal to the length of the array, then item is not in that array 
		if jump_count >= len(arr):
			return -1

	# Once you get the search block, where arr[jumpSize] is greater than your searchKey, then perform
	# a backward linear search		
	while arr[jumpSize] > searchKey:
		#perform a linear search backwards
		steps_to_go = int(math.sqrt(len(arr)))
		for i in range(steps_to_go):
			jumpSize -= 1
			if arr[jumpSize] == searchKey:
				return jumpSize
		# if after performing the linear search in that block you still can't find it then this means item not present
		return -1
			
		

print(jumpSearch([1,3,6,8,10,13,17], 1))
"""
Resources used 
1. https://www.geeksforgeeks.org/jump-search/
2. https://www.tutorialspoint.com/Jump-Search
"""

