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
# age = 67

# if age >= 18 and age <= 26 :
#     print("He can vote!")
# elif age > 26 and age <= 60:
#     print("He is old")
# else:
#     print("He can't vote!")

# # PEP 484
# # Type annotations
# name : str = "India"
# age : int = 12
# salary : float = 1277777777.78


# # nums = [
# #     1,2,3,4,5,\
# #     3455,567
# # ]

# #print("Gaurav Arora")
# #print("Gaurav Arora")

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

# yr= int(input("enter the year"))
# if yr %100 ==0:
#     if yr %400 ==0:
#         print("entered year is a leap year")
#     else:
#         print("entered year is not leap year")
# else:
#     if yr % 4 ==0:
#         print("entered year is a leap year")
#     else:
#         print ("entered year is not a leap year")
    
 
# print("hi")

# amt = 0
# nu= int(input("enter numbers pf electric units:"))
# if nu<=100:
#    amt=0
# elif nu <= 200:
#    amt=(nu-100)*5
# else:
#    amt=500+(nu-200)*10
#    print("amount to pay:",amt)


# per= int(input("enter marks"))
# if per > 90:
#     print("grade is a")
# if per<90 and per>80:
#     print("grade is b")
# if per>60 and per<80:
#     print("grade is c")
# if per<60:  
#     print("grade is d")

# a : int = 12


a : int = 'abhi'

# My name is abhi. abhi is an educator at gtec. abhi is teaching us about python.
# print("My name is ", a, ".", a, " is an educatort at getc.", a, " is teaching us about python.")

# print("")
# a=100
# b=500
# print(f"sum:{a+b}")

# F-strings => formatted strings.
# print(f"My name is {a}. {a} is an educator at gtec. {a} is teaching us about python.")

# n = 10

# sum_of_n_nos = n * (n + 1) // 2

# print(f"The sum of {n} natural no.s is {sum_of_n_nos}.")

# raw strings
# print(r"C:\Users\singh")

# a = 5
# b = 2

# # print(a + b) 
# # print(a - b)
# # print(a * b)
# print(a / b) # include decimals 2.5
# # print(a // b) # didn't take decimal value 2

# print(a**b) # 5 to the power 2 = 5 * 5 = 25


# print(a << b)
# print(a >> b)

# 64 32 16 8 4 2 1
# 1 0 1 ->

# 5 << 2


# Walrus operator
if age := int(input("Please provide your age : ")) >= 18:
    print("He can vote")
else:
    print("He can't")