'''
Given a positive integer N (read from the user), write a Python program to check if the number is
prime or not. Define a function named as prime_find_<your-student-id> in your program.
'''

def prime_find_2018_2_60_024(n):
    s = 0
    for num in range(2,n+1):
        if n % num == 0:
            s = s + 1
    if s < 2:
        return "The number is Prime Number"
    else :
        return "The number is not Prime Number"

user_input = int(input("Enter the number to check prime or not : "))
ans = prime_find_2018_2_60_024(user_input)
print(ans)