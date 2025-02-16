import math

def generator(n):
    for i in range(n+1):
        yield i**2
    
n = int(input())
for square in generator(n):
    print(square, end = ' ')
