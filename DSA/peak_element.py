def peakElement(arr, n):
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    start, end = 1, n - 2
    while start <= end:
        mid = start + (end - start) // 2
    if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
        return mid
    if arr[mid] >= arr[mid - 1]:
        start = mid + 1
    else :
        end = mid - 1
    return 0
arr = [1, 2, 3]
n = len(arr)
result = peakElement(arr, n)
print(result)

def peakElement(arr, n):
    if n == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n - 1] >= arr[n - 2]:
        return n - 1
    
    start, end = 1, n - 2
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

arr = [1, 2, 3]
n = len(arr)
result = peakElement(arr, n)
print(result)
