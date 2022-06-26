def calculation_lcm(x,y):
    lcm = max(x,y)
    while lcm % x != 0 or lcm % y != 0:
        lcm = lcm + 1
    return lcm

num1 = int(input("1st Number : "))
num2 = int(input("2nd Number : "))
lcm = calculation_lcm(num1,num2)

print(f"LCM of {num1} and {num2} is: {lcm}")