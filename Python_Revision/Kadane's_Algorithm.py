def max_circular_subarray_sum(nums):
    def max_subarray_sum(nums):
        max_sum = float('-inf')
        current_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    def min_subarray_sum(nums):
        min_sum = float('inf')
        current_sum = float('inf')

        for num in nums:
            current_sum = min(num, current_sum + num)
            min_sum = min(min_sum, current_sum)

        return min_sum

    total_sum = sum(nums)
    max_non_circular_sum = max_subarray_sum(nums)
    max_circular_sum = total_sum - min_subarray_sum(nums)

    return max(max_non_circular_sum, max_circular_sum)

# Example usage:
nums = [1, -2, 3, -2]
result = max_circular_subarray_sum(nums)
print(result)  # Output: 3 (The maximum circular subarray is [3])
