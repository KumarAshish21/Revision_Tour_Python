# What is Encapsulation in python?
# Wrapping up data and methods working on data together in a single unit (ie class) is called as encapsulation.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
        
    def display(self):
        print(f"name is: {self.name} and salary is: {self.salary}")
        

# What is the need of encapsulation
