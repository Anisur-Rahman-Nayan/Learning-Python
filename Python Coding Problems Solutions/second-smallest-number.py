def get_second_smallest(nums):
    smallest = nums[0]
    second_smallest = nums[0]
    for i in range(1,len(nums)):
        if(nums[i] < smallest):
            second_smallest = smallest
            smallest = nums[i]

        elif (nums[i] < second_smallest):
            second_smallest = nums[i]
    return second_smallest

user_input = [44,11,83,29,25,76,88]
ans = get_second_smallest(user_input)
print(ans)