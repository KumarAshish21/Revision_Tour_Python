t=int(input())
for i in range(t):
    X, Y = map(int,input().split())
    if X<=Y and (X+200)>=Y:
        print('YES')
    else:
        print('NO')