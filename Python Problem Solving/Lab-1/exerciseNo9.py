'''
Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
smallest element of the list. Define two functions largest_number_<your-student-id> and
smallest_number_<your-student-id> in your program. Do not use any built-in function.
'''
list = [3,8,6,3,90,24,56,77,99,23,4,102,100,14,101]

def largest_number_2018_2_60_024(list):
    for i in range(len(list)):
        largest = list[0]
        if largest < list[i]:
            largest = list[i]
    return largest

def smallest_number_2018_2_60_024(list):
    for i in range(len(list)):
        smallest = list[0]
        if smallest > list[i]:
            smallest = list[i]
    return smallest

ans1 = largest_number_2018_2_60_024(list)
print(ans1)
ans2 = smallest_number_2018_2_60_024(list)
print(ans2)