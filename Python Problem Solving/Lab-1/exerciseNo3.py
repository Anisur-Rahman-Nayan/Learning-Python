'''
Write a Python program to calculate the compound interest based on the given formula. Read inputs
from the user.
A = P * (1 + R/100)
T where P is the principle amount, R is the interest rate and T is time (in years).
Define a function named as compound_interest_<your-student-id> in your program.
'''

def compound_interest_2018_2_60_024(P,R,T):
    A = P * ((1+R/100)**T)
    return A

p = int(input("Enter the principle amount: "))
r = int(input("Enter the interest rate: "))
t = int(input("Enter the time in years: "))

result = compound_interest_2018_2_60_024(p,r,t)
print(f"Compound Interest is {round(result,2)}")
