'''
Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
the list. Do not use any built-in function.
'''

list = [8,6,3,90,24,56,77,99,23,100,14]

sum = 0
for x in list:
    sum = sum + x

print(f"The Sum is {sum}")
