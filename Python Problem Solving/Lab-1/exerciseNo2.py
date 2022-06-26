#Write a Python program to find the area and perimeter of a circle. Read inputs from the user.
import math
def area_of_circle(r):
    pi = math.pi
    area = pi * (r**2)
    return area

def perimeter_of_circle(r):
    pi = math.pi
    perimeter = 2 * pi * r
    return perimeter

user_input = float(input("Enter radius of a circle :"))
result1 = area_of_circle(user_input)
print(f"Area of a circle is {round(result1,2)}")
result2 = perimeter_of_circle(user_input)
print(f"Perimeter of a circle is {round(result2,2)}")