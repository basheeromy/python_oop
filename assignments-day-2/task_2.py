# Create a class called BankAccount with a constructor that 
# initializes the balance instance variable. Add methods called 
# deposit and withdraw that modify the balance. Add a method 
# called get_balance that returns the current balance.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    def deposite(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount
        
    def get_balance(self):
        print(f"Available balance : {self.balance}")
        

savings = BankAccount(500000)
savings.deposite(50000)
savings.withdraw(20000)
savings.get_balance()
