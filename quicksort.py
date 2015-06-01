def qsort(array):
  
  pivot = len(array)-1		# Choose the last element of the array
  left = 0
  right = len(array)-1		# Choose element to the right
  
  if len(array) > 1:
    while left <= right:
    	while array[left] < array[pivot]:
        left += 1
      while array[right] > array[pivot]:
        right -= 1
      # swap left and right marks here as they
      # are out of place relative to the pivot
      array[left], array[right] = array[right], array[left]
      left += 1
      right -= 1 
      
      # now flip the pivot to its respective
      # position needs to be swapped to the split point here
    array[pivot], array[left] = array[left], array[pivot]
      
    qsort(array[0:left])	# left should be to the right of the rightmark
    qsort(array[left::])	# right side of the previously partitioned array
    
  else:
    return array 				# returning the length 1 array to stop recursion
      
if __name__ == '__main__':
  x = [3,10,2,8,23,12,5]
  print(qsort(x))