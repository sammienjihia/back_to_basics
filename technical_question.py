"""
Given a integer array and a number k, output pairs that sum up to k
"""

def find_pairs_that_add_up_to(arr, k):
 	
 	# remove duplicates
	num_sets = set(arr)

	# convert the set into an iterable
	nums = list(num_sets)

	# A list to hold our tuples
	num_list = []

	for num in nums:

		# get the compliment
		complement = k-num
		
		# if complement is in the set list, then add the complement 
		# and num in the num_list and remove the num from the set list
		if complement in nums:
			num_list.append((complement, num))
			nums.remove(num)

	print(num_list)
			



find_pairs_that_add_up_to([1,3,5,3, 2,7,2,6,8,4], 8)


# Google way of doing this question: This will not handle duplicate entries in the array
def find_pair_that_add_up_to2(arr, w):
	# sort the array
	n=0

	list_to_hold_tuples = []

	for n in range(0, len(arr)-1):
		for k in range(0, len(arr)-n-1):
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k] 

	arr = list(set(arr))
	
	start_point = 0
	end_point = len(arr)-1

	while start_point < end_point:
		

		if (arr[start_point] + arr[end_point]) == w:
			list_to_hold_tuples.append((arr[start_point],arr[end_point]))
			end_point = end_point-1
			

		elif (arr[start_point] + arr[end_point])< w:
			start_point = start_point +1
			


		elif (arr[start_point] + arr[end_point])> w:
			end_point = end_point -1
			

	print(list_to_hold_tuples)
	print(arr)
			

print("***************")
find_pair_that_add_up_to2([1,3,5,3, 2,7,2,6,8,4], 8) 



"""
Given an array of unsorted int, find the nth smallest number
"""

def nth_smallest(arr, nth_number):

	

	for i in range(len(arr)):
		for k in range(len(arr)-i-1):
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1] , arr[k]

			

	print(arr[nth_number-1])


nth_smallest([3,3,6,8,4,1], 3)


"""
Given an array of integers, find pairs that are a multiple of k
"""

def find_multiples(arr, k):

	for n in range(0, len(arr)-1):
		pass



"""
given an array of integers that are duplicated evenly except one which is not duplicated, find the number which
is ordley duplicated
"""
def hash_map(arr):

	hash_dict = {} 
	ans_list = []
	# in this dictionary, the key will be the array value at a particular point, and the value will be the 
	# number of times the array value appears in the array

	for n in range(0, len(arr)):
		if arr[n] in hash_dict:
			hash_dict[arr[n]] = hash_dict[arr[n]] + 1

		else:
			hash_dict[arr[n]] = 1

	for key in hash_dict.keys():
		if hash_dict[key]%2 == 1:
			ans_list.append(key)



	print(hash_dict)
	print(arr[6])
	print(ans_list) 	

hash_map([1,2,2,3,3,3,4])

"""
Given a list of vertices and a vertex w, find the k nearest vertices to vertex w


NOT COMPLETED
"""
import math

def nearest_vertex(arr, k, given_vertex):
	
	# This list shall hold the eucledean distances
	counter_list = []

	# This dictionary will hold the eauclidean distance as the key and the value will be the vertex
	hash_map = {}

	# Iterate through the 
	for n in range(len(arr)):
		# find the eauclidean distance

		vertex = arr[n]

		x_index = vertex[0]
		y_index = vertex[1]

		x_index_gv = given_vertex[0]
		y_index_gv = given_vertex[1]

		# Eauclidean distance sqrt((x1-x2)**2+(y1-y2)**2)

		e_distance = math.sqrt((x_index - x_index_gv)**2 + (y_index - y_index_gv)**2)

		if e_distance in hash_map:
			pass

		hash_map[e_distance] = vertex

		counter_list.append(e_distance)



	print(counter_list)
	print(hash_map)

nearest_vertex([(6,15),(2,3),(5,12),(3,6),(4,9)], 3, (3,6))


"""
Given a string, delete any reocurring character and return the new character
"""

def deleteCharacter(string):
	character_store = set()
	outputString = ''

	for char in string:
		if char not in character_store:
			character_store.add(char)
			outputString += char

	return outputString

print(deleteCharacter('saaaammmy mwangi'))














"""
List comprehension
Given an array of integers, print the square of all the elements
"""

def square_elem(arr):

	square = [num*num for num in arr]

	return square


print(square_elem([1,2,3,4,5]))


"""
Generators, 

yeild is the key word

iteritems() vs items() in a dictionary

xrange() vs range()
"""
















































































