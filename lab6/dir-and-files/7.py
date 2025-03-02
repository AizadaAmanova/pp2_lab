file = input("Enter the source file path: ")
new_file = input("Enter the destination file path: ")

try:
    with open(file, "r") as abc:
        content = abc.read() 
    
    with open(new_file, "w") as dst:
        dst.write(content)  
    
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found!")
