'''
Given a string and an integer number n, remove characters from a string starting from zero up to n
and return a new string. N must be less than the length of the string. Read inputs from the user. Do
not use any built-in function.
'''

def remove_characters(text,num):
    list = ''
    for i in range(len(text)):
        if i > num:
            list = list + text[i]
    print(list)

text = str(input("Enter The Text Here :"))
num = int(input("Enter the index You want to remove from (index number must be smaller then text) :"))
remove_characters(text,num)
