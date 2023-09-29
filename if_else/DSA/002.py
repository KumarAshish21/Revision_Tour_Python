arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
x = 1
for i in range(len(arr)):
    if arr[i] == x:
        if i ==0 or arr[i] != arr[i-1]:
            print(i)
        break

