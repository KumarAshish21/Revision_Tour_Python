# what is inheritence
# Deriving a new class from an existing class so that new class inherits all members (attributes + methods) of existing class is called as inheritance.
# Old class :- Parent class, Base class,
# Existing class, Super class
# New class :- Child class, sub class, derived class
# All classes in Python are derived from built in object class
# How to create a child class:

# class Parent(object):
#     #attribute+methods
# class Child(Parent):

# class Employee:
#     bonus = 20000
    
#     def display(self):
#         print("This is employee class method")
        
# class Manager(Employee):
#     bonus1 = 50000
#     def show(self):
#         print("This is manager class")
        
# e1 = Employee()
# m1 = Manager()

# e1.display()
# m1.show()
# print(m1.bonus)


# Need of Inheritence
# For code-reuseability(Write Once use many times)
# When you have relations among classes

# how to use constructor in heritence

# By default constructor of parent class available to child class

# constructor overriding

# class Father:
#     def __init__(self):
#         print("Father constructor called")
#         self.vahicle = "Scooter"
# class Son(Father):
#     def __init__(self):
#         print("Son contructor called")
#         self.vahicle = "BMW"

# s = Son()
# print(s.__dict__)

# Super() function

# Using super() function, we can access parent class properites
# This function returns a temporary object which contains reference to parent class
# It makes inheritance more manageable and extensible

class Computer(object):
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        print("Computer class constructor called")
        
        

class Mobile(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)
        self.model='IphoneX'
        print("Mobile class constuctor called")
        
Apple = Mobile('8GB','512GB')
print(Apple.__dict__)
