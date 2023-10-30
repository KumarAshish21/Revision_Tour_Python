# Instance methods

# setter method :- set values of instance variables
# getter method : - get values of instance variables.

# this is called a accessor method

# class Empployee:
#     def setName(self,name): #setter method
#         self.name = name
       
#     def getName(self): #getter method
#         print(f"The name is : {self.name}")
# e1 = Empployee()
# e2 = Empployee()
# e1.setName(input("Enter the name: "))
# print(e1.__dict__)
# e1.getName()

# staticmethod
# Static method which performs operations on external data
# It can also perform operations on class data
# No need to pass object or class reference
# Created using decortor '@staticmethod'

class Bank:
    bank_name = 'BOI'
    rate_of_interest = 12.25
    @staticmethod
    def simple_interest(prin,n):
        si = (prin*n*Bank.rate_of_interest)/100
        print(si)
prin = float(input("Enter principle amount: "))
n = int(input("Enter numbers of years"))
Bank.simple_interest(300000,3)