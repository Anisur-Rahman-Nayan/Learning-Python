
nums = [1,2,3,4,5,6,7,8,9,10]

# result = [x*x for x in nums]
result = list(filter(lambda x : x%2==0 , nums))

print(result)