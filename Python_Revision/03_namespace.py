# # What are names?
# a = 10
# b = 20
# c = 30
# d = 40
# print(id(20))
# # Dictionary manage unique key
# # Namespace is collection of mapping 
# # Types of namespace-> Built-in namespace, Module level/global namespace, Local namespace, Enclosed Namespace

# # Bulit in namespace->
# print(dir())

# # show namespace contents
# # Global Namespace -> It's create particular for module,
# # When run pYthon program then it will create global namespace

# def display():
#     print('Hello') 
    
# # local namespace is using classes and function

# a = 50
# def func1():
#     a  =10
#     def func3():
#         b = 100
#         print(dir())
#     print(dir())
#     func3()

# def func2():
#     a= 20
# print(dir())

# func1()

# Enclosed Namespace

# LEGB Rule
# Non local variable

# local,enclosed, global,Built-in

# x = 100
# def outer():
#     global x
#     x = x+20
#     print(x)
#     x = 20
#     print(x)
# outer()

# Non local variable (enclosed)
# x = 100
# def outer():
#     x = 20
#     def inner():
#         nonlocal x
#         x = x+20
#         x = 200
#         print(x)
#     inner()
# outer()
        
# LEGB rule work inner to outer loop
# LEGB rule follow two rules

# Closure in Python

# def outer():
#     print("hello")
#     def inner():
#         print("Bye")
#     inner()
# outer()

def outerx():
    x =100
    print("hello")
    def inner():
        y = 200
        print("bye")
    inner()
# new = outerx()
# new()
outerx()


def outer():
    def inner():
        x= 200
        return x
    return inner
inner = outer()
print(inner())

# Closure is a technique by which data gets attached to the code.
# Closure are function objects that remembers values in the enclosing scope even if they are not present in the memory.

