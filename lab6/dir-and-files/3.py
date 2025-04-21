import os

path = input("Enter a file or directory path: ")

if os.path.exists(path):
    print("The path exists!")
    directory, filename = os.path.split(path)  
    print("Directory:", directory)
    print("Filename:", filename if filename else "This is a directory")
else:
    print("The specified path does not exist!")
