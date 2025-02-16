import math

def generator(a,b):
    for i in range(a,b+1):
        yield i**2

a = int(input("a = "))
b = int(input("b = "))

for square in generator(a,b):
    print(square, end = " ")