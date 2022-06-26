def Prime_factors(num):
    factors = []
    divisor = 2
    while num > 2:
            if(num % divisor == 0):
                factors.append(divisor)
                num = num/divisor
            else:
                divisor = divisor + 1
    return factors

n = int(input("Enter your Number : "))
ans = Prime_factors(n)
print(ans)