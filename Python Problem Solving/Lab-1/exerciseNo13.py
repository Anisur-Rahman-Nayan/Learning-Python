'''
Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
built-in function.
'''

text = "CSE303"
c = 0
for i in range(len(text)):
    if text[i] >= 'A' and text[i]<='Z':
        c = c+1
print(c)

