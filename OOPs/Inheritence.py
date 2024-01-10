"""Python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.


"""

# Single Inheritence
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# class DerivedClassName(modname.BaseClassName):


# 9.5.1. Multiple Inheritance¶


"""you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.
"""
 
# 9.6. Private Variables¶
# Private Instance variables that can not be accessed except from inside an object don't exit in Python.
# However, there is a convention that is followed by most Python Code: a name prefixed with an underscore(_spam)
# 

class Mapping:
    def __init__(self, iterable):
        self.items_list=[]
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update = update  # private copy of original update() method
    
class MappingSubclass(Mapping):
    def update(self,keys,values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)