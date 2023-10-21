def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i],end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j],end=" ")
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i],end=" ")
        i += 1

    while j < n:
        print(arr2[j],end=" ")
        j += 1

# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printUnion(arr1, arr2, m, n)



def union_array(arr1, arr2): 
    m = len(arr1)
    n = len(arr2) 
    i = 0
    j = 0
    
    # keep track of last element to avoid duplicates
    prev = None
    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != prev:
                print(arr2[j], end=' ')
                prev = arr2[j]
            j += 1
        else:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
            j += 1
            
    while i < m:
        if arr1[i] != prev:
            print(arr1[i], end=' ')
            prev = arr1[i]
        i += 1

    while j < n:
        if arr2[j] != prev:
            print(arr2[j], end=' ')
            prev = arr2[j]
        j += 1
    
# Driver Code 
if __name__ == "__main__": 
    arr1 = [1, 2, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
        
    union_array(arr1, arr2) 
    
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1

# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)


def IntersectionArray(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: array of intersection of two array or -1
    '''

    Intersection = []
    i = j = 0
    
    while i < n and j < m:
        if a[i] == b[j]:

            # If duplicate already present in Intersection list
            if len(Intersection) > 0 and Intersection[-1] == a[i]:
                i+= 1
                j+= 1

            # If no duplicate is present in Intersection list
            else:
                Intersection.append(a[i])
                i+= 1
                j+= 1
        elif a[i] < b[j]:
            i+= 1
        else:
            j+= 1
            
    if not len(Intersection):
        return [-1]
    return Intersection
# Driver Code
if __name__ == "__main__":

    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6, 7, 8]
    
    l = IntersectionArray(arr1, arr2, len(arr1), len(arr2))
    print(*l)