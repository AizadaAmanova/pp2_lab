import string 

for letter in string.ascii_uppercase: 
    file_name = f"{letter}.txt"
    with open(file_name, "w") as file:
        file.write(f"This is file {file_name}")  

print("Файлы A.txt - Z.txt созданы!")