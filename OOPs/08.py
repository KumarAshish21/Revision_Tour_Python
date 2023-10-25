# 4. Are access specifiers used in python?
# Python does not make use of access specifiers specifically like private, public, protected, etc. However, it does not derive this from any variables. It has the concept of imitating the behaviour of variables by making use of a single (protected) or double underscore (private) as prefixed to the variable names. By default, the variables without prefixed underscores are public.

class IntervieBitEmployee:
    
    # protected members
    _emp_name = None
    _age = None
    
    # Private members
    
    __branch = None
    
    # Constructor
    def __init__(self,emp_name,age,branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch
        
    def display():
        print(self._emp_name+""+self._age+""+self.__branch)
        

# Is it possible to call parent class without its instance creation?
# Yes, it is possible if the base class is instantiated by other child classes or if the base class is a static method.
# How is an empty class created in python?
# An empty class does not have any members defined in it. It is created by using the pass keyword (the pass command does nothing in python). We can create objects for this class outside the class.

# Why is finalize used?
# Finalize method is used for freeing up the unmanaged resources and clean up before the garbage collection method is invoked. This helps in performing memory management tasks.

# What is init method in python?
# The init method works similarly to the constructors in Java. The method is run as soon as an object is instantiated. It is useful for initializing any attributes or default behaviour of the object at the time of instantiation.

#  How will you check if a class is a child of another class?
# This is done by using a method called issubclass() provided by python. The method tells us if any class is a child of another class by returning true or false accordingly.

class Parent(object):
   pass   
 
class Child(Parent):
   pass   
 
# Driver Code
print(issubclass(Child, Parent))    #True
print(issubclass(Parent, Child))    #False

obj1 = Child()
obj2 = Parent()
print(isinstance(obj2, Child))    #False 
print(isinstance(obj2, Parent))  