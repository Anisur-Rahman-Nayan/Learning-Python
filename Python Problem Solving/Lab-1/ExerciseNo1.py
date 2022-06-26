'''Given two integer numbers, write a Python program to return their product. If the product is greater
than 1000, then return their sum. Read inputs from the user.'''

def product(number1,number2):
    result = number1 * number2
    if result > 1000:
            sum = number1 + number2
            return sum

    else:
            return result

number1 = int(input("Enter 1st integer Number: "))
number2 = int(input("Enter 2nd integer Number: "))
answer = product(number1,number2)

print(answer)