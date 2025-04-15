lst = list(map(int, input().split(' ')))
# print(lst)

filename = 'file.txt'

# with open(filename, "w") as file:
#     file.write(str(lst))

with open(filename, 'r') as file:
    contents = file.read() [-1,1] 
    # print(contents)