import math
def radian(degree):
    return degree * (math.pi / 180)

degree = float(input())
print(f"Degree to radian {radian(degree)}")