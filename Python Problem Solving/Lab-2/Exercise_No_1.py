'''
Find all of the numbers from 1–1000 that are divisible by 8
'''

def divisibleBy8(x):
    return x%8 == 0


nums = [i for i in range(1,1001)]
ans = list(filter(divisibleBy8,nums))
print(ans)