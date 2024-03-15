# Two_Sum Easy
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution:

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))


def two_sum(nums,target):
    dict={}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in dict:
            return [dict[diff],i]
        dict[n] = i
    return []
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))


