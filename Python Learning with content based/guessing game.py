from random import randint
## import random

for x in range(1,6):
    
    
    n = int(input("Enter the guessing Number between 1 to 5 : "))

    randomNumber = randint(1,5)
    ##randomNumber = random.random() * 100
    if(n == randomNumber):
        print("You have won")
    else:
        print("You have lost")
        print(f"The guessing Number is {randomNumber}")
