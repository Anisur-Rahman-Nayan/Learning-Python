import random

def get_a_clue():
    clues = ['-a-e','y-ll-w','s-mm-r','wi-t-r','s-n-y','l-v-','-i-e']
    position = random.randint(0,len(clues)-1)
    clue = clues[position]
    return clue

def check_word_match(clue,guess):
    if (len(clue) != len(guess)):
        return False
    for i in range(len(clue)):
        if clue[i] != '-' and clue[i] != guess[i]:
            return False
    return True

word_clue = get_a_clue()
print("Your Word Clue :",word_clue)
ans =input("What would be the word: ")

is_matched = check_word_match(word_clue,ans)

if is_matched is True:
    print("WOW!!! You Win")
else:
    print("Opps! You missed it")