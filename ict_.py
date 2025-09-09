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


# basket ={
#     "fruit": "apple",
#     "quantity": "ten",
#     "quality": "good"

# }

# print(basket["fruit"])
# basket['fruit']= "mango"
# print(basket)

# basket ["price"]= "fifty" 
# print(basket)

# del basket ['price']
# print(basket)
# print(basket.get("production"))
# print(basket.get("production","not available")) 

# # my_dict = {}

# # student ={

# # }

# # items()
# print(basket.items())

# # keys()
# print(basket.keys())

# # values()
# print(basket.values())


# my_dict={i:i**2 for  i in range (1,11)}
# print("assignment 1 dictionary:", my_dict)

# print("value of key 5:",my_dict[5])
# print("keys of dictionary:",list(my_dict.keys()))

# my_dict[11]=121
# print ("after adding (11,121):",my_dict)
# my_dict.pop(1)
# print("after removing key 1:",my_dict)

# for index, value in my_dict.items():
#     print(f"{index}:{value}")

# cube_dict = {i:i**3 for i in  range(1,11)}
# print("cubes dictionary:",cube_dict)

# data = {
#   {'Name' : 'Abhi', 'Age' : 25, 'Country' : 'Japan'},
#   {'Name' : 'Alya', 'Age' : 17, 'Country' : 'Japan'},
#   {'Name' : 'Vaani', 'Age' : 25, 'Country' : 'India'}
# }


# student = {
#     "name": "gaurav",
#     "age": 18,
#     "grades":{
#         "math": 46,
#         "physics": 83,
#         "chemistry": 79,
#         "english":90
#     }
# }
# print(student)


# d= {i:[i*j for j in range (1,6)]for i in range (1,6)}
# print(d) 


#Dictionary of Tuples.
#key= first 5 positive integers.
# Values - tuple containing (key,key^2)
# d= {i:(i,i**2)for i in range(1,6)}
# print(d)

# # Dictionary and list conversion.
# # Dictionary with first 5 positive integers and their squares.
# d = {i:i**2 for i in range (1,8)}
# #convert dictionary to a list of tuples.
# lst=list(d.items())
# print (lst)




# #Dictionary Filtering
# # First 10 positive integers and their squares
# d={i:i**2 for i in range (1,13)}
# #Keep only even keys
# filtered_d = {k:v for k,v in d.items()if k%2 ==0}
# print(filtered_d)




