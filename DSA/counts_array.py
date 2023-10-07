# Given a binary sorted non-increasing array of 1s and 0s. You need to print the count of 1s in the binary array.

def count_ones(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == 1:
            left = mid + 1
        else:
            right = mid - 1
    return len(arr) - left

binary_array = [1, 1, 1, 1, 0, 0, 0]
count = count_ones(binary_array)
print(count)



def countOnes(arr):
    count = 0
    for i in arr:
        if i == 1:
            count = count + i
    return count
arr  = [1, 1, 1, 1, 0, 0, 0]
print(countOnes(arr))