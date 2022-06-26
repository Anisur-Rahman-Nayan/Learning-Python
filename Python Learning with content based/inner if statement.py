number1 = int(input("Enter 1st Number : "))
number2 = int(input("Enter 2nd Number : "))
number3 = int(input("Enter 3rd Number : "))

if(number1 > number2):
         if(number1 > number3):
             print(f"{number1} is bigger")
         else:
             print(f"{number3}is bigger")
elif(number2 > number1):
         if(number2 > number3):
             print(f"{number2}is bigger")
         else:
             print(f"{number3}  is bigger")
