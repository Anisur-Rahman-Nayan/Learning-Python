def get_winner(p1,p2):
    if p1 == p2:
        return "it's tie !"
    elif p1 == 'rock':
        if p2 == 'scissor':
            return "1st player wins !"
        else:
            return "2nd player wins !"
    elif p1 == 'scissor':
        if p2 == 'paper':
            return "1st player wins !"
        else:
            return "2nd player wins!"
    elif p1 == 'paper':
        if p2 == 'rock':
            return '1st players win !'
        else:
            return "2nd player wins !"
    else:
        return "Invalid input !"

player1 = input("1st player : rock ,paper,scissors: ")
player2 = input("1st player : rock ,paper,scissors: ")

print(get_winner(player1,player2))