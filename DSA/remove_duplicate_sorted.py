#  Remove Duplicates from Sorted Array II

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    currentIndex = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[currentIndex -2]:
            nums[currentIndex] = nums[i]
            currentIndex += 1
    return currentIndex
nums = [1,1,1,2,2,3]
removeDuplicates(nums)


"""_summary_
    Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""
Given a sorted array of integers, what can be the minimum worst-case time complexity to find ceiling of a number x in given array? The ceiling of an element x is the smallest element present in array which is greater than or equal to x. Ceiling is not present if x is greater than the maximum element present in array. For example, if the given array is {12, 67, 90, 100, 300, 399} and × = 95, then the output should be 100.
Initialize two variables, start and end, to 0 and n-1, respectively, where n is the number of elements in the array.

While start is less than or equal to end, do the following:

a. Calculate the middle index as mid = (start + end) / 2.

b. Compare the middle element of the array, arr[mid], with x.

c. If arr[mid] is equal to x, then arr[mid] is the ceiling of x. Return arr[mid].

d. If arr[mid] is less than x, set start = mid + 1 because the ceiling of x must be in the right half of the remaining array.

e. If arr[mid] is greater than x, set end = mid - 1 because the ceiling of x must be in the left half of the remaining array.
"""
def find_ceiling(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    if start < len(arr):
        return arr[start]
    else:
        return None  # No ceiling found, x is greater than the maximum element

# Example usage:
arr = [12, 67, 90, 100, 300, 399]
x = 95
ceiling = find_ceiling(arr, x)
print(ceiling)  # Output: 100
