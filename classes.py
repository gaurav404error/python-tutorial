# # class Employee:
# #     pass

# # emp = Employee()
# # # e = Employee()

# # # print(emp)
# # # print(e)

# # emp.name = "Chikhu"
# # emp.salary = 89900100100101

# # print(emp.salary)

# class Employee:
#     # Constructor method
#     def __init__(self,fname,lname,dept,salary):
#         self.fname = fname # instance variables
#         self.lname = lname
#         self.dept = dept 
#         self.salary = salary 

#     def fullname(self):
#         return f"{self.fname} {self.lname}"
    
#     def printDetails(self):
#         return f"""
#                 ***************Details*******************
#                 *****************************************
#                 Employee Name : {self.fname} {self.lname}
#                 Department    : {self.dept}
#                 Salary        : {self.salary} per week
#                 *****************************************
#             """


# emp_1 = Employee("Gaurav","Vashishta","Management",200000)
# # print(emp_1.__dict__)


# # print(f"First name : {emp_1.fname}")
# # print(f"Last name : {emp_1.lname}")
# # print(f"Department : {emp_1.dept}")
# # print(f"Salary : {emp_1.salary}")

# # print(emp_1.printDetails())

# print(Employee.printDetails(emp_1))

class Wallet:
    balance = 50000
    rate = 0.2
    cashback = 0

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.cashback += amount * self.rate
        else:
            print("Insufficient Balance!")
    
    def view(self):
        return f"""
    ************Wallet****************
    * Available Bal : {self.balance}
    * Cashback  Bal : {self.cashback}
    **********************************
    """

c = Wallet()

c.withdraw(5000)

print(c.view())
