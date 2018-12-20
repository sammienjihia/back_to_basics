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

