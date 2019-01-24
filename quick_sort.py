def partition(lst, start, end):
    pos = start                           # condition was obsolete, loop won't
                                          # simply run for empty range

    for i in range(start, end):           # i must be between start and end-1
        if lst[i] < lst[end]:             # in your version it always goes from 0
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] # you forgot to put the pivot
                                          # back in its place
    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:                       # this is enough to end recursion
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)
                                          # you don't need to return the list
                                          # it's modified in place


# in a given array, get the pivot
# swap the pivot with the last element of the array
# get start index and the current index(index at position start_index + 1)


def quick_sort(arr):

  # get the mid point of the array
  mid  = int(len(arr)//2)

  if arr[0] < arr[mid]:
    if arr[mid] < arr[len(arr)-1]:
      mid_element = arr[mid]

  mid_element, arr[len(arr)-1] = arr[len(arr)-1], mid_element

  base_index = 0
  current_index = 1

  for n in range(len(arr)):

    if arr[n] < mid_element:
      arr[base_index], arr[current_index] = arr[current_index], arr[base_index]

      base_index = base_index + 1
      current_index = current_index + 1

    elif arr[n] > mid_element:
       current_index = current_index + 1

    arr[base_index], mid_element = mid_element, arr[base_index]

  print (arr[base_index])
  print (mid_element)
  print(arr)


quick_sort([1,4,2,6,4,9,5,8])



####################

def partition(arr, k):

  left, right = 0, len(arr)-1

  traverse = 0

  while traverse < right:

    while arr[traverse] < k:

      arr[left], arr[traverse] = arr[traverse], arr[left]

      left += 1

    while arr[traverse] > k :
      arr[right], arr[traverse] = arr[traverse], arr[right]

      right -= 1
      
    traverse += 1

    return arr


print(partition([1,2,8,4,7,6, 2,4,8,5,9,2], 6))



# question 1, shall the array have repeating integers
def partition_correct(arr, k):

  left = 0
  right = len(arr)-1

  while left != right :

    # left elements should be less than k
    if arr[left] < k:
      left += 1

    # right elements should be greater than or equal to k

    if arr[right] >= k:
      right -= 1

    if left>=right :
      return arr

    arr[left], arr[right] = arr[right], arr[left]

  # while left != right:
  #   if arr[left] == k:
  #     left_outer = left - 1
  #     left_inner = left + 1

  #     if 

  

  return arr

print(partition_correct([1,2,6, 8,6,4,7,6, 2,4,8,5,9,6,2], 6))







