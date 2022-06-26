def get_sum(nums):
    sum =0
    for num in nums:
        sum = sum + num
    return sum

num = [10,9,8,7,6,5,4,3,2,1,11,12]
ans = get_sum(num)
print(ans)
