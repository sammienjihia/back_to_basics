"""
Given a integer array and a number k, output pairs that sum up to k
"""

def find_pairs_that_add_up_to(arr, k):

	num_sets = set(arr)

	nums = list(num_sets)

	num_list = []

	for num in nums:

		complement = k-num
		
		if complement in nums:
			num_list.append((complement, num))
			nums.remove(num)

	print(num_list)
			

def find_pairs_that_add_up_to2(arr, k):
	num_sets = set(arr)

	nums = list(num_sets)

	tuples_list = []

	for i in range(0, len(nums)-1):
		for n in range(0, len(nums)-1):
			if nums[i] == nums[n]:
				pass

			elif (nums[i] + nums[n]) ==  k:
				
				tuples_list.append((nums[i], nums[n]))




		



	print(tuples_list)


find_pairs_that_add_up_to([1,3,5,3, 2,7,2,6,8,4], 8)

find_pairs_that_add_up_to2([1,3,5,3, 2,7,2,6,8,4], 8)