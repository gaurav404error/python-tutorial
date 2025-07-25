# choice = int(input("Enter between 1 to 10: "))

# match choice:
#     case 1: 
#         print("Today is monday!")
#     case 2: 
#         print("Today is tuesday!")
#     case 3: 
#         print("Today is wednesday!")
#     case 4: 
#         print("Today is thrusday!")
#     case 5: 
#         print("Today is friday!")
#     case 6: 
#         print("Today is saturday!")
#     case 7: 
#         print("Today is sunday!")
#     case _:
#         print("Invalid choice!")

# If the choices are even, print namaskaram else if the choices are odd, jai shree ram. Default, wrong choice!

# choice = 1

# match choice:
#     case 1 | 3 | 5 | 7 | 9:
#         print("Jai Shree Ram")
#     case 2 | 4 | 6 | 8 | 10:
#         print("Namaskaram")
#     case _:
#         print("Wrong choice!")

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4:
#     print("A weekday in April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")

# day = 6
# choice = int(input("Enter between 1 to 7: "))
# match choice:
#     case 1: print("Monday")
#     case 2: print("Tuesday")
#     case 3: print("Wednesday")
#     case 4: print("Thursday")
#     case 5: print("Friday")
#     case 6: print("Saturday")
#     case 7: print("Sunday")
#     case _: print("Invalid")

# num = 4
# choice=int(input("enter number 1 to 5:"))
# match choice:
#     case 1: print(1**2)
#     case 2: print(2**2)
#     case 3: print(3**2)
#     case 4: print(4**2)
#     case 5: print(5**2)
#     case _: print("invalid number")

# choice=int(input("enter 1 or 2"))
# match choice:
#     # num = 2
#     case 1: print("One")
#     case 2: print("Two")
#     case _: print("Other number")


# fruit = input("enter your fruit name")
# match fruit:
#     case "apple": print("Red")
#     case "banana": print("Yellow")
#     case "grape": print("Green")
#     case _: print("Unknown fruit")


# char = input("enter your char")
# match char:
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print("Vowel")
#     case _:
#         print("Consonant")

# response = input("enter your response")
# match response:
#     case "yes": print("Accepted")
#     case "no": print("Declined")
#     case _: print("Invalid response")


# num = int(input("enter your number"))
# match num:
#     case 2 | 4 | 6 | 8 | 10: print("Even")
#     case 1 | 3 | 5 | 7 | 9: print("Odd")
#     case _: print("Invalid")


# choice= int(input("enter your number"))
# match choice:
#     case _ if choice > 0:
#         print("Positive")
#     case _ if choice < 0:
#         print("Negative")
#     case _ if choice==0:
#         print("Zero")


# choice = int(input("Enter between 1 to 7: "))

# match choice:
#     case 1: 
#         print("Today is monday!")
#     case 2: 
#         print("Today is tuesday!")
#     case 3: 
#         print("Today is wednesday!")
#     case 4: 
#         print("Today is thrusday!")
#     case 5: 
#         print("Today is friday!")
#     case 6: 
#         print("Today is saturday!")
#     case 7: 
#         print("Today is sunday!")
#     case _:
#         print("Invalid choice!")


# choice=7

# match choice:
#     case 1 | 3 | 5 | 7 | 9:
#         print("Jai Shree Ram")
#     case 2 | 4 | 6 | 8 | 10:
#         print("Namaskaram")
#     case _:
#         print("Wrong choice!")

# Grade Check
# score = int(input("Enter the score of maths: "))

# match score:
#     case s if score <= 100 and score > 80:
#         print("A")
    
#     case s if score <= 80 and score > 70:
#         print("B")
    
#     case s if score <= 70 and score > 50:
#         print("C")
    
#     case _:
#         print("Give donation to pass!")



# signal = "red"
# match signal:
#     case "red": print("Stop")
#     case "green": print("Go")
#     case "yellow": print("Wait")
#     case _: print("Invalid color")


# day = 6
# match day:
#     case 6 | 7:
#         print("Weekend")
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")



# day, month = 15, 8
# match (day, month):
#     case (15, 8): print("Independence Day")
#     case (26, 1): print("Republic Day")
#     case _: print("Not a holiday")



# result = "pass"
# match result:
#     case "pass": print("Congratulations!")
#     case "fail": print("Try again")


# n = 15
# match n:
#     case x if x % 3 == 0 and x % 5 == 0: print("Divisible by 3 and 5")
#     case x if x % 3 == 0: print("Divisible by 3")
#     case x if x % 5 == 0: print("Divisible by 5")
#     case _: print("Not divisible")



# temp = 30
# match temp:
#     case t if t < 20: print("Cold")
#     case t if 20 <= t <= 35: print("Warm")
#     case _: print("Hot")



# animal = "snake"
# match animal:
#     case "dog" | "cat": print("Mammal")
#     case "parrot": print("Bird")
#     case "snake": print("Reptile")
#     case _: print("Unknown")


# n = 7
# match n:
#     case 2 | 3 | 5 | 7: print("Prime")
#     case 1: print("Neither Prime nor Composite")
#     case _: print("Composite")



# day, month = 25, 12
# match (day, month):
#     case (25, 12): print("Christmas")
#     case (14, 1): print("Makar Sankranti")
#     case _: print("No major festival")



# age, gender = 25, "male"
# match (age, gender):
#     case (a, "male") if a < 18: print("Boy")
#     case (a, "female") if a < 18: print("Girl")
#     case (a, "male") if a >= 18: print("Man")
#     case (a, "female") if a >= 18: print("Woman")



# marks, subject = 65, "math"
# match subject:
#     case "math" if marks >= 40: print("Pass in Math")
#     case "science" if marks >= 35: print("Pass in Science")
#     case _: print("Fail")



# word = "Amazing"
# match word:
#     case w if w.startswith("A") and len(w) > 5:
#         print("Starts with A and is long")
#     case _: print("Doesn't match")




# emp_type, salary = "permanent", 30000
# match emp_type:
#     case "permanent" if salary > 25000: print("Bonus: ₹5000")
#     case "contract" if salary > 20000: print("Bonus: ₹2000")
#     case _: print("No bonus")




# hour = 14
# match hour:
#     case h if 5 <= h < 12: print("Good Morning")
#     case h if 12 <= h < 17: print("Good Afternoon")
#     case h if 17 <= h < 21: print("Good Evening")
#     case _: print("Good Night")





# a, b = 4, 6
# match (a % 2, b % 2):
#     case (0, 0): print("Both even")
#     case (1, 1): print("Both odd")
#     case _: print("One even, one odd")




# year = 2024
# match year:
#     case y if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         print("Leap Year")
#     case _: print("Not Leap Year")




# day, month = 19, 2
# match (day, month):
#     case (d, 1) if d >= 20 or (month == 2 and d <= 18):
#         print("Aquarius")
#     case _: print("Other Sign")


















