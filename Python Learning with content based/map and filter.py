
def square(x):
    return x*x

nums = [1,2,3,4,5,6,7,8,9,10]

result = list(map(square,nums))

print(result)




def even(y):
    return y%2==0

numbers = [1,2,3,4,5,6,7,8,9,10]

ans = list(filter(even,numbers))
print(ans)