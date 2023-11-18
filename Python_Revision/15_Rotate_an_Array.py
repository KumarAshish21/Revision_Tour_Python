# Using Temporary Array: Create a new array and copy elements from the original array with adjusted indices to simulate the rotation.

def rotate_array_temporary(nums,k):
    n = len(nums)
    k %= n
    
    temp = [0] * n
    
    for i in range(n):
        temp[(i+k)%n] = nums[i]
        
    for j in range(n):
        nums[i] = temp[i]
        
nums = [1,2,3,4,5,6,7]
rotate_array_temporary(nums,3)
print(nums)

def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(nums, k):
    n = len(nums)
    k = k % n
    
    reverse_array(nums, 0, n - k - 1)
    reverse_array(nums, n - k, n - 1)
    reverse_array(nums, 0, n - 1)
    
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_reversal(nums, 3)
print(nums)

# using Juggling Algorithm 
from math import gcd

def rotate_array_juggling(nums,k):
    n = len(nums)
    k = k % n
    num_cycles = gcd(n , k)
    
    for i in range(num_cycles):
        temp = nums[i]
        j = i
        
        while True:
            next_index = (j + k)% n
            if next_index == i:
                break
            nums[j] = nums[next_index]
            j = next_index
        nums[j] = temp
        
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_juggling(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Cyclic Replacements:

def rotate_array_cyclic_replacements(nums, k):
    n = len(nums)
    k = k % n  # To handle cases where k is greater than n

    count = 0

    for start in range(n):
        current = start
        prev = nums[start]

        while True:
            next_index = (current + k) % n
            temp = nums[next_index]
            nums[next_index] = prev
            prev = temp
            current = next_index
            count += 1

            if start == current:
                break

        if count == n:
            break

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_cyclic_replacements(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Using a Queue

from collections import deque

def rotate_array_queue(nums, k):
    n = len(nums)
    k = k % n  # To handle cases where k is greater than n

    if k == 0:
        return

    queue = deque(nums)

    for _ in range(k):
        queue.appendleft(queue.pop())

    for i in range(n):
        nums[i] = queue.popleft()

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_queue(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]


# Using Left Shift (Block Swap Algorithm):
def block_swap(arr, start, end, size):
    for i in range(size):
        arr[start + i], arr[end + i] = arr[end + i], arr[start + i]

def rotate_array_block_swap(nums, k):
    n = len(nums)
    k = k % n  # To handle cases where k is greater than n

    if k == 0:
        return

    if k > n // 2:
        k = n - k

    # Swap the appropriate blocks
    block_swap(nums, 0, n - k, k)
    
    while k < n:
        if n - k >= k:
            block_swap(nums, k, n - k, k)
            k = n - k
        else:
            block_swap(nums, k, n - k, n - k)
            n -= k

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_block_swap(nums, 3)
print(nums)  # Output: [4, 5, 6, 7, 1, 2, 3]
