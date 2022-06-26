'''
Find all of the words in a string that are less than 5 letters (use string above)
'''

def string_less_5(text):
    string =[]
    text = text.split(" ")
    for x in text:
        if len(x) < 5 :
            string.append(x)
    return string

t= "Practice problem to drill list comprehension in your head"
ans = string_less_5(t)
print(ans)