def voter(age):
    if age < 18 :
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
 text = voter(18)
 print(text)
except ValueError:
 print("Invalid age")