def find_sum_natural(n):
    return n*(n+1)//2
n = 5
print(find_sum_natural(n))

def sum_natural(n):
    sum =  0
    x = 1
    while x<=n:
        sum = sum+x
        x = x + 1
    return sum
n =  int(input('Enter the number:'))
print(sum_natural(n))

# time_Complexity=O(n)
# space_complexity= O(1)