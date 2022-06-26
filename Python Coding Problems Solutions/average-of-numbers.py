def sum_of_numbers(nums):
    sum = 0
    for x in nums:
        sum = sum + int(x)
        avg = sum / len(nums)
    return avg

user_input = input("Enter Numbers: ")
numbers = user_input.split()
result = sum_of_numbers(numbers)

print(round(result,2))