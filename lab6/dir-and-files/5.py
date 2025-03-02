file_name = 'text.txt'

file = open(f"/Users/Acer/Desktop/pp2_lab/lab6/dir-and-files/{file_name}", "w")

content = str(input("write content: "))

file.write(content)