#2
def temperature(fahrenheit):
    return (5/9)*(fahrenheit-32) 

fahrenheit=float(input())
celsius=temperature(fahrenheit)
print(f"Equivalent temperature in Celsius: {celsius:.2f}")
