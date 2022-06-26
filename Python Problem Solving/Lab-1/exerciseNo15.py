'''
Given a two list of numbers (hardcoded in the program), create a new list such that new list should
contain only odd numbers from the first list and even numbers from the second list.
'''

list1 = [12,2,4,5,8,9,22,14,15,77,98,5]
list2= [33,55,73,21,96,44,66,73,24,55,10]
newList =[]
for x in (list1):
    if x % 2 !=0:
        newList.append(x)
for y in (list2):
    if y % 2 ==0:
        newList.append(y)

print(newList)