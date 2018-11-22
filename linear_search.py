# In this search a sequential search is made over all the items one by one untill a match is found

def linearSearch(arrayItem, searchKey):

	for i in range(len(arrayItem)):
		print(arrayItem[i])
		if searchKey == arrayItem[i]:

			return searchKey

		

print(linearSearch([1,2,5,7,3], 7))

# given an array of n elements, the big O notation of a linear search algorithm is 
# O(n)