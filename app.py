# print("gaurav")

# input output operations
# input("message or prompt")
# print("statement", or variable, end='')

# Python Enhancement Proposal 8 (PEP8)
# snake_case => firstname X => first_name `_/
# class StudentDetails
# PI = 3.14
# GRAVITY = 9.8
# : -> next print and 4 spaces or 1 tab (indentation)
age = 67

if age >= 18 and age <= 26 :
    print("He can vote!")
elif age > 26 and age <= 60:
    print("He is old")
else:
    print("He can't vote!")

# PEP 484
# Type annotations
name : str = "India"
age : int = 12
salary : float = 1277777777.78


# nums = [
#     1,2,3,4,5,\
#     3455,567
# ]

#print("Gaurav Arora")
#print("Gaurav Arora")

# num=int(input("enter any number 1 to 7:"))
# if num ==1:
#     print("sunday")
# elif num ==2:
#     print("monday")
# elif num ==3:
#     print("tuesday")
# elif num ==4:
#     print("wednesday")
# elif num ==5:
#     print("thrusday")
# elif num ==6:
#     print("friday")
# elif num ==7:
#     print("saturday")
# else:
#     print("please enter number btw 1 to 7")

yr= int(input("enter the year"))
if yr %100 ==0:
    if yr %400 ==0:
        print("entered year is a leap year")
    else:
        print("entered year is not leap year")
else:
    if yr % 4 ==0:
        print("entered year is a leap year")
    else:
        print ("entered year is not a leap year")
    
 
