def reverse_string(str):
    reverse = ""
    for char in str:
        reverse = char + reverse
    return reverse

str = input("Enter Your String: ")
result = reverse_string(str)
print(result)