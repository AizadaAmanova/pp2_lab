import os

file_path = input("Enter the file: ")

if os.path.exists(file_path): 
    if os.access(file_path, os.W_OK): 
        os.remove(file_path) 
        print("File deleted successfully!")
    else:
        print("No permission to delete the file!")
else:
    print("File does not exist!")
