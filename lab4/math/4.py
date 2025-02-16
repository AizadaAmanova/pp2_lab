import math

def parallelogram(length, height):
    return length * height

length = int(input("Length: "))
height = int(input("Height: "))

print(f"S = {parallelogram(length, height)}")