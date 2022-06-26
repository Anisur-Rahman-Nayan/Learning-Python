'''
Given a list of numbers (hardcoded in the program), write a Python program to find the second
largest element of the list.
'''

x = [8,6,3,90,24,56,77,99,23,4,102,100,14,101,97]
x.sort()
print(f"2nd largest element is {x[-2]}")