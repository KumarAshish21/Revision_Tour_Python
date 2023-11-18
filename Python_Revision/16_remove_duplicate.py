# Remove Duplicates from Sorted Array:
# Remove duplicate elements from a sorted array in-place and return the new length

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    new_length = 1  # Initialize the new length as 1 (at least one element is unique)
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[new_length] = nums[i]
            new_length += 1

    return new_length

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5]
new_length = remove_duplicates(nums)
print(nums[:new_length])  # Output: [1, 2, 3, 4, 5]
