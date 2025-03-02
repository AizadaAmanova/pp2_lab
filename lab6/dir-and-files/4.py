file_name = 'test.txt'

file = open(f"/Users/Acer/Desktop/pp2_lab/lab6/dir-and-files/{file_name}")

sum = 0 

for line in file:
    sum+=1
print(sum)