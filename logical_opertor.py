t = int(input())
for i in range(t):
    A, B = map(int, input().split())
    if A != B and (A%2 != 0 and B%2 != 0):
        print("A and B are different and are odd")
    elif A != B and (A%2 == 0 and B%2 == 0):
        print("A and B are different and are even")
    else:
        print("Doesn't matter")