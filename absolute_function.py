t = int(input())
for i in range(t):
    N, A = map(int, input().split())
    chef_chocolates = A
    chefina_chocolates = A - N
    diff = abs(chefina_chocolates - chef_chocolates)
    print(diff)