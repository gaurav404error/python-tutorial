class Employee:
    def __init__(self, name,salary):
     self.name= name
     self.salary= salary

    def increasment(self,amount):
        self.salary+=amount
        print(f"New salary of {self.name}is {self.salary}")

emp1= Employee("abhishek",10000)
emp1.increasment(5000)

