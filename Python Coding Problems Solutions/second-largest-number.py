def get_second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]

    for i in range(1,len(nums)):
        if(nums[i] > largest ):
            second_largest = largest
            largest = nums[i]

        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest

user_input = [44,11,83,29,25,76,88]
second_largest = get_second_largest(user_input)
print(second_largest)