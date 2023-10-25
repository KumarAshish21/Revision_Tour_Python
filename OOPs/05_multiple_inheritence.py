# This is achieved when one child class derives members from more than one parent class. All features of parent classes are inherited in the child class.

class Parent1:
    def parent1_func(self):
        print("Hi I am first Parent")
        

class Parent2:
    def parent2_func(self):
        print("Hi I am second Parent")
        
class Child(Parent1,Parent2):
    def child_func(self):
        self.parent1_func()
        self.parent2_func()
        
Obj1 = Child()
Obj1.child_func()