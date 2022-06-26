def square_sum(num):
    sum = 0
    for x in range(num+1):
        sum = sum + (x**2)
    return sum

num = int(input("Enter Numbers: "))
total = square_sum(num)

print(total)