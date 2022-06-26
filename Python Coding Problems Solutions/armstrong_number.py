def check_armstrong(num):
    order = len(str(num))

    sum = 0

    temp= num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**order
        temp =temp // 10
    return num == sum

num = int(input("Enter your Number : "))

if check_armstrong(num):
    print(num, "is a armstrong number")
else:
    print(num, "is not a armstrong number")