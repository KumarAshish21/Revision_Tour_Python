

t = int(input())
for i in range(t):
    X, Y, Z = map(int, input().split())
    #Variable declared to hold the final population of the town
    total_population = X - Y
    total_population = total_population + Z
    print(total_population)