try:
    num1 = int(input("ENTER 1st NUMBER : "))
    num2 = int(input("ENTER 2nd NUMBER : "))
    result = num1 / num2
    print(result)

except ValueError:
    print("You have to insert only integer")
except ZeroDivisionError:
    print("You can not devide a number by 0")

finally:
    print("Thanks !!!")