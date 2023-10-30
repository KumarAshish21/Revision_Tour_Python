"""Basics of 00P
Types of variables & methods
Inheritance
Polymorphism
Encapsulation
Abstraction
Interface
Mini-Project using OOP
Interview questions
 """
 
# Ways of organizing programs.
# • Python supports multiple paradigms. These are as follows:-
# 1) Procedural oriented paradigm
# 2) Functional oriented paradigm
# 3) Object-oriented paradigm

# An object in OOP represents real-life objects. ex. Email, man, student, employee etc
# Every object has two properties.
# 1) attributes
# 2) Behaviours
# Attributes:- heading,subject,name, recipients list
# Behaviours:- sending,Adding attachments

# What is Object-Oriented Programming(OOP)?
# Object-oriented programming is an approach of writing programs by creating classes and objects.
# More focus is on data rather than logic.
# Why OOP?
# To solve real-world problems effectively.
# OOP provides some features :-
# 1) Inheritance :- reusability
# 2) encapsulation: - data security
# 3) abstraction :- Data hiding

# What is class?
# Class is a template/blueprint/prototype for creating objects
# Every objects belong to some class
# Class is a collection of attributes and methods.
# Class is a collection of objects.
# Technically, class is a user-defined datatype.

# class Class_name:
#     #attribute
#     #methods
    
# obj1 = Class_name([args])
# obj2 = Class_name([args])

# Object is instance
# Examples
# obj2 = Class_name([args])

# class Email:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name)

# e1 = Email('Ashish',25)
# e2 = Email('Atul',24)

# Constuctor & types of constructor
# What is constructor?
# Special method used for initializing objects with attributes
# It is _init__0 method
# First arguments is 'self.

# Types of constructor?
# Parameterized constructor
# Non-Parameterized constructor
# Default Constructor

# class Employee:
#     def __init__(self,salary,age):
#         self.salary = salary
#         self.age = age
    
# e1  = Employee(24000,25)
# e2 = Employee(25000,26)
# print(e1.__dict__)
# print(e2.__dict__)
# # Without constructor :- object can't be created

# Memory representation and self variable
# Python memory allocated HEAP memory

# . dot notation is used for accessing particular object

# memory allocation for object
# 2. memory reference returned to the object
# 3. memory reference automatically passed inside constructor.
# 4. constructor creates/intiialize variables at that memory reference
# what is self:

# How to access class members?

# Class members :- Attributes(variables) + Actions(Methods)
# We can access these variables using object outside the class.
# Syntax:
# Accessing attribute:- object_name.variable_name
# Accessing method:- object name.method name()


# class Employee:
#     def __init__(self,salary,age):
#         self.salary = salary
#         self.age = age
#     def display(self):
#         # print(self.salary)
#         # print(self.age)
#         print(f"salary is {self.salary} and age is {self.age}")
# e1  = Employee(24000,25)
# e2 = Employee(25000,26)

# print(e1.salary)
# print(e1.age)

# Built-in class Functions
# getattr(object _name, attribute_name) -> Fetch object
# setattr(object _name, attribute_name, new_value) -> change value
# delattr(object _ name, attribute_name) -> delete value
# hasattr(object _ name, attribute _name) -> return True and False


# getattr example
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# e1 = Employee('Ashish',26)
# e2 = Employee('Abhishek',20)

# print(getattr(e1,'age'))
# print(getattr(e1,'name'))
    
# # setattr example

# setattr(e2,'name','Aman')
# print(getattr(e2,'name'))

# # delattr example

# delattr(e2,'age')
# print(e2.__dict__)

# # hasattr example

# print(hasattr(e1,'name'))
# print(hasattr(e2,'age'))

# Built-in class attribute

# __dict__:- Dictionary containing class's namespace maintaine namespace
# __doc__:- Class documentation string.
# __name__: - Class Name
# __module__:- Module name in which class is defined
# __bases__:- List of base classes

# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# e1 = Employee('Ashish',26)
# e2 = Employee('Abhishek',20)
# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)


# isinstance() function return boolean value

# class Demo:
#     pass

# d1 = Demo()
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(f"name is:{self.name} and age is {self.age}")
        
# e1 = Employee('Ashish',26)
# e2 = Employee('Abhishek',20)

# print(isinstance(e1,Employee))

# print(isinstance(d1, Employee))

# Instance variables & intance methods

# Types of variables

# Instance and class

# Instance variables

# Variables made for particular instance.
# Separate copy is created for every object.
# Values of variables differs from object to object.
# Modification in one object won't effect other objects

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
        
# std1 = Student('Ashish',24)
# std2 = Student('Abhishek',20)
# std3 = Student('Aman',23)

# std1.age = 26
# print(std1.__dict__)
# print(std2.__dict__)

# creating instance variables
# using constructor
# using instance method
# Outside class

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def display(self):
#         print(self.name, self.marks)
        
#     def  change_data(self):
#         # self.name = "Gaurav"
#         # self.marks = 30
#         self.name = input("Enter the name :")
#         self.marks = int(input("Enter your marks :"))
# std1 = Student('Ashish',24)
# std2 = Student('Abhishek',20)
# std3 = Student('Aman',23)
        
# # std2.display()

# std2.change_data()
# std2.display()

# print(std2.__dict__)

# Class Variables and class methods

# class Employee:
#     company_name = "infosys"
    
#     def __init__(self,nm,sal):
#         self.name = nm
#         self.salary = sal
        
# e1 = Employee('Jay',40000)
# e2 = Employee('Pooja',25000)

# # print(Employee.company_name)
# # print(e1.company_name)

# # if you want to modify then use class reference

# Employee.company_name = 'TCS'
# print(Employee.company_name)

# I can modified using class method
# Method which works on class variables
# First argument is class reference
# Made using decorator '@classmethod'

class Employee:
    company_name = "Infosys"

    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal

    @classmethod
    def get_company_name(cls):
        print(f"Company name is: {cls.company_name}")
        cls.company_name = 'TCS'
        print(cls.company_name)

e1 = Employee("Ashish", 30000)
e2 = Employee("Abhishek", 50000)

Employee.get_company_name()
