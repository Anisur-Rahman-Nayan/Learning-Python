'''
Remove all of the vowels in a string (use string above)
'''


def avoid_vowel(text):
    for i in "aeiou":
        text = text.replace(i,'')
    return text


name = "Practice problem to drill list comprehension in your head"
name1 = name.lower()
ans = avoid_vowel(name1)
print(ans)

