def findFloor(A,X):
    n = len(A)
    floor = -1
    for i in range(n):
        if A[i]<=X:
            floor = i
     
    return floor





