import random

print("To stop anytime, enter: q")
score = 0

while True:
    num = random.randint(0,10)
    guess = int(input("Guess a number between 0 to 10 : "))

    if guess =="q":
        print("Game Over")
        break
    if guess is num :
        print("Congrats ! You guessed it correctly")
        score = score+10
        print("Your New Score: " ,score )
    else:
        print("Your guess did not match")
        print("The Number was : ", num)
