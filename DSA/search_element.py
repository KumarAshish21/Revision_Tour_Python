def search(arr, N, X):
    for num in range(len(arr)):
        if arr[num] == X:
            return num
    return -1
N = 5
arr = list({1,2,3,4,5})
X = 5
print(search(arr, N, X))