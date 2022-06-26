import string
import random

def randomPassword(size):
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ""
    password = password + random.choice(string.ascii_lowercase)
    password = password + random.choice(string.ascii_uppercase)
    password = password + random.choice(string.digits)
    password = password + random.choice(string.punctuation)

    for i in range(size-4):
        password = password + random.choice(all_char)
    return password

len = int(input("Enter would be the password length ?"))
print("1st Random Password is: ", randomPassword(len))
print("2nd Random Password is: ", randomPassword(len))
print("3rd Random Password is: ", randomPassword(len))