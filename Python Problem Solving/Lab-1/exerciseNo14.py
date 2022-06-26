'''
Given a string, write a python program to check if it is palindrome or not. Define a function named
palindrome_checker_<your-student-id> in your program.
'''


def palindromeChecker_2018_2_60_024(s):
   
    return s == s[::-1]

s = "nayan"
ans = palindromeChecker_2018_2_60_024(s)

if ans:
    print("Yes")
else:
    print("No")