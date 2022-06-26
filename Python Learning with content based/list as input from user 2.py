numOfWords = 0
numOfLetters = 0
numOfDigits = 0

n = input("Enter a text of numbers : ")

for x in n :
    x = x.lower()
    if( x >= 'a' and x<= 'z'):
        numOfLetters = numOfLetters + 1
    elif (x >= '0' and x <= '9'):
        numOfDigits = numOfDigits + 1
    elif (x == " "):
        numOfWords = numOfWords + 1
print(numOfDigits)
print(numOfLetters)
print(numOfWords + 1)
