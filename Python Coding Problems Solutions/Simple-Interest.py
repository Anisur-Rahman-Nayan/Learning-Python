principle =int(input("Money You Borrowed: "))
interest_rate = float(input("Interest Rate: "))
time = float(input("Overall Duration: "))

simple_interest = principle*(interest_rate/100) * time

print(f"Simple interest is {round(simple_interest,2)} taka only")