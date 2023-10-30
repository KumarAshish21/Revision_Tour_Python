# Python program for implementation of heap Sort

# Input data: [4, 10, 3, 5, 1]
#          4(0)
#         /   \
#      10(1)   3(2)
#     /   \
#  5(3)    1(4)

# The numbers in bracket represent the indices in the array 
# representation of data.

# Applying heapify procedure to index 1:
#          4(0)
#         /   \
#     10(1)    3(2)
#     /   \
# 5(3)    1(4)

# Applying heapify procedure to index 0:
#         10(0)
#         /  \
#      5(1)  3(2)
#     /   \
#  4(3)    1(4)

# The heapify procedure calls itself recursively to build heap
# in top down manner.

# Time Complexity: Time complexity of heapify is O(N*LogN). Time complexity of createAndBuildHeap() is O(N) and overall time complexity of Heap Sort is O(N*LogN) where N is the number of elements in the list or array.

# Heap sort algorithm has limited use because Quicksort and Mergesort are better in practice. Nevertheless, the Heap data structure itself is enormously used.



def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2


	if l < n and arr[i] < arr[l]:
		largest = l


	if r < n and arr[largest] < arr[r]:
		largest = r


	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap


		heapify(arr, n, largest)



def heapSort(arr):
	n = len(arr)


	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)


	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i]) # swap
		heapify(arr, i, 0)


# Driver code to test above

arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i])

