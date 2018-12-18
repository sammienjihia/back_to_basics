


def bubbleSort(arr):
	n = len(arr)

	for i in range(0, n-1):

		for k in range(0, n-i-1):

			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]

	return arr

print (bubbleSort([1,7,2,5,9,2,4]))