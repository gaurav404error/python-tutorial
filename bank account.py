# class Bank_Account:
#     def __init__(self):
#         self.balance=0
    
#     def deposit(self,amount):
#         self.balance+=amount
#         print ("Amount added successfully!")

#     def withdraw (self,amount_to_withdraw):
#         if self.balance>=amount_to_withdraw:
#             self.balance -= amount_to_withdraw
#             print(f"amount withdrawn successfully!")
#         else:
#             print("insufficient funds!")

#         def check_balance(self):
#             print(f"Account balance: {self.balance}")
        
# bank = Bank_Account()
# bank.deposit(20000)

# bank.check_balance()

# bank.withdraw(5000)
# bank.check_balance()




class BankAccount:
    def _init_(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount added successfully!")

    def withdraw(self, amount_to_withdraw):
        if self.balance >= amount_to_withdraw:
            self.balance -= amount_to_withdraw
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


# Usage
bank = BankAccount()
bank.deposit(20000)
bank.check_balance()
bank.withdraw(5000)
bank.check_balance()