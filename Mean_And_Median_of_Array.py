"""
Given an array a[ ] of size N. The task is to find the median and mean of the array elements. Mean is average of the numbers and median is the element which is smaller than half of the elements and greater than remaining half.  If there are odd elements, the median is simply the middle element in the sorted array. If there are even elements, then the median is floor of average of two middle numbers in the sorted array. If mean is floating point number, then we need to print floor of it.

Note: To find the median, you might need to sort the array. Since sorting is covered in later tracks, we have already provided the sort function to you in the code.
"""

class Solution:
    def median(self, A, N):
        A.sort()
        n = len(A) // 2
        if N % 2 == 0:
            k = (A[n] + A[n - 1]) / 2
            return int(k)
        return A[n]

    def mean(self, A, N):
        total = sum(A)
        return total // N

# Example usage:
N = 5
a = [1, 2, 19, 28, 5]

solver = Solution()
mean_result = solver.mean(a, N)
median_result = solver.median(a, N)

print(mean_result, median_result)  # Output: 11 5
