# Iterating some lines of code or steps
# for each 
# for loop - range() or while - conditions
# blank => for _ in range(5)

# n = int(input("Enter the number of times loop should run: "))

# sum_of_numbers = 0 

# for _ in range(n):
#     n = int(input("Enter the number of elements: "))
#     for _ in range(n):
#         element = int(input("Enter a number: "))
#         sum_of_numbers += element

#     print(f"Sum of number: {sum_of_numbers}")

# n = int(input("Enter the number of elements: "))
# for _ in range(n):
#     element = int(input("Enter a number: "))
#     sum_of_numbers += element

# print(f"Sum of number: {sum_of_numbers}")


# print("  *   ")
# print(" ***  ")
# print("***** ")
# print("*******")

# for each loop

# names = ["Abhi", "Gauri", "Shreya", "Ansu"]

# # for name in names:
# #     print(name)


# # print(len(names)) # 4


# # for loop

# for i in range(len(names)): # range(4) - 0, 1, 2, 3
#     print(f"Index {i} : {names[i]}")

# range(100) : default start point = 0 till 99
# range(start, end) => start=1, end=4-1 : 1, 2, 3
# range(start, end, step) => start = 10, end = 20 - 1, step = 3: 10, 13, 16, 19

# Manually Interrupt : ctrl + c
# while True:
#     print("Gaurav Singh")

# i = 1
# while i <= 10:
#     print("Hello, How are you? I am Gaurav Singh Vashistha!")
#     i = i + 5


# print(ord("A")) # A - 65

# print(chr(107))




# for i in range(1, 11):
#     print(i)


# for char in "Python":
#     print(char)


# i = 2
# while i <= 20:
#     print(i)
#     i += 2


# i = 10
# while i >= 1:
#     print(i)
#     i -= 1



# for i in range(1, 6):
#     print(i ** 2)


# for _ in range(5):
#     print("Hello")

# for _ in range(7):
#     print("gaurav singh vashistha")



# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# fruits= ["mango","strawberry","lichi"]
# for name in fruits:
#     print(name)



# total = 0
# for i in range(1, 101):
#     total += i
# print(total)


# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)


# for i in range (1,91):
#     if i % 9 ==0:
#         print(i)


# countt=0
# i=5
# while i>0:
#     countt+=1
#     i-=1
# print(countt)
# print("liftoff") 



# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")


# for i in range(1, 5):
#     print("*" * i)


# for i in range(1, 4):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print("-----")


# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)



# text = "gaurav"
# for char in text:
#     if char == 'e':
#         break
#     print(char)



# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd")


# while True:
#     user_input = input("Enter something (type 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         break
 