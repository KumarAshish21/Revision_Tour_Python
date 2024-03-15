# Find the Pivot Integer
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.



def find_pivot(n):
    if n == 1:
        return 1
    for i in range(1,n+1):
        if sum(range(1,i+1)) == sum(range(i,n+1)):
            return i
    return -1
n = 4
print(find_pivot(n))
