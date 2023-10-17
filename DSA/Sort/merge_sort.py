# def merge_sort(a,b):
#     res = a+b
#     return sorted(res)
# a = [10,15,20]
# b = [5,6,6,30]
# print(merge_sort(a,b))

def merge_sorttwo_array(arr1,arr2):
    add_Array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            add_Array.append(arr1[i])
            i+=1
        else:
            add_Array.append(arr2[j])
            j +=1
            
    add_Array += arr1[i:]
    add_Array += arr2[j:]
    
    return add_Array
        

arr1 = [2,3,10,50]
arr2 = [1,2,6,25,35,40]
print(merge_sorttwo_array(arr1,arr2))


def merge(a, b):
    res = []
    m = len(a)
    n = len(b)
    
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    while i < m:
        res.append(a[i])
        i += 1
        
    while j < n:
        res.append(b[j])
        j += 1
    return res

a = [2, 3, 10, 50]
b = [5, 1, 2, 6, 25, 35, 40]
print(merge(a, b))




        






