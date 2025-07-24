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

score = int(input("Enter the score of maths: "))

match score:
    case s if score <= 100 and score > 80:
        print("A")
    
    case s if score <= 80 and score > 70:
        print("B")
    
    case s if score <= 70 and score > 50:
        print("C")
    
    case _:
        print("Give donation to pass!")















