# Hierarchical Inheritance: When a parent class is derived by more than one child class, it is called hierarchical inheritance.
class A:
    def a_func(self):
        print("I am from the parent class.")
        
class B(A):
    def b_func(self):
        print("I am from the first child")
        
class C(B):
    def c_func(self):
        print("I am from the second child")
        
obj1 = B()
obj2 = C()
obj1.a_func()
obj1.b_func()
obj2.a_func()
obj2.c_func()

