import math

def trapizoid(h, a, b):
    return ((a+b)/2) * h

h, a, b = map(int, input().split())
print(f"S = {trapizoid(h,a,b)}")