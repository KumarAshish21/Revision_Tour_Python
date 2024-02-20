# Singleton Design Pattern in Detail
# Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

# Encapsulation on a method level

class Order:
    def __init__(self, country, line_items):
        self.country = country
        self.line_items = line_items

class LineItem:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

def get_order_total(order):
    total = 0
    for item in order.line_items:
        total += item.price * item.quantity

    total += total * get_tax_rate(order.country)
    return total

def get_tax_rate(country):
    if country == "US":
        return 0.07  # US sales tax
    elif country == "EU":
        return 0.20  # European VAT
    else:
        return 0

# Example usage:
line_items = [LineItem(price=10, quantity=2), LineItem(price=20, quantity=1)]
order = Order(country="US", line_items=line_items)

total_with_tax = get_order_total(order)
print("Total with tax:", total_with_tax)
