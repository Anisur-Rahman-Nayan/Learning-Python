def cube_sum(num):
    sum = 0
    for n in range(num+1):
        sum = sum + num**3
    return sum

user_num = int(input("Enter a Number : "))
result = cube_sum(user_num)
print("Your Sum of cubes are : ", result)