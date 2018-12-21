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
is not duplicated
"""
def hash_map(arr):

	counter_list = []
	hash_dict = {} 

	for n in range(0, len(arr)):
		if arr[n] in hash_dict:
			hash_dict[arr[n]] = hash_dict[arr[n]] + 1

		else:
			hash_dict[arr[n]] = 1


	print(hash_dict)
	print(arr[6])
		 
	 	


 	

hash_map([1,2,2,3,3,3,4])














































































