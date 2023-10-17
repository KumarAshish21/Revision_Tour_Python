def merge_sort_single_array(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        a[k:] = left[i:] + right[j:]

a = [10, 15, 20, 40, 8, 11, 55]
merge_sort_single_array(a)

print(a)

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


a = [10, 15, 20, 40, 8, 11, 55]

merge(a, 0, 3, 6)

print(*a)

