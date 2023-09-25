# You are given an array arr(0-based indexing). The size of the array is given by n. You need to get the element at index i and return it. If no element exists at i then return -1.
"""
n = =6
arr[] = {1 2 3 4 5 6}
index = 0
Output: 1
Explanation: The array is {1 2 3 4 5 6}.
The index given is 0. so element at 0th
index is 1.
"""
"""
n = 4
arr[] = {1 2 3 4}
index = 4
Output: -1
Explanation: The array is {1 2 3 4}. The
index given is 4. Here no element exists
at the 4th index, so the answer is -1.
"""

def getByIndex(arr, n, idx):
    if 0 <= idx < len(arr):
        return arr[idx]
    else:
        return -1

if __name__ == '__main__':
    tcs = int(input("Enter the number of test cases: "))
    
    for _ in range(tcs):
        n = int(input("Enter the length of the array: "))
        arr = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
        idx = int(input("Enter the index to get the element from: "))
        
        result = getByIndex(arr, n, idx)
        print("Result:", result)
