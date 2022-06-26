'''
Count the number of spaces in a string (use string above)
'''

name = "Practice problem to drill list comprehension in your head"

count = 0
for x in name:
    if x == " " :
        count = count+1
print(count)