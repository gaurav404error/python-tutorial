class student:
    def __init__(self,name,age,percentage):
        self.name= name
        self.age= age
        self.percentage= percentage
    
    def printdetails(self):
        print(f"Name:{self.name}")
        print(f"Age :{self.age}")
        print(f"Percentage: {self.percentage}")

a = student("gaurav singh vashistha",18,60)
a.printdetails()

b = student("Manya Surve", 27, 89)
b.printdetails()