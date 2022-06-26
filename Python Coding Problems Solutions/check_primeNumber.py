#A Prime number is only divisible by 1 and the number by itself

def prime_Number(num):

    for i in range(2,num):
        if (num % i == 0):
            return False
    return True

n = int(input("Enter a Number to check: "))

result = prime_Number(n)

if result :
    print("The Number is a Prime Number")
else:
    print("The Number is not a Prime Number")
