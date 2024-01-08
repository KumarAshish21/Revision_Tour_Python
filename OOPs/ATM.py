class Atm:
    
    # Constructor
    # special/magic/dunder methods
    # jis object ke sath currentlly kaam kar rahe hote ho to vahi self hota hai
    # Class is represent data and methods. access only us class ka method hi kar sakta hai. if I have to access then create object then access.
    # Class apne methods se doosre methods se bhi access nahi kar sakta hai uske liye self ke through object access karte hai
    
    
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
    
    def menu(self):
        user_input = input('''
                           Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           ''')
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
            
        elif user_input == "3":
            self.withdraw()
            
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")
            
            
    def create_pin(self):
        self.pin = input("Enter your pin ")
        print("Pin set successfully")
        
        
    def deposit(self):
        temp =  input('Enter your pin ')
        if temp == self.pin:
            amount = int(input('Enter the amount '))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invaild Pin")
            
            
    def withdraw(self):
        temp = input("Enter your pin ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successful")
                
            else:
                print("Insufficient funds")
                
        else:
            print("Invaild pin")
            
            
    def check_balance(self):
        temp = input("Enter your balance ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invaild pin")
            
sbi = Atm()
print(sbi)