def qsort(array):
	
	if len(array) > 1:
		pivot = len(array) - 1
		left = 0
		right = len(array)-2
		while left <= right:
			while left <= right and array[left] < array[pivot]:
				left += 1
			while left <= right and array[right] >= array[pivot]:
				right -= 1
			if left <= right:
				array[left], array[right] = array[right], array[left]
				left += 1
				right -= 1
		
		array[pivot], array[left] = array[left], array[pivot]
		return(qsort(array[0:left]) + qsort(array[left::]))
	else:
		return array

if __name__ == '__main__':
	# test ls
	x = [3,10,2,8,23,12,5]
	print(qsort(x))