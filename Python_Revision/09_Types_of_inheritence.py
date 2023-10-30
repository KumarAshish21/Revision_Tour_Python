# Types of Inheritence

# Single Inheritance
# Multi-level Inheritance
# Hierarchical Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Cyclic Inheritance

#  Single Inheritance

# One Parent and one child class

# Multi-level Inheritance
# Parent class and child class further inherited into new class forming multiple levels
# Object-> Parent-> Child-> Grand_child


# class Human_beings(object):
#     def __init__(self):
#         print("human being constructor called")
#         self.name = input("Enter your name")
        

# class Employee(Human_beings):
#     def __init__(self):
#         print("Employee constructor called")
#         self.salary=float(input("Enter your salary:"))
        

# class Managers(Employee):
#     def __init__(self):
#         print("Managers constructor called")
#         self.bonus = float(input("Enter your bonus"))

# m1= Managers()
        
        
# Hierarchical Inheritance
# One Parent and multiple child classes

                #     object
                #        |
                #        |
                #        |
                #     Parent
                #        /\
                #       /  \
                #   Child1  Child2  

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("This is person display method")
class Employee(Person):
    def __init__(self, name, age,sal):
        super().__init__(name, age)
        self.salary = sal
    def display1(self):
        print("This is Employee display method")
class Student(Person):
    def __init__(self, name, age,m):
        super().__init__(name, age)
        self.marks =m
    def display2(self):
        print("This is Student display method")
        
s1 = Student('Ashish',21,90)
e1 = Employee("Aman",23,35000)
p1 = Person("Ashish",26)

s1.display()
p1.display() #attrubute error
s1.display2() #attrubute error