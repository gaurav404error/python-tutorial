# names = {}
names = dict()
# print(type(names))

# "name" : "gaurav"
# "name" : "gauri"


# student = {
#     "name" : "Gaurav",
#     "age" : 18,
#     "grade" : "A+"
# }

# print(student["name"])

# # get()

# print(student.get("score")) # None
# # print(student.get("score","not available"))

# student['name'] = "Shrey"

# print(student)

# student["address"] = "Navada"

# print(student)

# del student['age']
# print(student)


basket ={
    "fruit": "apple",
    "quantity": "ten",
    "quality": "good"

}

print(basket["fruit"])
basket['fruit']= "mango"
print(basket)

basket ["price"]= "fifty" 
print(basket)

del basket ['price']
print(basket)
print(basket.get("production"))
print(basket.get("production","not available")) 

# my_dict = {}

# student ={

# }

# items()
print(basket.items())

# keys()
print(basket.keys())

# values()
print(basket.values())