# Naive Approach

def invcount(arr) :
    n = len(arr) 
    res = 0
    for i in range (n - 1) :
        for j in range(i + 1,n) :
            if arr[i] > arr[j]:
                res += 1 
    print(res)
    
    
arr = [2,4,1,3,5]
invcount(arr)


# Python 3 program to count inversions in an array

def mergeSort(arr, n):
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)

def _mergeSort(arr, temp_arr, left, right):

	inv_count = 0

	if left < right:

		mid = (left + right)//2

		inv_count += _mergeSort(arr, temp_arr,
								left, mid)

		inv_count += _mergeSort(arr, temp_arr,
								mid + 1, right)


		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count


def merge(arr, temp_arr, left, mid, right):
	i = left	 
	j = mid + 1 
	k = left	 
	inv_count = 0

	while i <= mid and j <= right:

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return inv_count


arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)


# Time Complexity: O(n * log n), The algorithm used is divide and conquer i.e. merge sort whose complexity is O(n log n).
# Auxiliary Space: O(n), Temporary array.