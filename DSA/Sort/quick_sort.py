# Quick Sort using Lomuto Partition

def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:  # error
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


def qSort(arr, l, h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        qSort(arr, l, p - 1)
        qSort(arr, p + 1, h)


arr = [8, 4, 7, 9, 3, 10, 5]

qSort(arr, 0, 6)

print(*arr)


# Quick Sort using Hoare's Partition

def hoarsePartition(arr, l, h):
    pivot = arr[l]

    i = l - 1
    j = h + 1

    while True:

        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def qSort(arr, l, h):
    if l < h:
        p = hoarsePartition(arr, l, h)
        qSort(arr, l, p)
        qSort(arr, p + 1, h)


arr = [8, 4, 7, 9, 3, 10, 5]

qSort(arr, 0, 6)

print(*arr)

# Average Time Complexity :

# Running time for partition of N elements is O(N)
#  Quicksort Running time:
# call partition. Get two subarrays of sizes NL and NR
# (what is the relationship between NL, NR and N)
 
#  Then Quicksort the smaller parts
 
#  T(N) = N + T(NL) + T(NR)
