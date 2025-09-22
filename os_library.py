import os
from dotenv import load_dotenv

# os.getcwd() -> current working directory
# print(os.getcwd())

# os.chdir() -> change the directory(folder)

# path = "C:\\Users\\singh"
# os.chdir(path)
# print(os.getcwd())

# LIST ALL THE SUB-FOLDERS IN MY MAIN FOLDER (Include all folders, files, etc.)
# print(os.listdir())

# FOLDER BANANA HAI
# os.mkdir('test')
# print(os.listdir())

# FOLDER KA NAAM CHANGE KRNA HAI
# os.rename('test','gauri')
# print(os.listdir())

# FOLDER KO REMOVE KRNA
# rmdir() -> remove a folder
# os.rmdir('gauri')

# # remove() -> remove a file
# # os.remove('filename.extension')
# print(os.listdir())

# os.makedirs("test/hello")

# for dirpath, dirname, filenames in os.walk("C:\\Users\\singh\\OneDrive\\Desktop\\New folder"):
#     print(dirpath)
#     print(dirname)
#     print(filenames)


# Change directory

# import os

# os.chdir("c:\\users\\singh\\documents")

# print("current working directory:",os.getcwd())


# # create folder

# import os
# os.mkdir("practice")
# print("After creating 'practice':", os.listdir())

# # Rename folder
# os.rename("practice", "python_practice")
# print("After renaming to 'python_practice':", os.listdir())



# import os     

# # os.mkdir("demo")
# with open ("demo/hello.txt", "w")as f:
#     f.write ("hello world")

# base_path = os.getcwd()
# folder_path = base_path + "\\demo"
# file_path = folder_path + "\\hello.txt"

# print(path)


# # print ("After creating folder & file:", os.listdir())

# # print(os.getcwd())
# os.remove(file_path)
# os.rmdir(folder_path)
# # print("After removing file & folder:", os.listdir)

# print (path)

# print(os.getcwd())
# os.remove(file_path)
# os.rmdir(folder_path)
# print("after removing file & folder:",os.listdir)

# print(os.path)
# os.path.join()
# print(os.path.exists("test"))

# print(os.path.isfile(path))

# print(os.path.isdir(path))
# os.path.split()

path = "/home/user/documents/admit_card.pdf"

# head, tail = os.path.split(path)

# head will hold the folder path location
# tail will hold the file name. 
# print(head)
# print(tail)

# just do this
# load_dotenv()

# secret = os.environ.get("MY_SECRET")

# print(secret)
# if secret:
#     print("Logged in!")
# else:
#     print("Not provide the correct secret!")
# import time 

# stats = os.stat("test")
# mod_time = time.ctime(stats.st_mtime)
# print(mod_time)

# path, extension = os.path.splitext(path)
# print(path)
# print(extension)

# path = "C:\\Users\\singh\\OneDrive\\Desktop\\New folder"
# os.chdir(path)

# folder_path = "python"

# file_path = os.path.join(path,folder_path,"app.py")
# # print(file_path)

# os.makedirs(folder_path, exist_ok=True)

# with open(file_path, "a") as file:
#     file.writelines("""
#             arr=list(range(1000))
#             def linear_search(a,x):
#                 for i in range(len(a)):
#                     if x==a[i]:
#                         return i
#                 return-1
#         """)
# file_path(os.path.join)