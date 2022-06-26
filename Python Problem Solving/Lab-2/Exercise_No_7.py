'''
Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any
single digit besides 1 (2–9)
'''


numbers = [i for i in [j for j in range(1,1001)] if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0 or i % 9 == 0 ]
print(numbers)