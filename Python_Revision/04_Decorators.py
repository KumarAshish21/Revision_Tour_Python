# what is decorators
# Functions which takes other functions as input, add additional functionalities and returns it.
# It callable Python object which modifies other function/class.
# type of two decorators
# Function modify and class modify

# Function Modify

# def decor(func):
#     def inner(): #existing functionality
#         func()
#         print('Welocome')
#     return inner

# @decor
# def printer():
#     print("Welcome")
#     print("Welcome")

# # printer = decor(printer)
# printer()

# Example2
# def decor(addition):
#     def inner():
#         result = addition()
#         num3 = int(input("Enter third number"))
#         result = result+num3
#         return result
#     return inner()
        
# @decor
# def addition():
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number"))
#     result = num1+num2
#     return result

# addition= decor(addition)
# print("Addition is:",addition())

# Multiple decorators on one function

# def decor1(func):
#     def inner():
#         return func().upper()
#     return inner

# def decor2(func):
#     def inner():
#         parts = func().split()
#         return ' '.join(parts)
#     return inner

# @decor2
# @decor1
# def get_name():
#     name = input("Enter the first name: ")
#     sirname = input("Enter the Sirname: ")
#     full_name = name + " " + sirname
#     return full_name

# result = get_name()

# print(result)




# One decorator perform multiple methods
# def decor(func):
#     def inner(*args):
#         for num in args[1:]:
#             if num == 0:
#                 return "can't devide by zero."
#         return func(*args)
#     return inner
# @decor
# def div1(a,b):
#     return a/b
# @decor
# def div2(a,b,c):
#     return a/b/c

# print(div1(10,5))
# print(div1(10,0))

# print(div2(0,10,5))

# def smart_devider(f):
#     def inner(num1,num2):
#         if num2==0:
#             print("Can't devide by zero")
#             return
#         f(num1,num2)
#     return inner
# @smart_devider
# def Division(num1,num2):
#     print("Diviison is:", num1/num2)
# # smart_devider(Division)
# Division(10,0)

from functools import partial

def add(n1,n2,n3,n4):
    return n1+n2+n3+n4

add=partial(add,n1=2,n2 =3)
print(add(n3=5,n4=10))
