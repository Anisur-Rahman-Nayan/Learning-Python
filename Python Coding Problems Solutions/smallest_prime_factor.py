def get_smallest_factor(num):
    factor = 2
    while num % factor !=0:
        factor = factor+1
    return factor

num = int(input("Enter Your Number : "))
ans = get_smallest_factor(num)
print("The smallest Prime factor is:", ans)