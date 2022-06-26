num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))
num3 = int(input("3rd Number: "))

largest = num1

if (num2 >= num1) and (num2 >= num3):
    largest = num2
elif (num3 >= num1) and (num3 >= num2):
    largest = num3
else:
    largest = num1

print(largest)