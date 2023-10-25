# Write a Python program for factorial of a number using recursion

# def fact(n):
#     if n ==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# Prime Number

# def prime(n,i):
#     if i==1:
#         return i
#     if n%i==0:
#         return 0
#     return prime(n,n-1)
# n =int(input("Enter the number"))
# ind =prime(n,n-1)

# if ind ==1:
#     prime("Prime Number")
    
# if ind ==0:
#     prime("Not a prime number")
    
# Write a Python program for printing n to 1 sequence

n = int(input("Enter the value of n:"))

def natural(n):
    if n==1:
        return
    print(n)

    return natural(n-1)
print(natural(n))
