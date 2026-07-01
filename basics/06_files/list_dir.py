import os

print("Current working directory:", os.getcwd())

files = os.listdir(".")
print(files) # current working dir

files = os.listdir("./challenges")
#print(files)

files = os.listdir("./basics/05_OOP/cart")
#print(files)

files = os.listdir("../challenges")
print(files)