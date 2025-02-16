import math 

def generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("n: "))
print(", ". join(map(str, generator(n))))