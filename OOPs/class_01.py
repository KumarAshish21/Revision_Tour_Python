class MyClass:
    i = 12345
    
    def f(self):
        return 'hello World'
    
x = MyClass()



"""When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly created class instance. So in this example, a new, initialized instance can be obtained by:"""
class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

# 9.3.3. Instance Objects¶

# The other kind of instance attribute reference is a method. A method is a function that “belongs to” an object

# Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances

# 9.3.4. Method Objects¶

# x.f() :  it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time.


