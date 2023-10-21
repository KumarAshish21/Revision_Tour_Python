# def printUnion(a, b):
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if i > 0 and a[i] == a[i - 1]:
#             i = i + 1
#         elif j > 0 and b[j] == b[j - 1]:
#             j = j + 1
#         elif a[i] < b[j]:
#             print(a[i], end=" ")
#             i = i + 1
#         elif a[i] > b[j]:
#             print(b[j], end=" ")
#             j = j + 1
#         else:
#             print(a[i], end=" ")
#             i = i + 1
#             j = j + 1

#     while i < len(a):
#         if i == 0 or a[i] != a[i - 1]:
#             print(a[i], end=" ")
#         i = i + 1

#     while j < len(b):
#         if j == 0 or b[j] != b[j - 1]:
#             print(b[j], end=" ")
#         j = j + 1

# a = [2, 3, 3, 3]
# b = [2, 3, 5, 8, 9, 10, 15]

# printUnion(a, b)


def find_union(sorted_array1, sorted_array2):
    union = []
    i = j = 0

    while i < len(sorted_array1) and j < len(sorted_array2):
        if sorted_array1[i] < sorted_array2[j]:
            union.append(sorted_array1[i])
            i += 1
        elif sorted_array1[i] > sorted_array2[j]:
            union.append(sorted_array2[j])
            j += 1
        else:
            # If both elements are equal, add one to the union and advance both pointers
            union.append(sorted_array1[i])
            i += 1
            j += 1

    # Add any remaining elements from both arrays, if any
    while i < len(sorted_array1):
        union.append(sorted_array1[i])
        i += 1

    while j < len(sorted_array2):
        union.append(sorted_array2[j])
        j += 1

    return union

# Example usage:
arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
union_result = find_union(arr1, arr2)
print(union_result)  # Output: [1, 2, 3, 4, 5, 6, 7]
