# Instance variables are for data unique to each instance and class variables are for attriburtes and methods shared by all instances of the class.

class Dog:
    # class variable shared by all instances
    kind = 'canine'
    def __init__(self, name):
        self.name = name  # instance variables unique to each instance
        
d  = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(d.name)

print(e.name)



class Dogs:
    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list for each dog
        
    
    def add_trick(self, trick):
        self.tricks.append(trick)
        
d  = Dogs('Fido')
e = Dogs('Buddy')
d.add_trick("roll over")
e.add_trick('play dead')
print(d.tricks)