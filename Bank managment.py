class Account:
    rate = 1.04
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, acc_no, name, balance=0):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = Account(acc_no, name, balance)
            print(f"Account created for {name} with A/C No: {acc_no}")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)



bank = Bank("State Bank of BIHAR")

# Create Accounts
bank.create_account(101, "gaurav", 5000)
bank.create_account(102, "shivam", 3000)

# Transactions
acc1 = bank.get_account(101)
acc1.deposit(20000)
acc1.withdraw(15000)
acc1.check_balance()

acc2 = bank.get_account(102)
acc2.withdraw(5000) 

