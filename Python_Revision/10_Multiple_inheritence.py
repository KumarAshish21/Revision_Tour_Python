# Class is derived from muliple base classes

class Country:
    def __init__(self):
        print("Country class constructor")
        self.Office="Delhi"
        
class State:
    def __init__(self):
        
        print("State class constructor")
        self.Office="Mumbai"
        
class District(State,Country):
    def __init__(self):
        super().__init__()
        print("District class constructor")

d = District()
print(d.__dict__)

# MRO:- Method Resolution Order
# MRO represents how properties (attributes+methods) are searched in inheritance.
# Rule 1 - Python First search in child class and then goes to parent class.
# Priority is to child class
# Rule 2 - MRO Follows Defth first left to Right approach
# Rule 3 - You can use mro() method for knowing mro of any class objects
