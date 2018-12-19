"""
A divide and conquer algorithm. A recursive algorithm that continually splits a list in half. If the list is empty or
has only one element, then we consider that list already sorted(This is the base case). If the list has more than one item, 
we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, merge(combining the sorted 
smaller list into one) is performed

"""

def mergeSort(arr):

	# start with the base case. Check if arr has more than one item
	if len(arr)> 1:

		# Split the array into halaves

		mid = len(arr)//2

		lefthalf = arr[:mid]
		righthalf = arr[mid:]

		# perform mergesort on both halves

		mergeSort(lefthalf)
		mergeSort(righthalf)

		# Recurse through the two halves checking whether the element in the left block is less than that in the right

		# initialise some constants

		i = 0
		j = 0
		k = 0

		# recurse through both halves

		while i < len(lefthalf) and j < len(righthalf):

			# check if left element is lesser than right element and assign the lesser element to the array at that
			#points index 

			if lefthalf[i] < righthalf[j]:
				arr[k] = lefthalf[i]
				i = i+1

			else:
				arr[k] = righthalf[j]
				j = j+1

			
			

			
			
			k = k+1

		# print(arr)

		# merge the smaller sorted halves into one array
		while i < len(lefthalf):
			arr[k] = lefthalf[i]

			
			i = i+1
			k = k+1

		# print(arr)


		while j < len(righthalf):
			arr[k] = righthalf[j]

			
			j = j+1
			k = k+1

		# print(arr)

	print (arr)


mergeSort([2,4,7,9,4,6,9,2,4])


