import os

# os.getcwd() -> current working directory
# print(os.getcwd())

# os.chdir() -> change the directory(folder)

path = "C:\\Users\\singh"
os.chdir(path)
print(os.getcwd())

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



import os     

# os.mkdir("demo")
with open ("demo/hello.txt", "w")as f:
    f.write ("hello world")

base_path = os.getcwd()
folder_path = base_path + "\\demo"
file_path = folder_path + "\\hello.txt"

print(path)


# print ("After creating folder & file:", os.listdir())

# print(os.getcwd())
os.remove(file_path)
os.rmdir(folder_path)
# print("After removing file & folder:", os.listdir)
