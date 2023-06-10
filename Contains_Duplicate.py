# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        else:
            num_dict[num] = 1
    return False

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicate(nums))

def contains_duplicate_set(nums):
    return len(nums) != len(set(nums))
nums = [1,2,3,1]
print(contains_duplicate_set(nums))


def containsDuplicate(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
nums = [1,2,3,4]
print(containsDuplicate(nums))
