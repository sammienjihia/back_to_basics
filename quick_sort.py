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


