#Single Inheritence: Child class derives members of one parent class.

class ParentClass:
    def per_func(self):
        print("I am parent class function")
        
class ChildClass(ParentClass):
    def child_fun(self):
        print("I am child class function")
        
obj1 = ChildClass()
obj1.per_func()
obj1.child_fun()