import math

a = float(input("1st side: "))
b = float(input("2nd side: "))
c = float(input("3rd side: "))

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of your triangle is ",round(area,5))