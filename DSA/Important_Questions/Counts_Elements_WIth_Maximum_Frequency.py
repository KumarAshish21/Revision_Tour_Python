# 3005. Count Elements With Maximum Frequency
# Easy
# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.


from collections import Counter


def maxFrequencyElements(nums):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    max_freq = max(freq_dict.values(), default=0)

    count_max_freq = sum(freq for freq in freq_dict.values() if freq == max_freq)

    return count_max_freq

# Test cases
nums1 = [1, 2, 2, 3, 1, 4]
print(maxFrequencyElements(nums1))  # Output: 4

nums2 = [1, 2, 3, 4, 5]
print(maxFrequencyElements(nums2))  # Output: 5



