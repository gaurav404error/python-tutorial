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
# if age := int(input("Please provide your age : ")) >= 18:
#     print("He can vote")
# else:
#     print("He can't")


    
    #     if len(password) < 8:
    #         return False
    #     if not re.search(r'[A-Z]', password):  
    #         return False
    #     if not re.search(r'[a-z]', password):  
    #         return False
    #     if not re.search(r'\d', password):    
    #         return False
    #     if not re.search(r'[@#$%^&*()\-_+=\[\]{}|:;"\'<>,.?/]', password):  # Special char
    #         return False
    #     if "password" in password.lower():     
    #         return False
    #     return True


#     a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number is", a)
# elif b >= c:
#     print("Largest number is", b)
# else:
#     print("Largest number is", c)

# a=int(input("side a:"))
# b=int(input("side b:"))
# c=int(input("side c:"))
# if a+b>c and b+c>a and b+c>a and a+c>b:
#     if a== b ==c:
#         print ("equilateral triangle")
#     elif a==b or b==c or a==c:
#        print("ispsceles triangle")
#     else:
#         print("scalene triangle")
# else:
#     print("not a triangle")

# temp= float(input("enter temprature in celsius"))
# if temp<0:
#    print("freezing")
# elif temp<=10:
#    print("very cold")
# elif temp<20:
#    print("cold")
# elif temp<30:
#    print("warm")
# elif temp<40:
#    print(" hot")
# else:
#    print("stay at home")
   

# age=int(input("enter your age"))
# if age<0:
#     print ("invalid age")
# elif age <=12:
#     print("child")
# elif age <19:
#     print("teen")
# elif age<59:
#     print("adult")
# else:
#     print("senior citizen")
        
# for i in range(10):
#     if i ==5:
#         print(i)

# for i in range (1,11):
#     print(f"15*{i}={15*i}")

# total=0
# for i in range (1,101):
#     total += i
#     print("sum:",total)




# for i in range (3,51,3):
#     print(i)

# text="hello world"
# vowels='aeiouAEIOU'
# count=0
# for char in text:
#     if char in vowels:
#         count +=1
# print ("vowels count:,count")


# num=int(input("enter a number:"))
# factorial=1

# if num<0:
#     print("factorial does not exist for negative numbers.")
# elif num ==0:
#     print("factorial of 0 is 1.")
# else:
#     for i in range (i, num+ 1):
#         factorial *=i
#     print(f"the factorial of num {num}is {factorial}.")

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


     #TEST

# yr= int(input("enter the year"))
# if yr % 4 ==0:
#     if yr %100 ==0:
#         if yr %400 ==0:
#             print("entered year is a leap year")
#         else:
#             print("entered year is not leap year")
#     else:
#         print("entered year is a leap year")
# else:
#     print ("entered year is not a leap year")


# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
            
#     else:
#         print("prime")



# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit: ",fahrenheit)
    
     


# word = input("Enter a word: ")
# reversed_word = word[::-1]
# print("Reversed word:", reversed_word)
