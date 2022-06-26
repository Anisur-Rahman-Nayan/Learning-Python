def get_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

input = [0,15,68,1,0,-55]
ans = get_largest(input)

print(ans)