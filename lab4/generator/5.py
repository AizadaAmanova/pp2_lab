
n = int(input("n = "))

def generator(n):
    while n>=0:
        yield n
        n-=1
    
for i in generator(n):
    print(i)