# add = lambda x:lambda y:x+y

# func = add(10)

# print(func(10))

# squre = lambda n:n**2

# def modify(func):
#     num = int(input("Enter a number:"))
#     return func(num)+num

# print(modify(squre))

# IIFE() function

# def Bonus():
#     bonus = 2000
#     return bonus

# def total_salary(b):
#     basic_salary = b()+basic_salary
#     print("total payable salary is:", total_salary)
    
# total_salary(Bonus)


# def outer():
#     def inner():
#         print("Hello World")
#     inner()
#     return inner
# inner = outer()
# inner()


# def display():
#     return "Hello World"

# def Demo(f):
#     print(f())
#     return f

# f1 = Demo(display)
# print(f1())

# HOF
# filter
# map
# reduce

# This function is used to filter out elements of iterable.
# Syntax: filter(function_name, iterable)
# function_name: Function that tests every element of iterable
# iterable:- sequence which needs to be filtered

# numbers = [67,89,91,34,55,45,46,78]
# def filter_even(val):
#     if val%2 ==0:
#         return True
    
# filtered_object= list(filter(filter_even, numbers))
# print(filtered_object)
# print(type(filtered_object))
# print(list(filtered_object))

# values = [False, True, True, 0, 1, 45, False,None]
# print(list(filter(None,values)))




# # Filter in lambda
# numbers = [67,86,45,66,54,31,98,63]
# def greater(num):
#     if num > 60:
#         return True
        
# filtered_object = filter(lambda num:num%2==0,numbers)

# print(list(filtered_object))


# laptops = {'hp':50000,'lenovo':6000,'ASUS':45000,'mackbook':12000}

# budget = float(input("Enter your budget:"))
# def filter_items(ele):
#     if laptops[ele] < budget:
#         return True
#     else:
#         return False
# filtered_object= list(filter(filter_items,laptops))
# print("Prducts are:",filtered_object)
        
    
# Map Function
"""
Map () function:- This is built in higher order function. It apply a specified function on each element of the iterable and perhaps change element.
• Syntax:-
map(function_name, iterable)
"""

nums= [3,4,6,2]
def squre(n):
    return n*n
mapped=list(map(squre,nums))
print(mapped)

# in lambda
nums =[3,4,6,2]
mapped = list(map(lambda n:n*n,nums))
print(mapped)

# add two lists using map function

num1 = [10,20,30]
num2 = [1,2,3]

def add(a,b):
    return a+b

mapped =map(add,num1,num2)
print(list(mapped))

# Reduce

"""reduce () function:- This is built in higher order function defined in functools module.
• syntax:-import functools functools.reduce(function_name, iterable)
• It doesn't return another iterable but returns a single reduced value.
"""

import functools
nums = [5,8,2,10,9]
def func(a,b):
    return a+b
print(functools.reduce(func,nums))

# use in lambda

import functools
nums =[5,8,2,10,9]

print(functools.reduce(lambda a,b:a+b, nums))

# find maximum

nums =[5,8,2,10,9]
def max1(a,b):
    if a > b:
        return a
    else:
        return b
print(functools.reduce(max1,nums))

