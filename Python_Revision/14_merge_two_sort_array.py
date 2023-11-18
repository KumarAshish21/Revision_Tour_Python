# using Extra space
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0,0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
            
        else:
            merged_array.append(arr2[j])
            j+=1
            
    
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array

# In-Place Merging

def merge_sorted_arrays_inplace(arr1, arr2):
    m,n = len(arr1), len(arr2)
    
    arr1 += [0] * n
    
    i,j,k = m-1, n - 1, m + n -1
    
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
            
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    return arr1


# Two Pointer

def merge_sorted_arrays_two_pointers(arr1, arr2):
    merged_array = [0] * (len(arr1) + len(arr2))
    i, j, k = 0,0,0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array[k] = arr1[i]
            
            i += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
        
        k += 1
    
    while i < len(arr1):
        merged_array[k] = arr1[i]
        i += 1
        k += 1
        
    while j < len(arr2):
        merged_array[k] = arr2[j]
        j += 1
        k += 1
    
    return merged_array

# using Merge Sort
def merge_sort(arr1, arr2):
    merge_array = []
    i, j = 0,0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[j] < arr2[j]:
            merge_array.append(arr1[i])
            i += 1
        else:
            merge_array.append(arr2[j])
            j += 1
    merge_array.extend(arr1[i:])
    merge_array.extend(arr2[j:])
    
    return merge_array