class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
        
    def average_grade(self):
        return sum(self.grades)/ len(self.grades)
    

student = Student("Ashish",(100,90,34))
print(student.name)
print(student.average_grade())


class Person:
    
    def __init__(self, name, age):
        self.name =name 
        self.age = age
        
    def __str__(self):
        return f"Person'{self.name}', {self.age} years old"
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
bob = Person("Ashish",25)
print(bob)

# Classes and objects (Python 3.10)
# This coding exercise requires you to complete an implementation of three methods of a class:

# The __init__  method, which should take an argument, name . It should initialise self.name  to be the argument, and self.items  to be an empty list.

# The add_item  method, which should append a dictionary representing an item to the store's items  property. The dictionary should have keys name  and price .

# The stock_price  method, which should add up each item price inside self.items  to come up with a total, and return that.

class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        item = {'name':name, 'price':price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        return sum(item['price'] for item in self.items)
        # Add together all item prices in self.items and return the total.
