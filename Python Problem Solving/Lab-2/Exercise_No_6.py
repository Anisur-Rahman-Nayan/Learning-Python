'''
Use a dictionary comprehension to count the length of each word in a sentence (use string above)
'''

def result():
    string = "Practice Problems to Drill List Comprehension in Your Head"
    words = string.split(" ")
    word_count =dict.fromkeys(words,0)


    for word in words:
        word_count[word] = len(word)

    for x,y in word_count.items():
        print(f"\"{x}\"s length is {y}")

if __name__ =='__main__':
    result()