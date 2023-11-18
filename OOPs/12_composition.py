# Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.
# technique used when establishing relationships between classes and objects. Understanding compositions is important in object-oriented programming. Compositions can be a good idea in Python and software language to make a particular structure dynamic. 

class BookShelf:
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    

class Book:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name":"Ashish Chaurasiya", "age": 24},
    {"name":"Ashish", "age":30},
    {"name": "Abhishek", "age": 20},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Bob Smith", get_friend_name))