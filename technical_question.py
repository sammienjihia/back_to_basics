"""
More resources can be found at : https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0


HackerRank videos, cracking the coding interview; https://www.youtube.com/watch?v=7ArHz8jPglw&index=2&list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX

Top job interview questions: https://www.monster.com/career-advice/article/100-potential-interview-questions


python data structures: https://dbader.org/blog/fundamental-data-structures-in-python



2 simple ways of coding a linked list: https://www.youtube.com/watch?v=6sBsF13n5ig

sorting, searchng and algorithm analysis in python: https://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html



Scrum vs waterfall : https://blog.flatworldsolutions.com/10-differences-agile-waterfall-methodology/
"""


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


"""
Finding missing number given list of integers from 1 to n

A) Sum formulae: 
sum of 1 to n integers = n*(n+1)/2 whic is equal to sum(range(arr[0], arr[-1]+1))
Then subtract the the elements i the array one by one 

another way of doing it: https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-8.php
"""

def getMissing(arr):
	len_of_arr_minus_one_int = len(arr)

	# Find the total of the elemnets in array without missing value based on the sum formulae
	total = (len_of_arr_minus_one_int + 1) * (len_of_arr_minus_one_int+2)/2

	for elem in arr:
		total = total - elem

	return total

# shorter example
def getMissing2(arr):
	len_of_arr = len(arr)
	total = (len_of_arr+1)*(len_of_arr+2)/2

	sum_of_arr = sum(arr)

	return total-sum_of_arr

print("####3")
print(getMissing([1,2,3,5]))
print(getMissing2([1,2,3,5]))


"""
Cracking the coding inteverview Example question Pg 79
Given an array of integers, count the number of pairs of integers that have a difference k
Ex arr = [1,7,5,9,2,12,3] and k=2   there are 4 pairs with difference 2 : (1,3) (3,5), (5,7), (7,9) 
"""

# Example
"""
for every element find the total between the elemnt and the difference, then search for the total in the array

Elem 1 
1+2 = 3 // Search for three in the array

Elem 2 
2+2 = 4 // Search for 4 in the array

Elem 3
3+2 = 5 // Search for 5 in the array


....

and so on

So run time shall be n (iterating through every elemnt in the array) by n (iterating through the array searching for thr total)

Time Complexity O(n*n) = O(n2)

#Optimize

if we sort thr array (n Log n) and use binary serach to search for the total in the array (n Log n) we can reduce the 
time complexity to 2(n Log n)

"""
class Problem1:
	def __init__(self, k, arr):
		self.arr = arr
		self.k = k

	def getTotal(self):
		dic = {}

		for n in self.arr:
			w = n+self.k

			dic[w] = (n,w)

		return dic

	def getAns(self):

		ans = []
		dic_of_totals = self.getTotal()

		for n in self.arr:
			if n in dic_of_totals:
				ans.append(dic_of_totals[n])


		return ans

print("******************************")

prob = Problem1(2, [1,7,5,9,2,12,3])
print(prob.getAns())



		















































































