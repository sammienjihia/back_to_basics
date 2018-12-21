"""
Given list [3,2,8,4,1]

Outer iteration 1 (for i in range(0, len(arr)-1)): i is 0
	inner iteration (for j in range(0, len(arr)-1-i)) for the first iteration i is 0

		[3,2,8,4,1]

	1. [2,3,8,4,1] -> 3 is greater than 2 so it's swapped
	2. [2,3,8,4,1] ....3 is less than 8 so it's not swapped
	3. [2,3,4,8,1] -> 8 is greater than 4 so swapped
	4. [2,3,4,1,8] -> 8 is greater than 1 so swapped

	so last item is already sorted

"""


def bubbleSort(arr):
	n = len(arr)

	for i in range(0, n):

		for k in range(0, n-i-1):

			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]

	return arr

print (bubbleSort([1,7,2,5,9,2,4, 10, 0]))