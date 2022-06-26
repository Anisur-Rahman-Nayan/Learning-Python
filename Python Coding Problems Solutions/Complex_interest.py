def compound_interest(principle,rate,time):
    interest = principle * ((1 + rate /100) ** time)
    return interest

p = int(input("Money You Borrowed: "))
r = float(input("Interest Rate: "))
t = float(input("Overall Duration: "))

total_due = compound_interest(p,r,t)
print("Interest Amount is ", total_due)