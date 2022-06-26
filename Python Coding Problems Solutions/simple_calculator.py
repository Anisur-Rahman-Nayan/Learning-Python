def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def modulo(num1,num2):
    return num1%num2
def divide(num1,num2):
    return num1/num2

num1 = int(input("Enter 1st Number: "))
operation =input("Enter you want to do + ,- ,*, /, % : " )
num2 = int(input("Enter 2nd Number: "))
result = 0

if operation =='+':
    result = add(num1,num2)
elif operation =='-':
    result = sub(num1,num2)
elif operation =='*':
    result = multiply(num1,num2)
elif operation =='/':
    result = divide(num1,num2)
elif operation =='%':
    result = modulo(num1,num2)
else:
    print("please Enter you want to do + ,- ,*, /, : ")

print(num1 , operation , num2, '=' , result)