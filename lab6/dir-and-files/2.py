import os
path = str(input("Enter the directory path: "))
print(os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))  
print("Writable:", os.access(path, os.W_OK)) 
print("Executable:", os.access(path, os.X_OK))


