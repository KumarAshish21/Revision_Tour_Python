# Two Sum Problem Quetions
# Brute Force Solution:
def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i +1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return[]

# 2. Two Pointers Solution (requires sorted array):

def two_sum_two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
            
        else:
            right -= 1
    
    return []


# 3 Hash Table (Dictionary) Solution:

def two_sum_hash_table(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement],i]
        num_dict[num] = i
    return []

#4. Optimized Hash Table Solution:

def two_sum_optimized_hash_table(nums,target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

#5 Using set 

def two_sum_sets(nums, target):
    num_set = set()
    for num in nums:
        complement = target - num
        if complement in num_set:
            return [nums.index(complement), nums.index(num)]
        num_set.add(num)
        
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum_sets(nums, target)
print(result)