#  How do you access parent members in the child class?
# By using Parent class name: You can use the name of the parent class to access the attributes as shown in the example below:
class Parent(object):
    
    def __init__(self,name):
        self.name = name
        
# class Child(Parent):
#     def __init__(self,age, name):
#         Parent.name = name
#         self.age =age
    
#     def display(self):
#         print(Parent.name,self.age)
        
# obj = Child("Ashish",26)

# obj.display()

# By using super(): The parent class members can be accessed in child class using the super keyword.

class Child(Parent):
    def __init__(self,age, name):
        super(Child,self).__init__(name)
        self.age = age
        
    def display(self):
        print(self.name,self.age)
        
obj =Child("Ashish", 26)

obj.display()
