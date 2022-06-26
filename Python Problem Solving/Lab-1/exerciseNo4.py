'''
Given a positive integer N (read from the user), write a Python program to calculate the value of the
following series.
        1**2 + 2**2 + 3**2 + 4**2 + N**2
'''

def series(n):
    sum = 0
    for num in range(n):
        sum = sum + (num+1)**2
    return sum

num = int(input("Enter the last digit: "))
result = series(num)
print(f"The Sum is {result}")