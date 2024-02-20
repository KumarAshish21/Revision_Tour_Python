# S -> Single Responsibility Principle (A class should have only one reason to change).
# O -> Open/Closed Principle (Software entities should be open for extension, but closed for modification).
# L -> Liskov Substitution Principle (Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program).
# I -> Interface Segregation Principle (A client should never be forced to implement an interface that it doesn’t use or clients shouldn’t be forced to depend on methods they do not use).
# D -> Dependency Inversion Principle (Entities must depend on abstractions, not on concretions).

# Example of Single Responsibility Principle
"""
The Employee class has several reasons to change. The first
reason might be related to the main job of the class: managing
employee data. However, there’s another reason: the format of
the timesheet report may change over time, requiring you to
change the code within the class.

Solve the problem by moving the behavior related to printing
timesheet reports into a separate class. This change lets you
move other report-related stuff to the new class.
"""
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def generate_timesheet_report(self):
        return "TimeSheet Report"

class TimeSheetReport:
    @staticmethod
    def print(employee):
        return f"TimeSheet Report for {employee.name}"

employee = Employee("Ashish", 1)
print(TimeSheetReport.print(employee))

"""
@staticmethod indicates that the print method is associated with the TimeSheetReport
class as a whole rather than with instances of the class. It can be called on the
class itself without needing to create an instance of TimeSheetReport
The Employee class is responsible for managing employee data.
The TimesheetReporter class is responsible for generating timesheet reports.
The generate_timesheet_report method in the TimesheetReporter class takes an
employee object as an argument and generates the timesheet report for that employee.
This separation of concerns adheres to the Single Responsibility Principle (SRP),
as each class has a single responsibility and a single reason to change.
"""

# Example of Open/Closed Principle

"""
User
Example of Open/Closed Principle
You have an e-commerce application with an Order class that
calculates shipping costs and all shipping methods are hardcoded
inside the class. If you need to add a new shipping
method, you have to change the code of the Order class and risk breaking it.

You can solve the problem by applying the Strategy pattern. Start
by extracting shipping methods into separate classes with a common interface.

We define three concrete shipping strategy classes: StandardShipping, ExpressShipping, and FreeShipping, each implementing the calculate_shipping_cost method according to its own algorithm.
The Order class allows setting a shipping method dynamically using the set_shipping_method method.
The calculate_shipping_cost method in the Order class delegates the calculation to the chosen shipping strategy object.
We create an Order object with a total price and demonstrate calculating shipping costs using different shipping methods.
"""

class Order:
    def __init__(self,total_price):
        self.total_price = total_price

    def calculate_shipping_cost(self,method):
        if method == "standard":
            return self.total_price * 0.05
        elif method == "express":
            return self.total_price * 0.1
        elif method == "free":
            return 0
        else:
            raise ValueError("Invalid shipping method")

class ShippingStrategy:
    def calculate_shipping_cost(self,total_price):
        pass

class StandardShipping(ShippingStrategy):
    def calculate_shipping_cost(self,total_price):
        return total_price * 0.05

class ExpressShipping(ShippingStrategy):
    def calculate_shipping_cost(self,total_price):
        return total_price * 0.1
class FreeShipping(ShippingStrategy):
    def calculate_shipping_cost(self,total_price):
        return 0

class Order:
    def __init__(self,total_price):
        self.total_price = total_price

    def set_shipping_method(self,strategy):
        self.shipping_strategy = strategy

    def calculate_shipping_cost(self):
        return self.shipping_strategy.calculate_shipping_cost(self.total_price)

order = Order(100)
order.set_shipping_method(FreeShipping())
print(order.calculate_shipping_cost())
print(order.set_shipping_method(ExpressShipping()))
print(order.calculate_shipping_cost())


# Example of Liskov Substitution Principle (When extending a class, remember that you should be
"""
Quetions: Let’s look at an example of a hierarchy of document classes
that violates the substitution principle.
BEFORE: saving doesn’t make sense in a read-only document, so the
subclass tries to solve it by resetting the base behavior in the
overridden method. This is a violation of the Liskov Substitution
The save method in the ReadOnlyDocuments subclass throws an exception
if someone tries to call it. The base method doesn’t have this restriction.
This means that the client code will break if we don’t check the document type
before saving it. The resulting code also violates the open/closed principle,
since the client code becomes dependent on concrete classes of documents. If you
introduce a new document subclass, you’ll need to change the client code to support it.
"""

class ReadOnlyDocument:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

    def save(self, filepath):
        raise NotImplementedError("Can't save read-only document")

class WriteableDocument(ReadOnlyDocument):
    def __init__(self, content):
        super().__init__(content)

    def save(self, filepath):
        with open(filepath, 'w') as file:
            file.write(self.content)

# Create a read-only document
read_only_doc = ReadOnlyDocument("This is read-only content. ")
print(read_only_doc.read())

try:
    read_only_doc.save("read_only.txt")
except NotImplementedError as e:
    print("Saving not supported for read-only documents", e)

# Create a writeable document
writeable_doc = WriteableDocument("This is writeable content. ")

writeable_doc.save("writeable.txt")

print("Content saved Successfully")

"""
Explanation:

The ReadOnlyDocument class represents a read-only document with methods for reading the content and attempting to save it, which raises a NotImplementedError.
The WriteableDocument class inherits from ReadOnlyDocument and overrides the save method to actually save the content to a file specified by filepath.
Instances of ReadOnlyDocument and WriteableDocument are created and their methods are called accordingly.
When attempting to save the read-only document, a NotImplementedError is raised, which is caught and handled appropriately.
The writeable document is saved successfully to a file named "writeable.txt".
"""

# Example of Interface Segregation Principle

# Example of Dependency Inversion Principle

