'''
Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
number based on the following assumptions.
Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1
'''
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")

    elif n == 1:
        return 0

    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


user_input= int(input("Enter a num n to calculate nth fibonacci number:  "))
ans = fibonacci(user_input)
print(ans)