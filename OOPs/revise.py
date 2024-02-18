# OOPs:

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def chai_brand(self):
        return self.__brand + " "

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery,size):
        super().__init__(brand, model)
        self.battery = battery
        self.size = size


my_tesla = ElectricCar('Tesla', 'Model S', '100kw', 'large')
# print(my_tesla.full_name())
print(my_tesla.chai_brand())
# print(my_tesla.__brand())

# my_car = Car('Audi', 'A4')
# print(my_car.brand)
# print(my_car.full_name())

