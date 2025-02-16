import math

def polygon(side, length):
    return (side * length**2) / (4 * math.tan(math.pi / side)) 

side = int(input("Side: "))
length = int(input("Length: "))
print(f"Area of a trapezoid {polygon(side, length)}")