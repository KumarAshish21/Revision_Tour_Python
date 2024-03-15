# Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal
# A subarray is a contiguous part of the array.

def numSubarraysWithSum(nums, goal):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == goal:
                count += 1
    return count
nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums,goal))


# method 2
def numSubarraysWithSum(nums, goal):
    count = 0
    sum = 0
    dict = {0:1}
    for i in range(len(nums)):
        sum += nums[i]
        if sum - goal in dict:
            count += dict[sum - goal]
        if sum in dict:
            dict[sum] += 1
        else:
            dict[sum] = 1
    return count