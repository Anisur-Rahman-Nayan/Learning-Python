'''
Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
the even-indexed elements in the list.
'''

list = [8,6,3,90,24,56,77,99,23,100,14]

sum = 0
for i in range(len(list)):
    if i%2 == 0:
        sum = sum + list[i]

print(f"The Sum is {sum}")