class Account:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining Balance: ₹{self.balance}")
        else:
            print(" Insufficient Balance!")

    def check_balance(self):
        print(f"Balance for {self.name}: ₹{self.balance}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, pin, balance=0):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = Account(acc_no, name, pin, balance)
            print(f" Account created successfully for {name}.")

    def authenticate(self, acc_no, pin):
        account = self.accounts.get(acc_no)
        print(f" Account authenticate")


# ---------------- MAIN PROGRAM ----------------
atm = ATM()
acc = Account('123', 'rohit', '1235', 500)

# Pre-created sample accounts (Optional)
acc.check_balance()
acc.withdraw(200)
acc.deposit(500)