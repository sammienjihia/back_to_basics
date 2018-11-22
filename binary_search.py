# NB A binary search requires a sorted array
# Done by repeatedly dividing the search interval by half. Begin by an interval covering the whole array
#if the value of the search key is equal to the element in the middle of the intervalthen that's the answere
# If the search key is less than the item in the middle of the interval narrow your search to the lower half
# otherwise narrow it to the upper half. Repeat check until the value is found or the interval is empty

def binary_search(arrayItem, searchKey, startIndex, endIndex):

	# Sort array item
	arrayItem.sort()

	# the endIndex of an array must always be greater than the startIndex otherwise something wrong
	if endIndex >= startIndex :
		# get mid
		midIndex = int((startIndex + endIndex)/2)

		# check if searchKey is equal to the element in the middle index
		if searchKey == arrayItem[midIndex]: 
			return_data = "The search key is {} Found at index {} ".format(arrayItem[midIndex], midIndex)
			return return_data 

		elif searchKey > arrayItem[midIndex]:
			# select the upper bound for search
			# make the middle index +1 become the new start index thus selecting the upper bound and repeat the function
			return binary_search(arrayItem, searchKey, midIndex+1, endIndex)
		else:
			# select the lower bound for search
			# make the middle index -1 become the new end index thus selecting the lower bound and repeat the function
			return binary_search(arrayItem, searchKey, startIndex, midIndex-1)



	else:
		# element not in this array
		return -1


	
arr = [1,5,9,2,6,4,9,6,2,5]

print (binary_search(arr, 4, 0, len(arr)-1))

