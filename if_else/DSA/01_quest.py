def searchInSorted(arr, N, K):
        #Your code here
        low = 0
        high = N-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == K:
                index=mid
                return 1
            elif arr[mid] < K:
                low = mid + 1
            else:
                high = mid-1
        return -1