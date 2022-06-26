def prime_number(num):
    for i in range(2,num):
        if (num % i == 0):
            return False
    return True

def all_prime_number(num):
    primes =[]
    for n in range(2,num+1):
        if prime_number(n) is True:
            primes.append(n)
    return primes

num = int(input("Enter Upper limit: "))
primes = all_prime_number(num)
print(primes)
