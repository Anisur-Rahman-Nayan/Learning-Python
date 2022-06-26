my_str = input("String to Check: ")
rev_str = my_str[:: -1]

if (my_str == rev_str):
    print("it is palindrome")
else:
    print("it is not palindrome")