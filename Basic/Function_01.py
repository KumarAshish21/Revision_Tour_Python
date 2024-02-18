# Basic Function Syntax

# Problem: Write a function to calculate and return the square of a number.

# def squre(num):
#     return num * num
# num = int(input("Enter a number: "))
#
# print("The square of the number is: ", squre(num))

# roblem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
#
# def multiply(a, b):
#     return a * b
#
# print("The product of the numbers is: ", multiply('a', 4))

# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# def circle(radius):
#     area = 3.14 * radius * radius
#     circumference = 2 * 3.14 * radius
#     return area, circumference
# print("The area and circumference of the circle is: ", circle(5))


username = "chaiaurcode"

# def func():
#     username = "char"
#     print(username)
#
# print(username)
# func()
#
# x = 99
#
# def func2(x,y):
#     z = x + y
#     return z
# result = func2(1,4)
# print(result)

# def func3():
#     global x
#     x = 100
# func3()
# print(x)

# def f1():
#     x = 88
#     def f3():
#         print(x)
#     f3()
# f1()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual
square = chaicoder(2)
print(square(4))

