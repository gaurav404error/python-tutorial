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

i = 1
while i <= 10:
    print("Hello, How are you? I am Gaurav Singh Vashistha!")
    i = i + 5