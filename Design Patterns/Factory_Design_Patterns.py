"""
The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
The Factory Method is a creational design pattern in software engineering that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
In Other words, it defines an interface for creating an object, but delegates the actual instantiation to subclasses.

Factory Method pattern typically works:
1. A client asks a factory object to create a product.
2. The factory instantiates a concrete product class and returns
Define an interface (or abstract class) that declares a method for creating objects. This method acts as the "factory" for creating instances of a class.
Subclasses of the interface (or abstract class) implement this factory method to create objects of a specific type.
Clients of the pattern call the factory method to create instances of the desired class being instantiated.

The Factory Method pattern promotes loose coupling between the creator (the code that uses the factory method)
and the concrete products (the objects being created), allowing for easier maintenance and scalability of the code.

@abstractmethod decoratoe is a Python build-in decorator that is used to define abstract methods within abstract base classes(ABCs).
Abstract methods are methods declared in the base class but are meant to be implemented by subclasses.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.
Here's a breakdown of how @abstractmethod works:

Purpose: It marks a method in an abstract base class (ABC) as abstract, indicating that the method must be implemented by concrete subclasses. Abstract methods serve as placeholders in the base class, defining the interface that subclasses must adhere to.
Usage: The @abstractmethod decorator is placed above the method definition in the abstract base class to indicate that it is an abstract method. This decorator can only be used in ABCs and cannot be instantiated directly.
Enforcement: If a subclass of an abstract base class fails to implement all the abstract methods defined in the base class, attempting to instantiate the subclass will raise a TypeError indicating that the subclass is still abstract and cannot be instantiated.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        return "Inside Square::draw() method."

class Triangle(Shape):
    def draw(self):
        return "Inside Triangle::draw() method."

class ShapeFactory:
    def get_shape_instance(self, shape_type):
        if shape_type == "Rectangle":
            return Rectangle()
        elif shape_type == "Square":
            return Square()
        elif shape_type == "Triangle":
            return Triangle()
        return None

class Driver:

    def __init__(self):
        self.shape_factory = ShapeFactory()

    def draw_shape(self, shape_type):
        shape_instance = self.shape_factory.get_shape_instance(shape_type)
        if shape_instance:
            return shape_instance.draw()
        else:
            return "Invaild shape type specified."

if __name__ == "__main__":
    driver = Driver()
    print(driver.draw_shape("Rectangle"))
    print(driver.draw_shape("Square"))
    print(driver.draw_shape("Triangle"))
    print(driver.draw_shape("Circle"))


